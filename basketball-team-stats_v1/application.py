from itertools import cycle

import constants
from basketball_teams import BasketballTeam
from basketball_players import BasketballPlayer


TEAM = constants.TEAMS
PLAYERS = constants.PLAYERS


def sort_players(players):
    sorted_players = sorted(players, key=lambda x: int(x['height'][:2]), reverse=True)
    sorted_players = sorted(sorted_players, key=lambda x: x['experience'] == 'YES', reverse=True)
    sorted_players = sorted(sorted_players, key=lambda x: ' and ' in x['guardians'], reverse=True)

    return sorted_players


def create_balanced_teams(teams, players):
    # Create instances of BasketballTeam for each team
    basketball_teams = [BasketballTeam(team_name) for team_name in teams]

    # Add players to teams in a round-robin fashion
    for player_data, team in zip(players, cycle(basketball_teams)):
        player = BasketballPlayer(**player_data)
        team.add_player(player)

    return basketball_teams


class App(object):
    """Class for all the functions of the app """

    @staticmethod
    def run_menu():
        teams = create_balanced_teams(TEAM, sort_players(PLAYERS))

        while True:
            print("BASKETBALL TEAM STATS TOOL \n \n" + "-" * 15 + "Menu" + "-" * 15)
            print(" \n Here are your choices: \n 1) {} \n 2) {} \n ".format("Display Team Stats", "Quit"))

            try:
                chosen_pick = int(input("Enter an option > "))

                if chosen_pick == 1:
                    for i, team in enumerate(TEAM):
                        print(f"{i + 1}) {team}")

                    chosen_team = int(input("Enter the team number: "))
                    if 1 <= chosen_team <= len(TEAM):
                        team_name = TEAM[chosen_team - 1]
                        App.show_players_on_team(teams, team_name)
                        input("\n \n Press Enter to continue...")
                    else:
                        print("Invalid team number. Please choose again.")

                elif chosen_pick == 2:
                    break

            except ValueError:
                print("Invalid input. Please enter a valid option.")
            else:
                print("Invalid input. Please enter a valid option.")

    @staticmethod
    def show_players_on_team(teams, team_name):
        for team in teams:
            if team.team_name == team_name:
                print(f"Players for {team_name}:")
                for player in team.players:
                    print(player)
                break
        else:
            print(f"Team {team_name} not found.")


if __name__ == "__main__":
    App.run_menu()

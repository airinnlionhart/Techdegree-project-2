import constants

# this is my first attempt at this project check out application.py which is my refactor of this app

THE_TEAMS = constants.TEAMS
the_list_of_players = constants.PLAYERS
experienced_players = []
non_experienced_players = []
guardians = []
PANTHERS = []
BANDITS = []
WARRIORS = []
avg_height_exp = []
avg_height_inexp = []


class PrintToScreen(object):
    """Class for printing out to terminal"""

    def __init__(self, team):
        self.team = team

    def print_team_info(self):
        print("\n Team: Panthers Stats \n" + "-" * 25 + "\n Total players: {} \n".format(len(self)))
        print("Players on Team:")
        print(', '.join(self))
        if self == PANTHERS:
            avg = (sum(avg_height_exp[:3]) + sum(avg_height_inexp[:3])) / 6
        elif self == BANDITS:
            avg = (sum(avg_height_exp[3:6]) + sum(avg_height_inexp[3:6])) / 6
        else:
            avg = (sum(avg_height_exp[6:]) + sum(avg_height_inexp[6:])) / 6
        print("\nAverage height of team:", round(avg), "inches")
        print("\nList of guardians:")

    @staticmethod
    def print_tools_name():
        print("BASKETBALL TEAM STATS TOOL \n \n" + "-" * 15 + "Menu" + "-" * 15)

    @staticmethod
    def show_teams():
        print("\n 1) {} \n 2) {} \n 3) {} \n".format(THE_TEAMS[0], THE_TEAMS[1], THE_TEAMS[2]))

    @staticmethod
    def show_players_on_team():
        while True:
            try:
                chosen_pick = int(input("Enter an option > "))
                if chosen_pick == 1:
                    panthers = PrintToScreen
                    panthers.print_team_info(PANTHERS)
                    PrintToScreen.show_players_guardians(PANTHERS)
                    break
                elif chosen_pick == 2:
                    bandits = PrintToScreen
                    bandits.print_team_info(BANDITS)
                    PrintToScreen.show_players_guardians(BANDITS)
                    break
                elif chosen_pick == 3:
                    bandits = PrintToScreen
                    bandits.print_team_info(WARRIORS)
                    PrintToScreen.show_players_guardians(WARRIORS)
                    break
            except ValueError:
                print(
                    "Sorry about that we where expect a 1 for Panthers and a 2 for Bandits or 3 for Warriors try again")
            else:
                print(
                    "Sorry about that we where expect a 1 for Panthers and a 2 for Bandits or 3 for Warriors try again")

    def show_players_guardians(self) -> object:
        player_guardians = []
        for player_name in self:
            for players in the_list_of_players:
                if players['name'] == player_name:
                    player_guardians.append(player_name + " guardians(s): " + players['guardians'])
        print(', '.join(player_guardians))


class App(object):
    """Class for all the function of the app """

    @staticmethod
    def run_menu():
        while True:
            PrintToScreen.print_tools_name()
            print(" \n Here are your choices: \n 1) {} \n 2) {} \n ".format("Display Team Stats", "Quit"))
            try:
                chosen_pick = int(input("Enter an option > "))
                if chosen_pick == 1:
                    PrintToScreen.show_teams()
                    PrintToScreen.show_players_on_team()
                    input("\n \n Press Enter to continue...")
                elif chosen_pick == 2:
                    break
            except ValueError:
                print(
                    "Sorry about that we where expect a 1 for {} and a 2 for {} try again".format("Display Team Stats",
                                                                                                  "Quit"))
            else:
                print(
                    "Sorry about that we where expect a 1 for {} and a 2 for {} try again".format("Display Team Stats",
                                                                                                  "Quit"))

    @staticmethod
    def sort_players():
        global PANTHERS, BANDITS, WARRIORS
        for player in the_list_of_players:
            if player['experience'] == 'YES':
                player['experience'] = True
                player['height'] = int(player["height"][:2])
                experienced_players.append(player['name'])
                avg_height_exp.append(player['height'])
                guardians.append(player['name'] + ' garudians are ' + player['guardians'])
            else:
                non_experienced_players.append(player['name'])
                player['experience'] = False
                player['height'] = int(player["height"][:2])
                avg_height_inexp.append(player['height'])
                guardians.append(player['name'] + ' garudians are ' + player['guardians'])
        PANTHERS = experienced_players[:3] + non_experienced_players[:3]
        BANDITS = experienced_players[3:6] + non_experienced_players[3:6]
        WARRIORS = experienced_players[6:] + non_experienced_players[6:]
        return PANTHERS, BANDITS, WARRIORS


def main():
    App.sort_players()
    App.run_menu()


if __name__ == "__main__": main()

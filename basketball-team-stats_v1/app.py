import constants 

THE_TEAMS = constants.TEAMS
the_list_of_players = constants.PLAYERS
experienced_players = []
non_experienced_players = []
PANTHERS = []
BANDITS = []
WARRIORS = []
avg_height_exp = []
avg_height_inexp = []

def sort_players():
    global PANTHERS, BANDITS, WARRIORS
    for player in the_list_of_players:
        if (player['experience']== 'YES'):
            player['experience'] = True
            player['height'] = int(player["height"][:2])
            experienced_players.append(player['name'])
            avg_height_exp.append(player['height'])
        else:
            non_experienced_players.append(player['name'])
            player['experience'] = True
            player['height'] = int(player["height"][:2])
            avg_height_inexp.append(player['height'])
    PANTHERS = experienced_players[:3] + non_experienced_players[:3]
    BANDITS = experienced_players[3:6] + non_experienced_players[3:6]
    WARRIORS = experienced_players[6:] + non_experienced_players[6:]
    return(PANTHERS, BANDITS, WARRIORS)


def print_tools_name():
    print("BASKETBALL TEAM STATS TOOL \n \n" + "-"*15 + "Menu" + "-"*15)


def show_teams():
    print("\n 1) {} \n 2) {} \n 3) {} \n".format(THE_TEAMS[0],THE_TEAMS[1],THE_TEAMS[2]))

    
def show_players_on_team():
    while True:
        try:
            chosen_pick = int(input("Enter an option > "))
            if chosen_pick == 1:
                print("\n Team: Panthers Stats \n" + "-"*25 + "\n Total players: {} \n".format(len(PANTHERS)))
                print("Players on Team:")
                for player in PANTHERS:
                    if player == PANTHERS[-1]:
                        print(player, end=' ')
                    else:
                        print(player+",", end=' ')
                avg = (sum(avg_height_exp[:3]) + sum(avg_height_inexp[:3]))/6
                print("\nAverage height of team:", round(avg) , "inches")
                break  
            elif chosen_pick == 2:          
                print("\n Team: Bandits Stats \n" + "-"*25  + "\n Total players: {} \n".format(len(BANDITS)))
                print("Players on Team:")
                for player in BANDITS:
                    if player == BANDITS[-1]:
                    	   print(player, end=' ')
                    else:
                        print(player+",", end=' ')
                avg = (sum(avg_height_exp[3:6]) + sum(avg_height_inexp[3:6]))/6
                print("\nAverage height of team:", round(avg) , "inches")        
                break 
            elif chosen_pick == 3:          
                print("\n Team: Warriors Stats \n" + "-"*25 + "\n Total players: {}\n".format(len(WARRIORS)))
                print("Players on Team:")
                for player in WARRIORS:
                    if player == WARRIORS[-1]:
                        print(player, end=' ')
                    else:
                        print(player+",", end=' ')
                avg = (sum(avg_height_exp[3:6]) + sum(avg_height_inexp[3:6]))/6
                print("\nAverage height of team:", round(avg) , "inches")          
                break
        except ValueError:
            print("Sorry about that we where expect a 1 for Panthers and a 2 for Bandits or 3 for Warriors try again")
        else:
	    	      print("Sorry about that we where expect a 1 for Panthers and a 2 for Bandits or 3 for Warriors try again")

def run_menu():
    print(" \n Here are your choices: \n 1) {} \n 2) {} \n ".format("Display Team Stats","Quit"))
    while True:
        try:
            chosen_pick = int(input("Enter an option > "))
            if chosen_pick == 1:
                sort_players()
                show_teams()
                show_players_on_team()
                break
            elif chosen_pick == 2:
                break
        except ValueError:
            print("Sorry about that we where expect a 1 for {} and a 2 for {} try again".format("Display Team Stats","Quit"))
        else:
            print("Sorry about that we where expect a 1 for {} and a 2 for {} try again".format("Display Team Stats","Quit"))


            
if __name__ == "__main__":
    
    
        print_tools_name()
        run_menu()
        input("\n \n Press enter to continue")

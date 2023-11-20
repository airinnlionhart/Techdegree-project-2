class BasketballTeam:
    """Class representing a basketball team.

    Attributes:
        team_name (str): The name of the basketball teams.
    """

    def __init__(self, team):
        """Initialize a BasketballTeam instance.

        Args:
            team (str): The name of the basketball teams.

        """
        self.team_name = team
        self.players = []

    def add_player(self, player):
        self.players.append(player)
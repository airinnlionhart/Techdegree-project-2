class BasketballPlayer:
    """Class representing a player.

       Attributes:
           name (str): the players name.
           experience (bool): True or False based on experience.
           height (int): the players name.
           guardians (str): the players name.
       """

    def __init__(self, name, experience, height, guardians):
        self.name = name
        self.experience = self._convert_to_boolean(experience)
        self.height = int(height[:2])
        self.guardians = guardians

    @staticmethod
    def _convert_to_boolean(experience_str):
        """Convert a string representation of experience to a boolean."""
        return experience_str.upper() == 'YES'

    def __str__(self):
        return f"Name: {self.name}, Experience: {self.experience}, Height: {self.height} inches, " \
               f"Guardians: {self.guardians}"
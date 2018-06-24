from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mygame'
    players_per_group = 3
    num_rounds = 3
    stakes =c(100)
    instructions_template = 'mygame/Instructions.html'	


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pts = models.FloatField()
    
    def set_payoffs(self):
        players = self.get_players()
        pts = [p.pts for p in self.group()]
    def other_player(self):
        return self.get_others_in_group()[0]   

class Player(BasePlayer):
    pts = models.PositiveIntegerField(min=0, max=100)
    def other_player(self):
        return self.get_others_in_group()[0]    
    def other_player2(self):
        return self.get_others_in_group()[1]    
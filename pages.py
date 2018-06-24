# from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
       return self.round_number==1
    pass

class MyPage(Page):
    form_model = models.Player
    form_fields = ['pts']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
       pass
class Results(Page):
   def vars_for_template(self):
        me = self.player
        opp=me.other_player()
        opp2 =me.other_player2()
        pts_list=[0,0,0]
        pt=[]
        for i in range (3):
            if self.player.id_in_group == i+1:
                pts_list[i]=sum(list(x.pts for x in self.player.in_all_rounds()))
            if opp.id_in_group ==i+1:
                pts_list[i]=sum(list(x.pts for x in opp.in_all_rounds()))
            if opp2.id_in_group ==i+1:
                pts_list[i]=sum(list(x.pts for x in opp2.in_all_rounds()))  
        if sum(p.pts for p in self.player.in_all_rounds()) == max(pts_list):
            return{
                'pts':sum(p.pts for p in self.player.in_all_rounds()),
                'rank':1
            }
        elif sum(p.pts for p in self.player.in_all_rounds()) == min(pts_list) and pts_list.count(min(pts_list))==1:
            return{
                'pts':sum(p.pts for p in self.player.in_all_rounds()),
                'rank':3
            }
        else:
            return{
                'pts':sum(p.pts for p in self.player.in_all_rounds()),
                'rank':2
            }
class Final(Page):
   def is_displayed(self):
       return self.round_number== Constants.num_rounds
   def vars_for_template(self):
        return {
	      'player_in_all_rounds': self.player.in_all_rounds(),
	      'pts': sum(p.pts for p in self.player.in_all_rounds())
	}
   pass


page_sequence = [
    Introduction,
    MyPage,
    ResultsWaitPage,
    Results,
    Final,]

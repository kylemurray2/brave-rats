import random
import ipdb
from components import cards

def seans_brain_fn(player, game, spied_card):
    '''The most sophisticated Brave Rats AI ever written
    Expects to be called once each time a card needs to be played, and once after the game is over.

    :param player: a Player instance
    :param game: a Game instance, used to look up info about played cards, score, etc.
    :param spied_card: If I successfully played a spy last turn, this is the card that the opponent has revealed and
        will play. Otherwise, None
    :return: a card from my player's hand with which to vanquish my opponent, or None if the game is over
    '''
    
    def hand(game, player):
        '''
        Calculate a player's hand from the move history stored in the game instance.
       '''
        cards_played=[cardpair[player.color.value-1] for cardpair in game.all_fights]
        hand = [card for card in cards.initial_hand() if card not in cards_played]
        return hand
	
    #ipdb.set_trace()
    card_to_play = None
    if spied_card:
      print 'A {}? Prepare to be MURDALIZED!'.format(spied_card.name)
      if spied_card.name == 'prince':
	for card in player.hand:
	  if card.name in ['princess','assassin','musician']:
	    card_to_play = card
      elif spied_card.name == 'general':
	for card in player.hand:
	  if card.name in ['assassin','general','musician']:
	    card_to_play = card
      elif spied_card.name == 'wizard':
	for card in player.hand:
	  if card.name in ['general','wizard']:
	    card_to_play = card
      elif spied_card.name == 'ambassador':
	for card in player.hand:
	  if card.name in ['general','wizard','assassin','ambassador','musician']:
	    card_to_play = card
      elif spied_card.name == 'assassin':
	for card in player.hand:
	  if card.name in ['wizard','assassin','musician']:
	    card_to_play = card
      elif spied_card.name == 'princess':
	for card in player.hand:
	  if card.name in ['wizard','ambassador','spy','princess','musician']:
	    card_to_play = card
      elif spied_card.name == 'musician':
	for card in player.hand:
	  if card.name in ['princess','assassin','musician']:
	    card_to_play=card
      elif spied_card.name == 'spy':
	for card in player.hand:
	  if card.name in ['prince','general','wizard','ambassador','spy','musician']:
	    card_to_play=card
      if card_to_play:
	return card_to_play
      else:
	return player.hand[-1] 
    else:
      try:
	print 'tried to play last card'
	return player.hand[-1] 
      except IndexError:
	#ipdb.set_trace()
	pass
  
    
from django.db import models

#model for the player object, which just contains the information needed for someone to play the drug dealer game
class Player(models.Model):
	#enum for the rols in the game
	class GameRoles(models.IntegerChoices):
			Druggie = 1
			DrugDealer = 2
			Cop = 3
	#setting primary key to be true to make sure each player has a unique id
	primary_key = True
	#username that a player can enter 
	user_name = models.CharField(max_length=30)
	#the storage of the player role enum
	game_role = models.IntegerField(choices=GameRoles.choices)
	#boolean to see if the player is still containned in the game or not
	is_arrested = models.BooleanField(default=False)

	#assignning the name of the object to be the username in the data when looking at these objects
	def __str__(self):
			return self.userName

#model for a game/room to contain all of the players
class Game(models.Model):
	#setting a unique player id
	primary_key=True
	#foriegn key constraint to attach all of the players contained in the game to the room 
	all_players = models.ForeignKey(Player, on_delete=models.CASCADE)
	#the unique join code for the game, can change the length of this value latter on, 2 seemed enough for testing purposes
	join_code = models.CharField(max_length=2)

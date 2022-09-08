from django.db import models


class Game(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    name = models.CharField(max_length=80)


class Character(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    name = models.CharField(max_length=80)


class CharacterPlayed(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    name = models.CharField(max_length=80)
    game_instance = models.ForeignKey(Game, related_name="game_character_played", on_delete=models.CASCADE)
    character = models.ForeignKey(Character, related_name="character_character_played", on_delete=models.CASCADE)
    level = models.IntegerField(blank=True, null=True)


class Player(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    username = models.CharField(max_length=80)
    score = models.IntegerField(blank=True, null=True)
    avatar = models.ImageField(upload_to="profiles/avatars", null=True, blank=True)


class GameInstance(models.Model):
    player = models.ForeignKey(Player, related_name="game_instance_player", null=True, on_delete=models.SET_NULL)
    game = models.ForeignKey(Game, related_name="game_instance_game",  on_delete=models.CASCADE)

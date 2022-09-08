from django.db import models


class Game(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    name = models.CharField(max_length=250)
    players_count = models.IntegerField(blank=True, null=True)


class Player(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    username = models.CharField(max_length=80)
    score = models.IntegerField(blank=True, null=True)
    avatar = models.ImageField(upload_to="profiles/avatars", null=True, blank=True)
    game = models.ForeignKey(Game, related_name="game_player", null=True, on_delete=models.SET_NULL)
    is_banned = models.BooleanField(default=False)


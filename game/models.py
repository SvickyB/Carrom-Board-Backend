from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=255)


class Game(models.Model):
    player1 = models.ForeignKey(Player, related_name="player1", on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name="player2", on_delete=models.CASCADE, null=True, blank=True)
    is_ai = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=[("ongoing", "Ongoing"), ("completed", "Completed")], default="ongoing")
    created_at = models.DateTimeField(auto_now_add=True)

class Piece(models.Model):
    x_position = models.FloatField()
    y_position = models.FloatField()
    is_pocketed = models.BooleanField(default=False)
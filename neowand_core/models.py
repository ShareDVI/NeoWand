from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Wizard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    power = models.PositiveIntegerField(default=0)
    mana = models.PositiveIntegerField()


class Spell(models.Model):
    name = models.CharField(max_length=64)


class AuraSpell(models.Model):
    source = models.ForeignKey(Wizard, related_name='source')
    target = models.ForeignKey(Wizard, related_name='target')
    spell = models.ForeignKey(Spell)
    mana = models.PositiveIntegerField()

# User knows spells
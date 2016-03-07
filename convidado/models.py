from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.IntegerField()
    id.primary_key = True
    nome = models.CharField(max_length=200)
    confirmado = models.BooleanField()

    def publish(self):
        self.save()

    def getNome(self):
        return self.nome

    def getId(self):
        return self.id

    def getConfirmado(self):
        return self.confirmado

class User(models.Model):
    user = models.OneToOneField(User)



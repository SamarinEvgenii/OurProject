from django.contrib.auth.models import User
from django.db import models

from django.conf import settings

auth_user = settings.AUTH_USER_MODEL if getattr(
    settings, "AUTH_USER_MODEL") else User

class Client(models.Model):
    """Пользователь"""
    user = models.ForeignKey(auth_user, on_delete = models.CASCADE)
    description = models.TextField("Информация о пользователе")
    email = models.EmailField("email")
    id = models.IntegerField("id")

    def __str__(self):
        return self.description
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Room(models.Model):
    room = models.IntegerField("Номер аудитории")

    def __str__(self):
        return self.room

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"


class Reservations(models.Model):
    request_number = models.IntegerField("Номер заявки")
    room_number = models.IntegerField("Номер аудитории", Room)
    user_id = models.IntegerField("id пользователя", Client)
    booking_date_time_start = models.DateTimeField("Начало бронирования")
    description = models.TextField("Описание заявки")

    def __str__(self):
        return self.request_number
    def __str__(self):
        return self.room_number
    def __str__(self):
        return self.user_id
    def __str__(self):
        return self.booking_date_time_start
    def __str__(self):
        return self.description


    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "заявки"






# Create your models here.

from django.db import models

class StandaloneTraffic(models.Model):
    """ Здесь мы создаем модель StandaloneTraffic с полями id, timestamp, username, request и response,
    которые соответствуют столбцам таблицы standalone_traffic. """
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()  # старая версия
    # timestamp = models.DateTimeField(default=now)  # новая версия
    # timestamp = models.DateTimeField(auto_now_add=True)  # ещё новее
    username = models.CharField(max_length=255, blank=False)
    request = models.TextField()
    response = models.TextField()


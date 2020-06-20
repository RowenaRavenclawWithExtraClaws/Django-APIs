from django.db import models


class Item(models.Model):
    content = models.CharField(max_length=120)
    pub_date = models.DateTimeField(auto_now=True)
    todo_date = models.DateTimeField()

    def __str__(self):
        return self.content

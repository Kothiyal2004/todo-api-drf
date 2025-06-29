from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    class Meta:
        db_table = 'todos_tables'
# Create your models here.

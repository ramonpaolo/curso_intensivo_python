from django.db import models

class Topicos(models.Model):

    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entre(models.Model):
    topico = models.ForeignKey(Topicos, on_delete=models.PROTECT)
    text = models.TextField()
    add_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
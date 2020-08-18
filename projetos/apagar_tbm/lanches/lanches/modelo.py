from django.db import models

class Categoria(models.Model):
    text = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Especificacao(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:15] + "..."
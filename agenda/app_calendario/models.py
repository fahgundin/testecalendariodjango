from django.db import models

class Registros(models.Model):
    idregistro = models.IntegerField(primary_key=True)
    data = models.DateField(null = True)
    oqfoifeito = models.TextField(max_length=255, null = False, blank = False)
    

from django.db import models

# Create your models here.

class Tier(models.Model):
    id_tier = models.AutoField(db_column='idTier', primary_key=True)
    tier = models.CharField(max_length=1, blank=False, null=False)
def __str__(self):
    return str(self.tier)

class Usuario(models.Model):
    id_usu = models.CharField(max_length=3,primary_key="true")
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank="false", null="true")
    password = models.CharField(max_length=30, blank="true", null="true")
    id_tier = models.ForeignKey(
        "Tier", on_delete=models.CASCADE, db_column="IDTier"
    )
    
def __str__(self):
    return str(self.nombre) +" " + str(self.apellido_paterno)
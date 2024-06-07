from django.db import models

# Create your models here.

class Tier(models.Model):
    id_tier = models.AutoField(db_column='idTier', primary_key=True)
    tier = models.CharField(max_length=1, blank=False, null=False)

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank="false", null="true")
    password = models.CharField(max_length=30, blank="true", null="true")
    id_tier = models.ForeignKey(
        "Tier", on_delete=models.CASCADE, db_column="IDTier"
    )
    activo = models.IntegerField()

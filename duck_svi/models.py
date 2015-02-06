from django.db import models
from django_apogee.models import Etape
# Create your models here.


class WishSvi(models.Model):
    code_dossier = models.CharField(db_column='NumDossier', primary_key=True, max_length=10)
    password = models.CharField(db_column='Password', null=False, default='1234', max_length=10)
    etat = models.CharField(db_column='Etat', null=False, max_length=250)
    gestionaire_etape = models.CharField(db_column='GestModif', null=False, max_length=6)
    psycho = models.BooleanField(db_column='Psycho', null=False)
    gestionaire_equiv = models.CharField(db_column='GestEquiv', null=True, max_length=6)
    gestionaire_bourse = models.CharField(db_column='GestBourse', null=False, max_length=6)

    class Meta:
        db_table = "ied_etudiant"



class GestToEtape(models.Model):
    code_gestionaire = models.CharField(primary_key=True, max_length=6)
    etape = models.ForeignKey(Etape, null=False)
    nom = models.CharField(null=True, max_length=100)
    prenom = models.CharField(null=True, max_length=200)




# -*- coding: utf-8 -*-
import random
from django.conf import settings
from django_apogee.models import AnneeUni, VersionEtape as VersionEtapeApogee, EtpGererCge, Etape
from duck_inscription.models import SettingAnneeUni, SettingsEtape, Wish
from duck_svi.models import WishSvi

__author__ = 'paul'
from django.core.management.base import BaseCommand
APOGEE_CONNECTION = getattr(settings, 'APOGEE_CONNECTION', 'oracle')


def get_gestionaire(wish):
    #pour l'instant des donéés bidon mais plus tard ... ici on va choisir le bon gestionaire
    sequence_gestionaire = ['GEST01', 'GEST02', 'GEST03']
    return random.choice(sequence_gestionaire)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for wish in Wish.objects.all():
            try:
                #on verifie si il existe deja dans la base de données
                wish_svi = WishSvi.objects.get(code_dossier=wish.code_dossier)
                #update if passed
                wish_svi.code_dossier = wish.code_dossier
                wish_svi.password = "1234"
                wish_svi.etat = "TEST"
                wish_svi.psycho = random.choice([True, False])
                wish_svi.gestionaire_bourse = get_gestionaire(wish)
                wish_svi.gestionaire_equiv = get_gestionaire(wish)
                wish_svi.gestionaire_etape = get_gestionaire(wish)
                print "Updated a wish"
            except WishSvi.DoesNotExist:
                # c'est une nouvelle creation
                WishSvi.objects.create(code_dossier=wish.code_dossier,
                                       password='1234',
                                       etat='Test',
                                       gestionaire_etape=get_gestionaire(wish),
                                       psycho=random.choice([True, False]),
                                       gestionaire_equiv=get_gestionaire(wish),
                                       gestionaire_bourse=get_gestionaire(wish)
                                       )
                text_to_announce = "Created new wish_svi code %s" % wish.code_dossier
                print text_to_announce





















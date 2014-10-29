# -*- coding: utf-8 -*-
import random
from django.conf import settings
from django_apogee.models import AnneeUni, VersionEtape as VersionEtapeApogee, EtpGererCge, Etape
from duck_inscription.models import SettingAnneeUni, SettingsEtape, Wish, SuiviDossierWorkflow
from duck_svi.models import WishSvi

__author__ = 'paul'
from django.core.management.base import BaseCommand
APOGEE_CONNECTION = getattr(settings, 'APOGEE_CONNECTION', 'oracle')
import string
alphabet = list(string.ascii_lowercase)
dict_gest={
    "L1NPSY": {'gest': ['GEST01', 'GEST02'], "psycho": True, 'bourse': "GEST22"},
    "L1NDRO": {'gest': ['GEST05'], "psycho": False, 'bourse': "GEST22"},
    "L1NINF": {'gest': ['GEST08'], "psycho": False, 'bourse': "GEST22"},
    "L2NPSY": {'gest': ['GEST03'], "psycho": False, 'bourse': "GEST22"},
    "L3NPSY": {'gest': ['GEST04'], "psycho": False, 'bourse': "GEST22"},
    "L2NDRO": {'gest': ['GEST06'], "psycho": False, 'bourse': "GEST22"},
    "L3NDRO": {'gest': ['GEST07'], "psycho": False, 'bourse': "GEST22"},
    "L2NINF": {'gest': ['GEST09'], "psycho": False, 'bourse': "GEST22"},
    "L3NINF": {'gest': ['GEST10'], "psycho": False, 'bourse': "GEST22"},
    "L3NEDU": {'gest': ['GEST11'], "psycho": False, 'bourse': "GEST22"},
    "M1NEFI": {'gest': ['GEST12'], "psycho": False, 'bourse': "GEST22"},
    "M2NEFI": {'gest': ['GEST13'], "psycho": False, 'bourse': "GEST22"},
    "M1NPEA": {'gest': ['GEST14'], "psycho": False, 'bourse': "GEST22"},
    "M2NPEA": {'gest': ['GEST15'], "psycho": False, 'bourse': "GEST22"},
    "M1NPST": {'gest': ['GEST16'], "psycho": False, 'bourse': "GEST22"},
    "M2NPST": {'gest': ['GEST17'], "psycho": False, 'bourse': "GEST22"},
    "DSNATA": {'gest': ['GEST18'], "psycho": False, 'bourse': "GEST22"},
    "M1NPCL": {'gest': ['GEST19'], "psycho": False, 'bourse': "GEST22"},
    "M2NPCL": {'gest': ['GEST20'], "psycho": False, 'bourse': "GEST22"}


}

def get_gestionaire(wish):
    #pour l'instant des donéés bidon mais plus tard ... ici on va choisir le bon gestionaire
    if dict_gest[wish.etape.cod_etp]["psycho"]:
        if wish.individu.last_name[0].upper() > "K":
            return dict_gest[wish.etape.cod_etp]['gest'][1]

    return dict_gest[wish.etape.cod_etp]['gest'][0]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for wish in Wish.objects.filter(etape__in=dict_gest.keys(), annee__cod_anu=2014):
            try:
                #on verifie si il existe deja dans la base de données
                wish_svi = WishSvi.objects.get(code_dossier=wish.code_dossier)
                #update if passed
                wish_svi.code_dossier = wish.code_dossier
                wish_svi.password = "1234"
                wish_svi.etat = SuiviDossierWorkflow.states[wish.suivi_dossier].title,
                wish_svi.psycho = dict_gest[wish.etape.cod_etp]["psycho"]
                wish_svi.gestionaire_bourse = dict_gest[wish.etape.cod_etp]["bourse"]
                wish_svi.gestionaire_equiv = get_gestionaire(wish)
                wish_svi.gestionaire_etape = get_gestionaire(wish)
                wish_svi.save()
                print "Updated a wish"
            except WishSvi.DoesNotExist:
                # c'est une nouvelle creation
                WishSvi.objects.create(code_dossier=wish.code_dossier,
                                       password='1234',
                                       etat=SuiviDossierWorkflow.states[wish.suivi_dossier].title,
                                       gestionaire_etape=get_gestionaire(wish),
                                       psycho=dict_gest[wish.etape.cod_etp]["psycho"],
                                       gestionaire_equiv=get_gestionaire(wish),
                                       gestionaire_bourse=dict_gest[wish.etape.cod_etp]["bourse"]
                                       )
                text_to_announce = "Created new wish_svi code %s" % wish.code_dossier
                print text_to_announce





















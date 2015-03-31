# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_apogee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GestToEtape',
            fields=[
                ('code_gestionaire', models.CharField(max_length=6, serialize=False, primary_key=True)),
                ('nom', models.CharField(max_length=100, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('etape', models.ForeignKey(to='django_apogee.Etape')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WishSvi',
            fields=[
                ('code_dossier', models.CharField(max_length=10, serialize=False, primary_key=True, db_column=b'NumDossier')),
                ('password', models.CharField(default=b'1234', max_length=10, db_column=b'Password')),
                ('etat', models.CharField(max_length=250, db_column=b'Etat')),
                ('gestionaire_etape', models.CharField(max_length=6, db_column=b'GestModif')),
                ('psycho', models.BooleanField(default=False, db_column=b'Psycho')),
                ('gestionaire_equiv', models.CharField(max_length=6, null=True, db_column=b'GestEquiv')),
                ('gestionaire_bourse', models.CharField(max_length=6, db_column=b'GestBourse')),
            ],
            options={
                'db_table': 'ied_etudiant',
            },
            bases=(models.Model,),
        ),
    ]

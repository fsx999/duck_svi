# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # # Adding model 'WishSvi'
        db.create_table('ied_etudiant', (
            ('code_dossier', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True, db_column='NumDossier')),
            ('password', self.gf('django.db.models.fields.CharField')(default='1234', max_length=10, db_column='Password')),
            ('etat', self.gf('django.db.models.fields.CharField')(max_length=250, db_column='Etat')),
            ('gestionaire_etape', self.gf('django.db.models.fields.CharField')(max_length=6, db_column='GestModif')),
            ('psycho', self.gf('django.db.models.fields.BooleanField')(db_column='Psycho')),
            ('gestionaire_equiv', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, db_column='GestEquiv')),
            ('gestionaire_bourse', self.gf('django.db.models.fields.CharField')(max_length=6, db_column='GestBourse')),
        ))
        db.send_create_signal(u'duck_svi', ['WishSvi'])

        # Adding model 'GestToEtape'
        db.create_table(u'duck_svi_gesttoetape', (
            ('code_gestionaire', self.gf('django.db.models.fields.CharField')(max_length=6, primary_key=True)),
            ('etape', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.Etape'])),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'duck_svi', ['GestToEtape'])


    def backwards(self, orm):
        # Deleting model 'WishSvi'
        db.delete_table('ied_etudiant')

        # Deleting model 'GestToEtape'
        db.delete_table(u'duck_svi_gesttoetape')


    models = {
        u'django_apogee.etape': {
            'Meta': {'object_name': 'Etape', 'db_table': "u'ETAPE'"},
            'cod_cur': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CUR'"}),
            'cod_cyc': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CYC'"}),
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'COD_ETP'"}),
            'lib_etp': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'db_column': "u'LIB_ETP'"})
        },
        u'duck_svi.gesttoetape': {
            'Meta': {'object_name': 'GestToEtape'},
            'code_gestionaire': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True'}),
            'etape': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.Etape']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        },
        u'duck_svi.wishsvi': {
            'Meta': {'object_name': 'WishSvi', 'db_table': "'ied_etudiant'"},
            'code_dossier': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True', 'db_column': "'NumDossier'"}),
            'etat': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_column': "'Etat'"}),
            'gestionaire_bourse': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_column': "'GestBourse'"}),
            'gestionaire_equiv': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'db_column': "'GestEquiv'"}),
            'gestionaire_etape': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_column': "'GestModif'"}),
            'password': ('django.db.models.fields.CharField', [], {'default': "'1234'", 'max_length': '10', 'db_column': "'Password'"}),
            'psycho': ('django.db.models.fields.BooleanField', [], {'db_column': "'Psycho'"})
        }
    }

    complete_apps = ['duck_svi']
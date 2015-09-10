# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table('firstclass_message', (
            ('key', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('data', self.gf('django.db.models.fields.TextField')(default='{}')),
        ))
        db.send_create_signal('firstclass', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table('firstclass_message')


    models = {
        'firstclass.message': {
            'Meta': {'object_name': 'Message'},
            'data': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'})
        }
    }

    complete_apps = ['firstclass']
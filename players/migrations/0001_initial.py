# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table('players_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('stick', self.gf('django.db.models.fields.CharField')(default='RT', max_length=2)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cv', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cv_image', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(blank=True, related_name='cv_image', null=True, to=orm['medialibrary.MediaFile'])),
            ('speed', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('agility', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('shoot', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('puck_control', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('roster_image', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(blank=True, related_name='roster_image', null=True, to=orm['medialibrary.MediaFile'])),
        ))
        db.send_create_signal('players', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table('players_player')


    models = {
        'medialibrary.category': {
            'Meta': {'ordering': "['parent__title', 'title']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['medialibrary.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medialibrary.mediafile': {
            'Meta': {'ordering': "['-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'players.player': {
            'Meta': {'object_name': 'Player'},
            'agility': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'cv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cv_image': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'blank': 'True', 'related_name': "'cv_image'", 'null': 'True', 'to': "orm['medialibrary.MediaFile']"}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'puck_control': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'roster_image': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'blank': 'True', 'related_name': "'roster_image'", 'null': 'True', 'to': "orm['medialibrary.MediaFile']"}),
            'shoot': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'stick': ('django.db.models.fields.CharField', [], {'default': "'RT'", 'max_length': '2'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['players']
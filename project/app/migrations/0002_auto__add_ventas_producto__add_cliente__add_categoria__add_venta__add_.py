# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ventas_producto'
        db.create_table(u'app_ventas_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('folio_venta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Venta'])),
            ('nombre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Producto'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Ventas_producto'])

        # Adding model 'Cliente'
        db.create_table(u'app_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave_cl', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nombre_cl', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('appaterno_cl', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('apmaterno_cl', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('rfc_prov', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('direccion_prov', self.gf('django.db.models.fields.TextField')()),
            ('telefono_prov', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email_prov', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Cliente'])

        # Adding model 'Categoria'
        db.create_table(u'app_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Categoria'])

        # Adding model 'Venta'
        db.create_table(u'app_venta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('folio_venta', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('clave_cl', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Cliente'])),
            ('subtotal_venta', self.gf('django.db.models.fields.FloatField')()),
            ('iva', self.gf('django.db.models.fields.FloatField')()),
            ('total_venta', self.gf('django.db.models.fields.FloatField')()),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Venta'])

        # Adding model 'Receta'
        db.create_table(u'app_receta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Producto'])),
            ('unidad_de_medida', self.gf('django.db.models.fields.CharField')(default='kilogramo', max_length=2)),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app', ['Receta'])

        # Adding M2M table for field clave_mat on 'Receta'
        m2m_table_name = db.shorten_name(u'app_receta_clave_mat')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('receta', models.ForeignKey(orm[u'app.receta'], null=False)),
            ('materia_prima', models.ForeignKey(orm[u'app.materia_prima'], null=False))
        ))
        db.create_unique(m2m_table_name, ['receta_id', 'materia_prima_id'])

        # Adding model 'Materia_Prima'
        db.create_table(u'app_materia_prima', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave_mat', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion_mat', self.gf('django.db.models.fields.TextField')()),
            ('costo1', self.gf('django.db.models.fields.FloatField')()),
            ('clave_prov', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Proveedor'])),
            ('clave_up', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Unidad_de_presentacion'])),
        ))
        db.send_create_signal(u'app', ['Materia_Prima'])

        # Adding model 'Proveedor'
        db.create_table(u'app_proveedor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave_prov', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('razonsocial_prov', self.gf('django.db.models.fields.TextField')()),
            ('rfc_prov', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('direccion_prov', self.gf('django.db.models.fields.TextField')()),
            ('telefono_prov', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email_prov', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Proveedor'])

        # Adding model 'Producto'
        db.create_table(u'app_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Categoria'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Producto'])

        # Adding model 'Unidad_de_presentacion'
        db.create_table(u'app_unidad_de_presentacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave_up', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion_up', self.gf('django.db.models.fields.TextField')()),
            ('cantidad_up', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('presentacion_up', self.gf('django.db.models.fields.CharField')(default='kilogramo', max_length=2)),
        ))
        db.send_create_signal(u'app', ['Unidad_de_presentacion'])


    def backwards(self, orm):
        # Deleting model 'Ventas_producto'
        db.delete_table(u'app_ventas_producto')

        # Deleting model 'Cliente'
        db.delete_table(u'app_cliente')

        # Deleting model 'Categoria'
        db.delete_table(u'app_categoria')

        # Deleting model 'Venta'
        db.delete_table(u'app_venta')

        # Deleting model 'Receta'
        db.delete_table(u'app_receta')

        # Removing M2M table for field clave_mat on 'Receta'
        db.delete_table(db.shorten_name(u'app_receta_clave_mat'))

        # Deleting model 'Materia_Prima'
        db.delete_table(u'app_materia_prima')

        # Deleting model 'Proveedor'
        db.delete_table(u'app_proveedor')

        # Deleting model 'Producto'
        db.delete_table(u'app_producto')

        # Deleting model 'Unidad_de_presentacion'
        db.delete_table(u'app_unidad_de_presentacion')


    models = {
        u'app.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apmaterno_cl': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'appaterno_cl': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'clave_cl': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion_prov': ('django.db.models.fields.TextField', [], {}),
            'email_prov': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_cl': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rfc_prov': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'telefono_prov': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app.materia_prima': {
            'Meta': {'object_name': 'Materia_Prima'},
            'clave_mat': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'clave_prov': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Proveedor']"}),
            'clave_up': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Unidad_de_presentacion']"}),
            'costo1': ('django.db.models.fields.FloatField', [], {}),
            'descripcion_mat': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.producto': {
            'Meta': {'object_name': 'Producto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Categoria']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'clave_prov': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion_prov': ('django.db.models.fields.TextField', [], {}),
            'email_prov': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'razonsocial_prov': ('django.db.models.fields.TextField', [], {}),
            'rfc_prov': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'telefono_prov': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app.receta': {
            'Meta': {'object_name': 'Receta'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'clave_mat': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['app.Materia_Prima']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Producto']"}),
            'unidad_de_medida': ('django.db.models.fields.CharField', [], {'default': "'kilogramo'", 'max_length': '2'})
        },
        u'app.unidad_de_presentacion': {
            'Meta': {'object_name': 'Unidad_de_presentacion'},
            'cantidad_up': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'clave_up': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'descripcion_up': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presentacion_up': ('django.db.models.fields.CharField', [], {'default': "'kilogramo'", 'max_length': '2'})
        },
        u'app.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'administrador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'perfil': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'usuario': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35', 'db_index': 'True'})
        },
        u'app.venta': {
            'Meta': {'object_name': 'Venta'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'clave_cl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Cliente']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'folio_venta': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.FloatField', [], {}),
            'subtotal_venta': ('django.db.models.fields.FloatField', [], {}),
            'total_venta': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.ventas_producto': {
            'Meta': {'object_name': 'Ventas_producto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'folio_venta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Venta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Producto']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']
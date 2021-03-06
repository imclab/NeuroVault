# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Collection'
        db.create_table(u'statmaps_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('DOI', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, unique=True, null=True, blank=True)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('add_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('type_of_design', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('number_of_imaging_runs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('number_of_experimental_units', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('length_of_runs', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('length_of_blocks', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('length_of_trials', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('optimization', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('optimization_method', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('number_of_subjects', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('subject_age_mean', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('subject_age_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('subject_age_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('handedness', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('proportion_male_subjects', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('inclusion_exclusion_criteria', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('number_of_rejected_subjects', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('group_comparison', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('group_description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('scanner_make', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('scanner_model', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('field_strength', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pulse_sequence', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('parallel_imaging', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('field_of_view', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('matrix_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slice_thickness', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('skip_factor', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('acquisition_orientation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('order_of_acquisition', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('repetition_time', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('echo_time', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('flip_angle', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('software_package', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('software_version', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('order_of_preprocessing_operations', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('quality_control', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('used_b0_unwarping', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('b0_unwarping_software', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('used_slice_timing_correction', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('slice_timing_correction_software', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('used_motion_correction', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('motion_correction_software', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('motion_correction_reference', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('motion_correction_metric', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('motion_correction_interpolation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('used_motion_susceptibiity_correction', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('used_intersubject_registration', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('intersubject_registration_software', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('intersubject_transformation_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('nonlinear_transform_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('transform_similarity_metric', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('interpolation_method', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('object_image_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('functional_coregistered_to_structural', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('functional_coregistration_method', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('coordinate_space', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('target_template_image', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('target_resolution', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('used_smoothing', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('smoothing_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('smoothing_fwhm', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('resampled_voxel_size', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('intrasubject_model_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('intrasubject_estimation_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('intrasubject_modeling_software', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('hemodynamic_response_function', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('used_temporal_derivatives', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('used_dispersion_derivatives', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('used_motion_regressors', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('used_reaction_time_regressor', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('used_orthogonalization', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('orthogonalization_description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('used_high_pass_filter', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('high_pass_filter_method', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('autocorrelation_model', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('group_model_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('group_estimation_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('group_modeling_software', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('group_inference_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('group_model_multilevel', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('group_repeated_measures', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('group_repeated_measures_method', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'statmaps', ['Collection'])

        # Adding model 'KeyValueTag'
        db.create_table(u'statmaps_keyvaluetag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'statmaps', ['KeyValueTag'])

        # Adding model 'ValueTaggedItem'
        db.create_table(u'statmaps_valuetaggeditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'statmaps_valuetaggeditem_tagged_items', to=orm['contenttypes.ContentType'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tagged_items', to=orm['statmaps.KeyValueTag'])),
        ))
        db.send_create_signal(u'statmaps', ['ValueTaggedItem'])

        # Adding model 'Image'
        db.create_table(u'statmaps_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statmaps.Collection'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('hdr_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('json_path', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('add_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('map_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('statistic_parameters', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('smoothness_fwhm', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('contrast_definition', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('contrast_definition_cogatlas', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'statmaps', ['Image'])

        # Adding unique constraint on 'Image', fields ['collection', 'name']
        db.create_unique(u'statmaps_image', ['collection_id', 'name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Image', fields ['collection', 'name']
        db.delete_unique(u'statmaps_image', ['collection_id', 'name'])

        # Deleting model 'Collection'
        db.delete_table(u'statmaps_collection')

        # Deleting model 'KeyValueTag'
        db.delete_table(u'statmaps_keyvaluetag')

        # Deleting model 'ValueTaggedItem'
        db.delete_table(u'statmaps_valuetaggeditem')

        # Deleting model 'Image'
        db.delete_table(u'statmaps_image')


    models = {
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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'statmaps.collection': {
            'DOI': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Collection'},
            'acquisition_orientation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'autocorrelation_model': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'b0_unwarping_software': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'coordinate_space': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'echo_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'field_of_view': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'field_strength': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'flip_angle': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'functional_coregistered_to_structural': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'functional_coregistration_method': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'group_comparison': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'group_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'group_estimation_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'group_inference_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'group_model_multilevel': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'group_model_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'group_modeling_software': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'group_repeated_measures': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'group_repeated_measures_method': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'handedness': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hemodynamic_response_function': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'high_pass_filter_method': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inclusion_exclusion_criteria': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'interpolation_method': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'intersubject_registration_software': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'intersubject_transformation_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'intrasubject_estimation_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'intrasubject_model_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'intrasubject_modeling_software': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'length_of_blocks': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_of_runs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_of_trials': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'matrix_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'motion_correction_interpolation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'motion_correction_metric': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'motion_correction_reference': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'motion_correction_software': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'nonlinear_transform_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'number_of_experimental_units': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_imaging_runs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_rejected_subjects': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_subjects': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'object_image_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'optimization': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'optimization_method': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'order_of_acquisition': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'order_of_preprocessing_operations': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'orthogonalization_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'parallel_imaging': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'proportion_male_subjects': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pulse_sequence': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'quality_control': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'repetition_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'resampled_voxel_size': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'scanner_make': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'scanner_model': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'skip_factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slice_thickness': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slice_timing_correction_software': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'smoothing_fwhm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smoothing_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'software_package': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'software_version': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'subject_age_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'subject_age_mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'subject_age_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'target_resolution': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'target_template_image': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'transform_similarity_metric': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'type_of_design': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'used_b0_unwarping': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_dispersion_derivatives': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_high_pass_filter': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_intersubject_registration': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_motion_correction': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_motion_regressors': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_motion_susceptibiity_correction': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_orthogonalization': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_reaction_time_regressor': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_slice_timing_correction': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_smoothing': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'used_temporal_derivatives': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'statmaps.image': {
            'Meta': {'unique_together': "(('collection', 'name'),)", 'object_name': 'Image'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['statmaps.Collection']"}),
            'contrast_definition': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contrast_definition_cogatlas': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'hdr_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json_path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'map_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'smoothness_fwhm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'statistic_parameters': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'statmaps.keyvaluetag': {
            'Meta': {'object_name': 'KeyValueTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'statmaps.valuetaggeditem': {
            'Meta': {'object_name': 'ValueTaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'statmaps_valuetaggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tagged_items'", 'to': u"orm['statmaps.KeyValueTag']"})
        }
    }

    complete_apps = ['statmaps']
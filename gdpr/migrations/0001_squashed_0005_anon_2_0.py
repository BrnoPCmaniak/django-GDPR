# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-27 10:11
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.db import migrations, models
from django.utils.timezone import utc


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# gdpr.migrations.0003

class Migration(migrations.Migration):
    replaces = [('gdpr', '0001_initial'), ('gdpr', '0002_auto_20180509_1518'), ('gdpr', '0003'), ('gdpr', '0004'),
                ('gdpr', '0005_anon_2_0')]

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymizedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('field', models.CharField(max_length=250, verbose_name='anonymized field name')),
                ('object_id', models.TextField(verbose_name='related object ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('content_type',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType',
                                   verbose_name='related object content type')),
            ],
            options={
                'verbose_name': 'anonymized data',
                'verbose_name_plural': 'anonymized data',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='LegalReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('expires_at', models.DateTimeField(db_index=True, verbose_name='expires at')),
                ('tag', models.CharField(blank=True, max_length=100, null=True, verbose_name='tag')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('purpose_slug', models.CharField(max_length=100, verbose_name='purpose')),
                ('source_object_id', models.TextField(verbose_name='source object ID')),
                ('source_object_content_type',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType',
                                   verbose_name='source object content type')),
            ],
            options={
                'verbose_name': 'legal reason',
                'verbose_name_plural': 'legal reasons',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='LegalReasonRelatedObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('object_id', models.TextField(db_index=True, verbose_name='related object ID')),
                ('object_content_type',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType',
                                   verbose_name='related object content type')),
                ('legal_reason',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_objects',
                                   to='gdpr.LegalReason', verbose_name='legal reason')),
            ],
            options={
                'verbose_name': 'legal reason related object',
                'verbose_name_plural': 'legal reasons related objects',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='anonymizeddata',
            name='expired_reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='gdpr.LegalReason', verbose_name='expired reason'),
        ),
        migrations.AddField(
            model_name='legalreason',
            name='issued_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 9, 13, 18, 7, 317147, tzinfo=utc),
                                       verbose_name='issued at'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='legalreason',
            name='purpose_slug',
            field=models.CharField(max_length=100, verbose_name='purpose'),
        ),
        migrations.AlterField(
            model_name='legalreason',
            name='purpose_slug',
            field=models.CharField(db_index=True, max_length=100, verbose_name='purpose'),
        ),
        migrations.AlterField(
            model_name='legalreason',
            name='source_object_id',
            field=models.TextField(db_index=True, verbose_name='source object ID'),
        ),
        migrations.AlterField(
            model_name='legalreason',
            name='expires_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='expires at'),
        ),
        migrations.AlterUniqueTogether(
            name='legalreason',
            unique_together=set([('purpose_slug', 'source_object_content_type', 'source_object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='legalreasonrelatedobject',
            unique_together=set([('legal_reason', 'object_content_type', 'object_id')]),
        ),
        migrations.AlterField(
            model_name='anonymizeddata',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType',
                                    verbose_name='related object content type'),
        ),
        migrations.AlterField(
            model_name='anonymizeddata',
            name='expired_reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='gdpr.LegalReason', verbose_name='expired reason'),
        ),
        migrations.AlterField(
            model_name='legalreason',
            name='source_object_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType',
                                    verbose_name='source object content type'),
        ),
        migrations.AlterField(
            model_name='legalreason',
            name='source_object_id',
            field=models.TextField(verbose_name='source object ID'),
        ),
        migrations.AlterField(
            model_name='legalreasonrelatedobject',
            name='object_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType',
                                    verbose_name='related object content type'),
        ),
        migrations.AlterField(
            model_name='legalreasonrelatedobject',
            name='object_id',
            field=models.TextField(verbose_name='related object ID'),
        ),
        migrations.AlterUniqueTogether(
            name='anonymizeddata',
            unique_together=set([('content_type', 'object_id', 'field')]),
        ),
        migrations.AlterUniqueTogether(
            name='legalreason',
            unique_together=set([('purpose_slug', 'source_object_content_type', 'source_object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='legalreasonrelatedobject',
            unique_together=set([('legal_reason', 'object_content_type', 'object_id')]),
        ),
    ]

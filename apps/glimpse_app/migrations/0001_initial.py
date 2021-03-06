# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-21 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_key_name', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=45)),
                ('email_address', models.CharField(max_length=45)),
                ('phone_number', models.CharField(max_length=45)),
                ('device_key_name', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to='glimpse_app.User'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='glimpse_app.User'),
        ),
    ]

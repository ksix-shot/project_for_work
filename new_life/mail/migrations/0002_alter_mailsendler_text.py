# Generated by Django 3.2.5 on 2021-07-18 15:30

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailsendler',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]
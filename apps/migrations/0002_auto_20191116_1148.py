# Generated by Django 2.2.6 on 2019-11-16 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='projevt_image',
            new_name='project_image',
        ),
    ]

# Generated by Django 5.0 on 2024-01-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0041_remove_reporttemplate_path_alter_reporttemplate_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisory',
            name='is_draft',
        ),
        migrations.AddField(
            model_name='advisory',
            name='visibility',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Private'), (2, 'Team')], default=1),
        ),
        migrations.AddField(
            model_name='advisory',
            name='vulnerability_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Unfixed'), (2, 'Fixed'), (3, "Won't Fix")], default=1),
        ),
        migrations.AlterField(
            model_name='advisory',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Not disclosed'), (2, 'Disclosed')], default=2),
        ),
    ]
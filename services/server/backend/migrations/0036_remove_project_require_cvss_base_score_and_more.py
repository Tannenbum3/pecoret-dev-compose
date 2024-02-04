# Generated by Django 4.2.6 on 2023-11-19 14:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0035_vulnerabilitytemplatetranslation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='require_cvss_base_score',
        ),
        migrations.RemoveField(
            model_name='project',
            name='require_owasp_risk_rating',
        ),
        migrations.AddField(
            model_name='finding',
            name='cvss_score_40',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(regex='CVSS:4\\.0\\/AV:[N|A|L|P]\\/AC:[L|H]\\/AT:[N|P]\\/PR:[N|L|H]\\/UI:[N|P|A]\\/VC:[H|L|N]\\/VI:[H|L|N]\\/VA:[H|L|N]\\/SC:[H|L|N]\\/SI:[H|L|N]\\/SA:[H|L|N]')]),
        ),
        migrations.AddField(
            model_name='project',
            name='require_cvss_score',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'CVSS 4.0 Base'), (1, 'CVSS 3.1 Base')], null=True),
        ),
        migrations.DeleteModel(
            name='OWASPRiskRating',
        ),
    ]

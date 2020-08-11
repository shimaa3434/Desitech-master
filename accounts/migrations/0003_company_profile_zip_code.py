# Generated by Django 3.0.9 on 2020-08-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_company_profile_job_seeker_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_profile',
            name='zip_code',
            field=models.CharField(default=1, max_length=12, verbose_name='ZIP / Postal code'),
            preserve_default=False,
        ),
    ]

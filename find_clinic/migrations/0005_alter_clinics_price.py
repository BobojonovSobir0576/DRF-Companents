# Generated by Django 4.2.7 on 2023-11-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_clinic', '0004_alter_clinics_id_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinics',
            name='price',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-27 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('find_clinic', '0002_clinics_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinics',
            name='id_categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='find_clinic.cliniccategoriyes'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-27 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='fitness-categories/')),
            ],
        ),
        migrations.CreateModel(
            name='FitnessAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessCreateReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(blank=True, max_length=255, null=True)),
                ('secondstamp', models.IntegerField(blank=True, default=30, null=True)),
                ('fitness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.fitness')),
                ('user', models.ManyToManyField(blank=True, null=True, related_name='reservation_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('fitness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.fitnesscreatereservation')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessMultipleImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='fitness-categories/')),
                ('fitness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.fitness')),
            ],
        ),
        migrations.AddField(
            model_name='fitness',
            name='amenities',
            field=models.ManyToManyField(blank=True, null=True, to='fitness.fitnessamenities'),
        ),
        migrations.AddField(
            model_name='fitness',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='fitness.fitnesscategories'),
        ),
        migrations.AddField(
            model_name='fitness',
            name='teacher',
            field=models.ManyToManyField(blank=True, null=True, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fitness',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]

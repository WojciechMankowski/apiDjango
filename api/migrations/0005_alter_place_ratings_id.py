# Generated by Django 5.0.3 on 2024-03-24 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_rating_place_place_ratings_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='ratings_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='api.rating'),
        ),
    ]

# Generated by Django 4.0.6 on 2024-03-13 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0025_tourbookingname_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourItinerary',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('itinerary', models.TextField(max_length=2000)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
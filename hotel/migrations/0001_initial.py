# Generated by Django 4.0.6 on 2024-02-15 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_rename_places_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hotelname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('map_link', models.URLField()),
                ('total_room', models.IntegerField()),
                ('price', models.IntegerField()),
                ('rating', models.FloatField(default=0, null=True)),
                ('facility', models.CharField(max_length=100)),
                ('hotel_image', models.ImageField(upload_to='image/hotel/')),
                ('room_image', models.ImageField(upload_to='image/hotel/')),
                ('image_3', models.ImageField(upload_to='image/hotel/')),
                ('image_4', models.ImageField(upload_to='image/hotel/')),
                ('image_5', models.ImageField(upload_to='image/hotel/')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.place')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
# Generated by Django 5.0.3 on 2024-05-28 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('numberOfSongs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Track', models.CharField(max_length=100)),
                ('Artist', models.CharField(max_length=100)),
                ('Album', models.CharField(max_length=100)),
                ('Length', models.CharField(max_length=100)),
                ('playlist', models.ManyToManyField(to='zing.playlist')),
            ],
        ),
    ]
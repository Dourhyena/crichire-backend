# Generated by Django 3.1.4 on 2021-01-04 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach_type', models.CharField(choices=[('BAT', 'batting'), ('BOWL', 'bowling'), ('FIELD', 'fielding'), ('FIT', 'fitness')], max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('is_available', models.BooleanField()),
                ('dob', models.DateField()),
                ('experience', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_type', models.CharField(choices=[('BAT', 'batting'), ('BOWL', 'bowling'), ('FIELD', 'fielding'), ('FIT', 'fitness')], max_length=10)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('date', models.DateField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaches.coach')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.player')),
            ],
        ),
    ]
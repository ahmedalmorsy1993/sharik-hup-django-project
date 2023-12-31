# Generated by Django 4.2.2 on 2023-06-24 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='countries.country')),
            ],
        ),
        migrations.CreateModel(
            name='StateTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(max_length=2)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.state')),
            ],
        ),
    ]

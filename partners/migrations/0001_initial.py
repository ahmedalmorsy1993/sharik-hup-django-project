# Generated by Django 4.2.2 on 2023-06-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/partners')),
                ('is_active', models.BooleanField(default=True)),
                ('alt_image', models.CharField(max_length=255)),
            ],
        ),
    ]

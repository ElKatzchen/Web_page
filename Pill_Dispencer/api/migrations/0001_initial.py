# Generated by Django 4.2.20 on 2025-03-29 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Age', models.PositiveIntegerField()),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]

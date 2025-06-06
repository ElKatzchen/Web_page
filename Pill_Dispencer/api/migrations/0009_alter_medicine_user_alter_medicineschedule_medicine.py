# Generated by Django 4.2.20 on 2025-04-20 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_user_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Medicines', to='api.user'),
        ),
        migrations.AlterField(
            model_name='medicineschedule',
            name='Medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Schedules', to='api.medicine'),
        ),
    ]

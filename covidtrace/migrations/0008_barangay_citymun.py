# Generated by Django 3.1.1 on 2020-10-05 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidtrace', '0007_auto_20201005_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='barangay',
            name='citymun',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='covidtrace.citymun'),
            preserve_default=False,
        ),
    ]

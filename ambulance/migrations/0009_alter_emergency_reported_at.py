# Generated by Django 3.2.18 on 2023-03-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance', '0008_alter_emergency_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergency',
            name='reported_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

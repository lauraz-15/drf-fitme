# Generated by Django 3.2.15 on 2022-08-10 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_goal_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='current_weight',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]

# Generated by Django 3.2.15 on 2022-08-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_current_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='current_weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='goal_weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

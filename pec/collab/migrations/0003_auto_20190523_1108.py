# Generated by Django 2.2.1 on 2019-05-23 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0002_carpenter_maid_plumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='address',
            new_name='about',
        ),
        migrations.RemoveField(
            model_name='server',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='server',
            name='name',
        ),
        migrations.AlterField(
            model_name='server',
            name='profession',
            field=models.CharField(max_length=100),
        ),
    ]
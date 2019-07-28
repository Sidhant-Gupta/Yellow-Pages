# Generated by Django 2.2.1 on 2019-05-22 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('profession', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=12)),
                ('address', models.TextField()),
            ],
        ),
    ]
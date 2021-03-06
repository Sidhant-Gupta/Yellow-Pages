# Generated by Django 2.2.1 on 2019-06-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0008_auto_20190529_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('contact', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('dist', models.FloatField(blank=True, null=True)),
            ],
            options={
                'ordering': ['dist'],
            },
        ),
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('contact', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('dist', models.FloatField(blank=True, null=True)),
            ],
            options={
                'ordering': ['dist'],
            },
        ),
        migrations.CreateModel(
            name='Electrician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('contact', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('dist', models.FloatField(blank=True, null=True)),
            ],
            options={
                'ordering': ['dist'],
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('contact', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('dist', models.FloatField(blank=True, null=True)),
            ],
            options={
                'ordering': ['dist'],
            },
        ),
    ]

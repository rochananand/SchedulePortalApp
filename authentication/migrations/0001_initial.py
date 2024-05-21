# Generated by Django 4.2.11 on 2024-04-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElaClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=50)),
                ('mMembers', models.IntegerField()),
                ('maxMembers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MathClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=50)),
                ('mMembers', models.IntegerField()),
                ('maxMembers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ScienceClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=50)),
                ('mMembers', models.IntegerField()),
                ('maxMembers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=50)),
                ('mMembers', models.IntegerField()),
                ('maxMembers', models.IntegerField()),
            ],
        ),
    ]
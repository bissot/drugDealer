# Generated by Django 3.1.4 on 2020-12-27 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30)),
                ('role', models.IntegerField(choices=[(1, 'Druggie'), (2, 'Drugdealer'), (3, 'Cop')])),
                ('isArrested', models.BooleanField(default=False)),
            ],
        ),
    ]

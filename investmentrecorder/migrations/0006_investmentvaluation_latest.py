# Generated by Django 2.1.1 on 2018-09-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investmentrecorder', '0005_auto_20180905_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentvaluation',
            name='latest',
            field=models.CharField(default='y', max_length=1),
        ),
    ]

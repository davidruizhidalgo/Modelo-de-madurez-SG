# Generated by Django 2.1.2 on 2018-10-18 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20181017_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question1_act',
            field=models.CharField(choices=[('', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question1_p1',
            field=models.CharField(choices=[('', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question1_p2',
            field=models.CharField(choices=[('', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
    ]

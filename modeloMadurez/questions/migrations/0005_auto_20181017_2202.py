# Generated by Django 2.1.2 on 2018-10-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20181017_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question1_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question1_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question1_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
    ]

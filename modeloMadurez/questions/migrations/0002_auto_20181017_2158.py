# Generated by Django 2.1.2 on 2018-10-18 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question1',
        ),
        migrations.AddField(
            model_name='question',
            name='question1_act',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='question1_p1',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='question1_p2',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
    ]

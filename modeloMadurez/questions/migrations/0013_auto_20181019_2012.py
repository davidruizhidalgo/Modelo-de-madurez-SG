# Generated by Django 2.1.2 on 2018-10-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_auto_20181019_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionary',
            old_name='q_11_act',
            new_name='smr_11_act',
        ),
        migrations.RenameField(
            model_name='questionary',
            old_name='q_11_p1',
            new_name='smr_11_p1',
        ),
        migrations.RenameField(
            model_name='questionary',
            old_name='q_11_p2',
            new_name='smr_11_p2',
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_12_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_12_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_12_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_13_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_13_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_13_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='', max_length=100),
        ),
    ]

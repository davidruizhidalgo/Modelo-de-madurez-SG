# Generated by Django 2.1.2 on 2018-10-20 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_auto_20181018_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionary',
            old_name='question1_act',
            new_name='q_11_act',
        ),
        migrations.RenameField(
            model_name='questionary',
            old_name='question1_p1',
            new_name='q_11_p1',
        ),
        migrations.RenameField(
            model_name='questionary',
            old_name='question1_p2',
            new_name='q_11_p2',
        ),
    ]

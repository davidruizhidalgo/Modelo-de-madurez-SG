# Generated by Django 2.1.2 on 2018-10-21 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_auto_20181019_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionary',
            name='os_11_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_11_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_11_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_12_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_12_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_12_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_13_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_13_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_13_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_21_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_21_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_21_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_22_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_22_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_22_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_23_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_23_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_23_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_24_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_24_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_24_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_25_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_25_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_25_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_31_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_31_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_31_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_32_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_32_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_32_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_33_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_33_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_33_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_34_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_34_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_34_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_35_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_35_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_35_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_36_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_36_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_36_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_41_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_41_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_41_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_42_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_42_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_42_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_43_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_43_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_43_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_51_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_51_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_51_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_52_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_52_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_52_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_53_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_53_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='os_53_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
    ]

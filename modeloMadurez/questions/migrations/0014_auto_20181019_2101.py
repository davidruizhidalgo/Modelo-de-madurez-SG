# Generated by Django 2.1.2 on 2018-10-20 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_auto_20181019_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionary',
            old_name='smr_11_act',
            new_name='srm_11_act',
        ),
        migrations.RenameField(
            model_name='questionary',
            old_name='smr_11_p1',
            new_name='srm_11_p1',
        ),
        migrations.RenameField(
            model_name='questionary',
            old_name='smr_11_p2',
            new_name='srm_11_p2',
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_21_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_21_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_21_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_22_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_22_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_22_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_23_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_23_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_23_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_24_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_24_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_24_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_25_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_25_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_25_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_26_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_26_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_26_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_31_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_31_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_31_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_32_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_32_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_32_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_33_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_33_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_33_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_34_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_34_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_34_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_41_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_41_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_41_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_42_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_42_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_42_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_43_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_43_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_43_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_51_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_51_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_51_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_52_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_52_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_52_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_53_act',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_53_p1',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='questionary',
            name='srm_53_p2',
            field=models.CharField(choices=[('0', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=100),
        ),
    ]

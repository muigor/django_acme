# Generated by Django 3.0 on 2023-02-23 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20230111_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseignant',
            name='prenom',
        ),
        migrations.AddField(
            model_name='ue',
            name='codeUE',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='exercice',
            name='regles',
            field=models.ManyToManyField(blank=True, to='api.Regle'),
        ),
        migrations.AlterField(
            model_name='exercice',
            name='ue',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.UE'),
        ),
        migrations.AlterField(
            model_name='regle',
            name='exercices',
            field=models.ManyToManyField(blank=True, to='api.Exercice'),
        ),
    ]

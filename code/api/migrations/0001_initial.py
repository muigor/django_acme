# Generated by Django 3.0 on 2023-01-06 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('adresse_mail', models.EmailField(max_length=254)),
                ('mot_de_passe', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UE',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enseignants', models.ManyToManyField(to='api.Enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Regle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('exercices', models.ManyToManyField(to='api.Exercice')),
            ],
        ),
        migrations.AddField(
            model_name='exercice',
            name='regles',
            field=models.ManyToManyField(to='api.Regle'),
        ),
        migrations.AddField(
            model_name='exercice',
            name='ue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UE'),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='ues',
            field=models.ManyToManyField(to='api.UE'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-05 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_expert', models.CharField(max_length=255, verbose_name="Nom de l'expert")),
                ('email', models.EmailField(max_length=254)),
                ('fonction', models.CharField(max_length=255, verbose_name='Fonction')),
                ('connected_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.TextField(verbose_name='Libellé de la question')),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_expert', to='forum.expert')),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.TextField(verbose_name='Libellé de la réponse')),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reponse_expert', to='forum.expert')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reponse_question', to='forum.question')),
            ],
        ),
    ]

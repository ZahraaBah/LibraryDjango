# Generated by Django 4.2.7 on 2024-03-11 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('ID_commune', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom_commune', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'commune',
            },
        ),
        migrations.CreateModel(
            name='Formilair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'Formilair',
            },
        ),
        migrations.CreateModel(
            name='Moughata',
            fields=[
                ('ID_maghataa', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom_maghataa', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'moughata',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('choices', models.TextField()),
                 ('categorie', models.TextField()),
                ('type', models.CharField(choices=[('text', 'Text'), ('choice', 'Choice')], max_length=10)),
                ('formilair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='myapp.formilair')),
            ],
            options={
                'db_table': 'Question',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.IntegerField()),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('ID_wilaya', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom_wilaya', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Wilaya',
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('NumeroVillage', models.IntegerField(primary_key=True, serialize=False)),
                ('NomAdministratifVillage', models.CharField(max_length=150)),
                ('NomLocal', models.CharField(max_length=150)),
                ('DistanceChefLieu', models.FloatField()),
                ('DistanceAxesPrincipaux', models.FloatField()),
                ('DateCreation', models.DateField()),
                ('CompositionEthnique', models.TextField()),
                ('AutresInfosVillage', models.TextField()),
                ('ID_Commune', models.ForeignKey(db_column='ID_commune', max_length=100, on_delete=django.db.models.deletion.CASCADE, to='myapp.commune')),
                ('ID_Moughata', models.ForeignKey(db_column='ID_Moughata', max_length=100, on_delete=django.db.models.deletion.CASCADE, to='myapp.moughata')),
            ],
            options={
                'db_table': 'village',
            },
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_reponse', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reponses', to='myapp.question')),
            ],
            options={
                'db_table': 'Reponse',
            },
        ),
        migrations.AddField(
            model_name='moughata',
            name='ID_wilaya',
            field=models.ForeignKey(db_column='ID_wilaya', on_delete=django.db.models.deletion.CASCADE, to='myapp.wilaya'),
        ),
        migrations.CreateModel(
            name='InfrastructuresVillage',
            fields=[
                ('ID_Infrastructures', models.IntegerField(primary_key=True, serialize=False)),
                ('TypeInfrastructure', models.CharField(max_length=150)),
                ('NombreTotal', models.IntegerField()),
                ('NombreFonctionnelles', models.IntegerField()),
                ('NombreNonFonctionnelles', models.IntegerField()),
                ('NumeroVillage', models.ForeignKey(db_column='NumeroVillage', on_delete=django.db.models.deletion.CASCADE, to='myapp.village')),
            ],
            options={
                'db_table': 'infrastructuresvillage',
            },
        ),
        migrations.CreateModel(
            name='EstimationRessources',
            fields=[
                ('ID_EstimationRessources', models.IntegerField(primary_key=True, serialize=False)),
                ('NombreFamillesEstime', models.IntegerField()),
                ('PopulationEstimee', models.IntegerField()),
                ('EstimationBetail', models.IntegerField()),
                ('AnneeEstimation', models.IntegerField()),
                ('NumeroVillage', models.ForeignKey(db_column='NumeroVillage', on_delete=django.db.models.deletion.CASCADE, to='myapp.village')),
            ],
            options={
                'db_table': 'estimationressources',
            },
        ),
        migrations.CreateModel(
            name='Demographie',
            fields=[
                ('ID_Demographie', models.IntegerField(primary_key=True, serialize=False)),
                ('PopulationFixe', models.IntegerField()),
                ('NombreMenages', models.IntegerField()),
                ('AutresInfosDemographie', models.TextField()),
                ('NumeroVillage', models.ForeignKey(db_column='NumeroVillage', on_delete=django.db.models.deletion.CASCADE, to='myapp.village')),
            ],
            options={
                'db_table': 'demographie',
            },
        ),
        migrations.CreateModel(
            name='CoordonneesGPS',
            fields=[
                ('ID_CoordonneesGPS', models.IntegerField(primary_key=True, serialize=False)),
                ('Longitude', models.FloatField()),
                ('Latitude', models.FloatField()),
                ('TypeLocalite', models.CharField(max_length=150)),
                ('StructureHabitat', models.CharField(max_length=150)),
                ('ObservationsAccesLocalite', models.TextField()),
                ('NumeroVillage', models.ForeignKey(db_column='NumeroVillage', on_delete=django.db.models.deletion.CASCADE, to='myapp.village')),
            ],
            options={
                'db_table': 'coordonneesgps',
            },
        ),
        migrations.AddField(
            model_name='commune',
            name='ID_maghataa_id',
            field=models.ForeignKey(db_column='ID_maghataa_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.moughata'),
        ),
        migrations.CreateModel(
            name='ActivitesEconomiques',
            fields=[
                ('ID_ActiviteEco', models.IntegerField(primary_key=True, serialize=False)),
                ('TypeActivite', models.CharField(max_length=150)),
                ('AutresDetailsActivite', models.TextField()),
                ('NumeroVillage', models.ForeignKey(db_column='NumeroVillage', on_delete=django.db.models.deletion.CASCADE, to='myapp.village')),
            ],
            options={
                'db_table': 'activiteseconomiques',
            },
        ),
    ]

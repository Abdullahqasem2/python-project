# Generated by Django 3.2.4 on 2021-06-04 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lancer_info',
            fields=[
                ('language', models.CharField(max_length=50)),
                ('education', models.TextField()),
                ('description', models.TextField()),
                ('lancer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='logapp.user')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='education',
        ),
        migrations.RemoveField(
            model_name='user',
            name='language',
        ),
    ]

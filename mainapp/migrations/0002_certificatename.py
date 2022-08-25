# Generated by Django 4.0.6 on 2022-07-24 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('LevelCertificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.certificatelevel')),
            ],
        ),
    ]

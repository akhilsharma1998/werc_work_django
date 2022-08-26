# Generated by Django 4.0.6 on 2022-08-26 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0006_jobtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='currentuser', to=settings.AUTH_USER_MODEL)),
                ('typejob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobtype', to='mainapp.jobtype')),
            ],
        ),
    ]

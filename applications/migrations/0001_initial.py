# Generated by Django 3.1.7 on 2021-04-03 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studyrooms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('studyroomId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to='studyrooms.studyroom')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.1.5 on 2021-04-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thema',
            field=models.CharField(choices=[('n', '공지게시판'), ('f', '자유게시판'), ('q', '질문게시판'), ('i', '정보게시판')], max_length=1),
        ),
    ]

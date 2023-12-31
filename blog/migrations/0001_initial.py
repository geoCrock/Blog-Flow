# Generated by Django 5.0 on 2023-12-24 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

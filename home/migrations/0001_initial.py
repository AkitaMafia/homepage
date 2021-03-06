# Generated by Django 3.1 on 2020-09-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=100, null=True)),
                ('email', models.TextField(max_length=100)),
                ('subject', models.TextField(max_length=300)),
                ('content', models.TextField(max_length=3000)),
            ],
        ),
    ]

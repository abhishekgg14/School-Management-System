# Generated by Django 3.2.25 on 2024-06-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scl_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dept_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
            ],
        ),
    ]

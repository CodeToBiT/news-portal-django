# Generated by Django 4.0.2 on 2022-04-26 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsToday', '0004_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_email', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]

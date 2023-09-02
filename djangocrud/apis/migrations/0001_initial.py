# Generated by Django 4.2.4 on 2023-09-02 15:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=200, unique=True)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField()),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
    ]

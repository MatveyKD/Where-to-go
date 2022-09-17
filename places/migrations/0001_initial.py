# Generated by Django 4.1 on 2022-09-03 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название места')),
                ('description_short', models.TextField(blank=True, null=True, verbose_name='короткое описание места')),
                ('description_long', models.TextField(verbose_name='полное описание места')),
                ('lng', models.FloatField(verbose_name='широта')),
                ('lat', models.FloatField(verbose_name='долгота')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='место картинки')),
            ],
        ),
    ]
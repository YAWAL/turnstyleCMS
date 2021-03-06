# Generated by Django 3.0.3 on 2020-08-01 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('standard', models.CharField(max_length=30)),
                ('coating', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Turnstyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articyl', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
                ('produce_date', models.DateTimeField(verbose_name='manufacturing date')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='turnstyle_storage.Material')),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hero_headshots/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fizz', models.CharField(max_length=200)),
                ('buzz', models.IntegerField()),
                ('fizzbuzz', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'db_table': 'example',
            },
        ),
    ]

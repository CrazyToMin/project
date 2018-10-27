# Generated by Django 2.1.1 on 2018-10-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_mustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'shop',
            },
        ),
    ]
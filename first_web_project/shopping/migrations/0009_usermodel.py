# Generated by Django 2.1.1 on 2018-10-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0008_auto_20181009_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='icons')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]

# Generated by Django 2.1.1 on 2018-10-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=200)),
                ('categoryid', models.CharField(max_length=10)),
                ('brandname', models.CharField(max_length=20)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=10)),
                ('productid1', models.CharField(max_length=10)),
                ('longname1', models.CharField(max_length=50)),
                ('price1', models.CharField(max_length=10)),
                ('marketprice1', models.CharField(max_length=10)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=10)),
                ('productid2', models.CharField(max_length=10)),
                ('longname2', models.CharField(max_length=50)),
                ('price2', models.CharField(max_length=10)),
                ('marketprice2', models.CharField(max_length=10)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=10)),
                ('productid3', models.CharField(max_length=10)),
                ('longname3', models.CharField(max_length=50)),
                ('price3', models.CharField(max_length=10)),
                ('marketprice3', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'mainshow',
            },
        ),
    ]
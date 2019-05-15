# Generated by Django 2.1.7 on 2019-05-15 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0014_auto_20190515_0326'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='serviceresourcesrelation',
            unique_together={('service', 'resource')},
        ),
        migrations.AlterIndexTogether(
            name='serviceresourcesrelation',
            index_together={('service', 'resource')},
        ),
    ]

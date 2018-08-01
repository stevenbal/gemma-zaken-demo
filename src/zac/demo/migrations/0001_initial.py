# Generated by Django 2.0.3 on 2018-07-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_api_key', models.CharField(blank=True, max_length=255, verbose_name='Google API-key')),
                ('zrc_base_url', models.URLField(blank=True, default='http://localhost:8000', verbose_name='ZRC basis URL')),
                ('drc_base_url', models.URLField(blank=True, default='http://localhost:8001', verbose_name='DRC basis URL')),
                ('ztc_base_url', models.URLField(blank=True, default='http://localhost:8002', verbose_name='ZTC basis URL')),
                ('orc_base_url', models.URLField(blank=True, default='http://localhost:8003', verbose_name='ORC basis URL')),
                ('zrc_bronorganisatie', models.CharField(default='517439943', max_length=9)),
                ('ztc_catalogus_uuid', models.CharField(blank=True, max_length=36, verbose_name='Standaard catalogus UUID')),
                ('ztc_mor_zaaktype_uuid', models.CharField(blank=True, max_length=36, verbose_name='Zaaktype "Melding Openbare Ruimte" UUID')),
                ('ztc_mor_statustype_new_uuid', models.CharField(blank=True, max_length=36, verbose_name='Statustype "Nieuw" UUID')),
            ],
            options={
                'verbose_name': 'Configuratie',
            },
        ),
    ]

# Generated by Django 2.2 on 2020-08-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200802_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(default='admin', max_length=20, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.TextField(default='2020-08-02 16:25:35', verbose_name='время'),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.IntegerField(default=0, verbose_name='ссылка'),
        ),
    ]

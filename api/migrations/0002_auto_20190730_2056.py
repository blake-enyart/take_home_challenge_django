# Generated by Django 2.2.3 on 2019-07-30 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olympian',
            name='medal',
            field=models.CharField(blank=True, choices=[('NA', None), ('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold')], max_length=15, null=True),
        ),
    ]

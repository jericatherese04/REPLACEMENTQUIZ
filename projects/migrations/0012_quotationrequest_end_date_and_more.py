# Generated by Django 5.1.2 on 2024-11-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_remove_quotationrequest_material_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationrequest',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quotationrequest',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quotationrequest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
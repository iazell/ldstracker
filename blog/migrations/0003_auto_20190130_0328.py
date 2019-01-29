# Generated by Django 2.0.10 on 2019-01-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='student_level',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_name',
            field=models.CharField(blank=True, default='000', max_length=3, null=True),
        ),
    ]

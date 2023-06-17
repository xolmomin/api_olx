# Generated by Django 4.2.2 on 2023-06-17 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(max_length=255)),
                ('label', models.CharField(blank=True, max_length=55)),
                ('range', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('enum', 'Enum'), ('bool', 'Bool'), ('salary', 'Salary')], max_length=25)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adverts.category')),
            ],
        ),
        migrations.CreateModel(
            name='ParamValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=55)),
                ('label', models.CharField(max_length=55)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adverts.parameter')),
            ],
        ),
    ]
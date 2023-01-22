# Generated by Django 4.1.5 on 2023-01-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.AddField(
            model_name='student',
            name='Email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Graduation_year',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Program_Of_Study',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Select_Degree',
            field=models.CharField(choices=[('MTech', 'MTech'), ('BTech', 'BTech'), ('Ph.D', 'Ph.D')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
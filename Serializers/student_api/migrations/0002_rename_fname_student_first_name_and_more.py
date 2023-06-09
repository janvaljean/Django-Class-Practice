# Generated by Django 4.1.3 on 2023-04-28 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='student',
            name='path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='student_api.path'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_student_book_alter_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='book',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
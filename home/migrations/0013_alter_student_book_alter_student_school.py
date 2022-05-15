# Generated by Django 4.0.4 on 2022-05-14 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_student_book_alter_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.book'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.school'),
        ),
    ]
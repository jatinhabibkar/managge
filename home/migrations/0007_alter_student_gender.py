# Generated by Django 4.0.4 on 2022-05-13 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_student_book_alter_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'not to disclose')], default='N', max_length=1),
        ),
    ]
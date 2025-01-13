# Generated by Django 5.1.1 on 2024-11-25 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_alter_course_image_quizresult"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="avatars/"),
        ),
        migrations.AddField(
            model_name="student",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="courses",
            field=models.ManyToManyField(
                related_name="students_set", to="courses.course"
            ),
        ),
    ]

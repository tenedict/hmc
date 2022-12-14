# Generated by Django 3.2.13 on 2022-10-27 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('otwo', multiselectfield.db.fields.MultiSelectField(choices=[(1, '근지구력'), (2, '심폐지구력'), (3, '근력')], max_length=5)),
                ('workout', models.CharField(max_length=30)),
                ('part', multiselectfield.db.fields.MultiSelectField(choices=[(1, '윗가슴'), (2, '스트레칭'), (3, '가슴중앙'), (4, '아랫가슴'), (5, '승모근'), (6, '광배근'), (7, '척추기립근'), (8, '전면삼각근'), (9, '후면삼각근'), (10, '측면삼각근'), (11, '이두근'), (12, '삼두근'), (13, '복근'), (14, '대퇴이두근'), (15, '대퇴사두근'), (16, '비복근')], max_length=38)),
                ('like_users', models.ManyToManyField(related_name='like_articles', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

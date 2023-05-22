# Generated by Django 4.2.1 on 2023-05-15 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ocr_record",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.TextField(blank=True, null=True, verbose_name="检测图片base64"),
                ),
                ("text", models.TextField(null=True, verbose_name="检测文本")),
                (
                    "is_sen",
                    models.CharField(
                        default="否", max_length=20, verbose_name="是否有敏感词汇"
                    ),
                ),
                ("sen_txt", models.TextField(null=True, verbose_name="敏感词汇")),
                (
                    "create_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="生成日期"
                    ),
                ),
                ("update_at", models.DateTimeField(auto_now=True, verbose_name="更新日期")),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_name",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="姓名"
                    ),
                ),
                (
                    "pass_word",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="密码"
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="生成日期"
                    ),
                ),
                ("update_at", models.DateTimeField(auto_now=True, verbose_name="更新日期")),
            ],
        ),
    ]
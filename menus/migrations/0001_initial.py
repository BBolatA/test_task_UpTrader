# Generated by Django 5.2.1 on 2025-05-13 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(db_index=True, max_length=50, unique=True)),
                ("verbose_name", models.CharField(blank=True, max_length=100)),
            ],
            options={
                "verbose_name": "Меню",
                "verbose_name_plural": "Меню",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="MenuItem",
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
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "url",
                    models.CharField(
                        max_length=200, verbose_name="URL или pattern-name"
                    ),
                ),
                (
                    "sort_order",
                    models.PositiveIntegerField(default=0, verbose_name="Порядок"),
                ),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="menus.menu",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="menus.menuitem",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пункт меню",
                "verbose_name_plural": "Пункты меню",
                "ordering": ("sort_order", "id"),
                "unique_together": {("menu", "parent", "title")},
            },
        ),
    ]

from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    verbose_name = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.verbose_name or self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="items")
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    title = models.CharField("Название", max_length=100)
    url = models.CharField(
        "URL или pattern-name", max_length=200,
    )
    sort_order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ("sort_order", "id")
        unique_together = ("menu", "parent", "title")
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.title

    @property
    def resolved_url(self):
        try:
            return reverse(self.url)
        except NoReverseMatch:
            return self.url

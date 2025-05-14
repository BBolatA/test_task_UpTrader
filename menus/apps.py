from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command


class MenusConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "menus"

    def ready(self):
        post_migrate.connect(load_initial_menus, sender=self)


def load_initial_menus(**kwargs):
    from .models import Menu
    if Menu.objects.exists():
        return
    try:
        call_command("loaddata", "initial_menus", verbosity=0)
        print("Все ок")
    except Exception as exc:
        print("Ошибка", exc)

from urllib.parse import urlparse

from django import template
from ..models import Menu, MenuItem
from ..utils import build_tree

register = template.Library()


@register.inclusion_tag("menus/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    current_path = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {"nodes": []}

    items = (
        MenuItem.objects
        .filter(menu=menu)
        .select_related("parent")
        .order_by("parent_id", "sort_order")
    )

    tree = build_tree(items)
    expanded, active_id = _collect_state(items, current_path)

    return {
        "nodes": tree,
        "expanded": expanded,
        "active_id": active_id,
        "current_path": current_path,
    }


def _collect_state(items, path):
    def same_path(url):
        parsed = urlparse(url)
        candidate = parsed.path if parsed.scheme or parsed.netloc else url
        return candidate == path

    matches = [i for i in items if same_path(i.resolved_url)]
    match = matches[-1] if matches else None

    expanded, active_id = set(), None
    while match:
        if active_id is None:
            active_id = match.id
        expanded.add(match.id)
        if match.parent_id:
            expanded.add(match.parent_id)
        match = match.parent
    return expanded, active_id


def _expanded_ids(items, path):
    match = next((i for i in items if i.resolved_url == path), None)
    opened = set()
    while match:
        opened.add(match.id)
        if match.parent_id:
            opened.add(match.parent_id)
        match = match.parent
    return opened

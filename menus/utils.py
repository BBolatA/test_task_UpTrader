def build_tree(items):
    node = {i.id: {"obj": i, "children": []} for i in items}
    roots = []
    for i in node.values():
        if i["obj"].parent_id:
            node[i["obj"].parent_id]["children"].append(i)
        else:
            roots.append(i)
    return roots

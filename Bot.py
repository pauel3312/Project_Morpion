from Morpion import number_to_base


def create_tree():
    list_active = [0]
    dct_layouts_tree = {}
    while len(list_active) > 0:
        new_list_active = []
        for layout in list_active:
            dct_layouts_tree[layout] = get_next_layouts(layout)
            for lyt in get_next_layouts(layout):
                if str(lyt) not in dct_layouts_tree.keys():
                    new_list_active.append(lyt)
        list_active = new_list_active
    return dct_layouts_tree


def get_next_layouts(layout):
    layout = number_to_base(layout)
    turn = get_turn(layout)
    list_next_layouts = []
    for i in range(len(layout)):
        if layout[i] == "0":
            list_next_layouts.append(int(f"{layout[:i]}{turn}{layout[1+i:]}", 3))
    return list_next_layouts


def get_turn(layout):
    if layout.count("2") == layout.count("1"):
        return "1"
    else:
        return "2"


"""
#If you need to recreate the morpion_tree.json, use this code
import json
with open("morpion_tree.json", "w") as f:
    f.write(json.dumps(create_tree()))
"""

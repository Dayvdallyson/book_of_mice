def find_the_box(item_index):
    items = [
        "wall", "table", "box", "sofa", "lamp",
        "mirror", "pillow", "curtain", "chair", "television"
    ]

    if item_index >= len(items):
        return "There is no box!"

    if items[item_index] == "box":
        return "You found the box!"

    return find_the_box(item_index + 1)

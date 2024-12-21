initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

def add_menu_item(add_item):
    if add_item in initial_menu:
        return f"{add_item} is already exists"
    initial_menu.append(add_item)
    return f"Updated menu: {initial_menu}"

def remove_menu_item(remove_item):
    if remove_item not in initial_menu:
        return f"{remove_item} can't be deleted"
    initial_menu.remove(remove_item)

def check_menu_item(check_item):
    if check_item in initial_menu:
        return f"Availability: {check_item} is available"
    return f"Availability: {check_item} is not available"


remove_menu_item(remove_item)
print(add_menu_item(add_item))
print(check_menu_item(check_item))

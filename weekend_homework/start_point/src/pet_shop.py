# WRITE YOUR FUNCTIONS HERE

#1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#3/4
def add_or_remove_cash(pet_shop,val):
    shopcash = get_total_cash(pet_shop)
    newval = shopcash + val
    pet_shop["admin"]["total_cash"] = newval

#5
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#6
def increase_pets_sold(pet_shop,val):
    shoppets = get_pets_sold(pet_shop)
    newval = shoppets + val
    pet_shop["admin"]["pets_sold"] = newval

#7
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

#8
def get_pets_by_breed(pet_shop,breed):
    newl = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            newl.append(pet["breed"])
    return newl

#9
def find_pet_by_name(pet_shop,pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

#10
def remove_pet_by_name(pet_shop,pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

#11
def add_pet_to_stock(pet_shop,new_pet):
    pet_shop["pets"].append(new_pet)

#12
def get_customer_cash(customer_list_index):
    return customer_list_index["cash"]

#13
def remove_customer_cash(customer_dictionary,monies_amount):
    customer_dictionary["cash"] -= monies_amount

#14
def get_customer_pet_count(customer_dictionary):
    pet_count = 0
    for pet in customer_dictionary["pets"]:
        pet_count += 1
    return pet_count

#15
def add_pet_to_customer(customer_dictionary,new_pet):
    customer_dictionary["pets"].append(new_pet)
    len(customer_dictionary["pets"])

#16/17/18 - Optional
def customer_can_afford_pet(customer_dictionary,new_pet_dictionary):
    return customer_dictionary["cash"] >= new_pet_dictionary["price"]
    
def sell_pet_to_customer(pet_shop, pet, customer):
    pet_nr = 0

    if pet is None:
        return "Pet not found"
    elif pet:
        pet_nr += 1
    
    if pet["price"] > customer["cash"]:
        return "Insufficient funds"
    else:
        remove_pet_by_name(pet_shop, pet)
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        increase_pets_sold(pet_shop,pet_nr)
        add_or_remove_cash(pet_shop, pet["price"])


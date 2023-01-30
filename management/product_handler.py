from menu import products



def get_product_by_id(product_id):
    
        if not type(product_id) == int:
            raise TypeError("product id must be an int")

        for product in products:
            if product["_id"] == product_id:
                return product
        return {}

def get_products_by_type(prodType):
    objects = []

    if not type(prodType) is str:
        raise TypeError('product type must be a str')
        
    for obj in products:
        if (prodType == obj['type']):
            objects.append(obj)
   
    return objects
    
def add_product(menu, **newProduct):
    newId = []

    for obj in menu:
        newId.append(obj['_id'])
    newId.sort()

    if (menu == []):
        newId = 1
    else:
        newId = newId[-1]+1

    newProduct['_id'] = newId

    menu.append(newProduct)
    return newProduct

def menu_report():
    product_count = len(products)
    average_price = 0

    for i in range(0, len(products)):
        average_price += products[i]["price"]


    total = 0
    most_type = ''

    for i in range(0, len(products)):
        count = 0 
        type_product = products[i]["type"]
        for j in range(0, len(products)):
            if products[j]["type"] == type_product:
                count += 1
        
        if count > total:
            most_type = type_product
            total = count



    return f'Products Count: {product_count} - Average Price: ${round(average_price/len(products), 2)} - Most Common Type: {most_type}'


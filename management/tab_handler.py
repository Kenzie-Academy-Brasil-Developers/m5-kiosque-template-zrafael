from menu import products 


def calculate_tab(table):
    sub = []

    for item in table:
        for prod in products:
            if (item['_id'] == prod['_id']):
                sub.append(prod['price'] * item['amount'])
    subTotal = sum(sub)
    return {'subtotal': f'${round(subTotal, 2)}'}

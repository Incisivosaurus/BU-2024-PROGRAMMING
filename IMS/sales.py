import random


def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
    restock_interval = 7 # How many days must be waited before restocking inventory

    # When it is restock day, the shop will be closed, thus we return early as we aren't selling anything.
    if current_day % restock_interval == 0:
        return available_items

    # Generate a random value from 0 to 200 to simulate sold units
    sold_units = random.randint(0, min(200, available_items)) # Using min will prevent us from selling more shirts than we have in stock
    available_items -= sold_units # Update the amount of available items after sales

    # Update the latest entries data
    inventory_records[-1][1] = sold_units # Update sold units to be the new accurate amount
    inventory_records[-1][3] = available_items # Update the new amount of available items
    
    return available_items

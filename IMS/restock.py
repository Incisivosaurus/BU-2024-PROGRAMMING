def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
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


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''
    # Stocking constants
    max_stock_levels = 2_000 # Max amount of stock that can be held at any given moment
    restock_interval = 7 # How many days must be waited before restocking inventory

    restocked_items = 0 # How many items we have restocked, 0 by default
    
    # Reset available items to 0 on day 0 as the simulation mistakenly starts at maximum stock
    if current_day == 0:
        available_items = 0

    # Check if it is time to restock
    if current_day % restock_interval == 0:
        restocked_items = max_stock_levels - available_items # Calculate the difference between max stock and current stock
        available_items += restocked_items # Add difference to the available stock

    # This function is entirely for restocking, thus sold units is always defaulted to zero
    # Using an array so it is mutable for daily_sales
    inventory_records.append([current_day, 0, restocked_items, available_items])

    return available_items

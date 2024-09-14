import os

INVENTORY_FILE = 'inventory.txt'

def load_inventory():
    inventory = {}
    if os.path.exists(INVENTORY_FILE):
        try:
            with open(INVENTORY_FILE, 'r') as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) == 4:
                        product_id, name, quantity, price = parts
                        inventory[product_id] = {
                            'name': name,
                            'quantity': int(quantity),
                            'price': float(price)
                        }
        except IOError:
            print('Error reading file.')
        except Exception as e:
            print(f"Couldn't load the file. {e}")
    return inventory

def save_inventory(inventory):
    try:
        with open(INVENTORY_FILE, 'w') as file:
            for product_id, details in inventory.items():
                file.write(f"{product_id}|{details['name']}|{details['quantity']}|{details['price']:.2f}\n")
    except IOError:
        print('Error saving.')
    except Exception as e:
        print(f'Error saving inventory: {e}')

def is_valid_id(product_id):
    return product_id

def add_product(inventory):
    try:
        product_id = int(input('Enter product ID: '))
        if not is_valid_id(product_id):
            print('Invalid product ID. It should be an integer.')
            return
        
        product_name = input('Enter product name: ')
        try:
            quantity = int(input('Enter quantity: '))
            price = float(input('Enter price: '))
        except ValueError:
            print('Invalid input. Quantity and price must be numbers.')
            return

        if product_id in inventory:
            print('Product ID already exists. Updating quantity.')
            inventory[product_id]['quantity'] += quantity
        else:
            inventory[product_id] = {
                'name': product_name,
                'quantity': quantity,
                'price': price
            }
        print('Product updated successfully.')
    except Exception as e:
        print(f'Error while adding. : {e}')

def view_inventory(inventory):
    try:
        if not inventory:
            print('Empty Inventory')
        else:
            for product_id, details in inventory.items():
                print('Product ID:', product_id)
                print('Name:', details['name'])
                print('Quantity:', details['quantity'])
                print('Price: ${:.2f}'.format(details['price']))
                print('---')
    except Exception as e:
        print(f'Error while viewing inventory.: {e}')

def place_order(inventory):
    try:
        product_id = input('Enter product ID to order: ')
        if not is_valid_id(product_id):
            print('Invalid product ID. It should be an integer.')
            return
        
        if product_id in inventory:
            try:
                quantity = int(input('Enter quantity to order: '))
            except ValueError:
                print('Invalid input. Quantity must be a number.')
                return

            if inventory[product_id]['quantity'] >= quantity:
                inventory[product_id]['quantity'] -= quantity
                print('Order placed successfully.')
            else:
                print('Insufficient quantity.')
        else:
            print('Product ID does not exist.')
    except Exception as e:
        print(f'Error while placing order: {e}')

def main():
    inventory = load_inventory()
    
    while True:
        try:
            print('Inventory Management System')
            print('1. Add Product')
            print('2. View Inventory')
            print('3. Place Order')
            print('4. Exit')
            
            choice = input('Enter your choice: ')
            
            if choice == '1':
                add_product(inventory)
            elif choice == '2':
                view_inventory(inventory)
            elif choice == '3':
                place_order(inventory)
            elif choice == '4':
                save_inventory(inventory)
                print('Inventory saved. Exiting.')
                break
            else:
                print('Invalid choice. Please try again.')
        except Exception as e:
            print(f'An error occurred: {e}')

main()

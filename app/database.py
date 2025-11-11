import csv 
import os 
import fcntl
class Database:
    def __init__(self, filename="products.csv"):
        self.filename = filename
        self.create_file()

    def create_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'name', 'price'])

    def get_all(self):
        products = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products.append({
                        'id': int(row['id']),
                        'name': row['name'],
                        'price': float(row['price'])
                    })
        except:
            return []
        return products

    def get_next_id(self):
        products = self.get_all()
        return max((int(p['id']) for p in products), default=0) + 1

    def add(self, name, price):
        new_id = self.get_next_id()
        with open(self.filename, 'a') as file:
            fcntl.flock(file.fileno(), fcntl.LOCK_EX)
            writer = csv.writer(file)
            writer.writerow([new_id, name, price])
            fcntl.flock(file.fileno(), fcntl.LOCK_UN)
        return {'id': new_id, 'name': name, 'price': price}

    def delete(self, product_id):
        products = self.get_all()
        found = any(p['id'] == product_id for p in products)

        if found:
            new_products = [p for p in products if p['id'] != product_id]
            with open(self.filename, 'w') as file:
                fcntl.flock(file.fileno(), fcntl.LOCK_EX)
                writer = csv.writer(file)
                writer.writerow(['id', 'name', 'price'])
                for p in new_products:
                    writer.writerow([p['id'], p['name'], p['price']])
                fcntl.flock(file.fileno(), fcntl.LOCK_UN)
            return True
        return False

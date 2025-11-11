from database import Database
import statistics

class ProductService:
    def __init__(self):
        self.db = Database()

    def create_product(self, name, price):
        if price <= 0:
            return {"error": "Price must be positive"}
        return self.db.add(name, price)

    def get_products(self):
        return self.db.get_all()

    def get_highest_price(self):
        products = self.db.get_all()
        if not products:
            return {"error": "No products"}
        return max(products, key=lambda x: x['price'])

    def get_lowest_price(self):
        products = self.db.get_all()
        if not products:
            return {"error": "No products"}
        return min(products, key=lambda x: x['price'])

    def get_average_price(self):
        products = self.db.get_all()
        if not products:
            return {"average": 0}
        prices = [p['price'] for p in products]
        return {"average": statistics.mean(prices)}

    def get_above_average(self):
        products = self.db.get_all()
        if not products:
            return []
        avg = statistics.mean(p['price'] for p in products)
        return [p for p in products if p['price'] >= avg]

    def get_below_average(self):
        products = self.db.get_all()
        if not products:
            return []
        avg = statistics.mean(p['price'] for p in products)
        return [p for p in products if p['price'] < avg]

    def delete_product(self, product_id):
        success = self.db.delete(product_id)
        if success:
            return {"message": "Product deleted"}
        return {"error": "Product not found"}
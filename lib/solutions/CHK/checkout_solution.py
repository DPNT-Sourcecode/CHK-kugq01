
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        item_prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15
        }

        special_offers = {
            'A': {'quantity': 3, 'price': 130},
            'B': {'quantity': 2, 'price': 45}
        }

        total_price = 0
        for sku in skus:
            if sku in item_prices:
                total_price += item_prices[sku]
            else:
                return -1

        return total_price    


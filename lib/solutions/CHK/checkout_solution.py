
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        import collections
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40
        }

        special_offers = {
            'A': [{'quantity': 5, 'price': 200}, {'quantity': 3, 'price': 130}],
            'B': [{'quantity': 2, 'price': 45}]
        }

        free_gift_offers = {
            'E': {'quantity': 2, 'free_item': 'B'}
        }

        if not isinstance(skus, str):
            return -1

        item_counts = collections.Counter(skus)
        total_price = 0

        for item, count in item_counts.items():
            if item not in prices:
                return -1
            
            if item in special_offers:
                offer = special_offers[item]
                offer_quantity = offer['quantity']
                offer_price = offer['price']
                
                # Apply special offers
                num_of_offers = count // offer_quantity
                total_price += num_of_offers * offer_price
                
                # Add the price of remaining items
                remaining_items = count % offer_quantity
                total_price += remaining_items * prices[item]
            else:
                total_price += count * prices[item]
                
        return total_price
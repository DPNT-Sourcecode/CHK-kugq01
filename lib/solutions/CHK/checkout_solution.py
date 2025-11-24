
class CheckoutSolution:

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

        for item in item_counts:
            if item not in prices:
                return -1
        
        if 'E' in item_counts and 'B' in item_counts:
            free_bs = item_counts['E'] // free_gift_offers['E']['quantity']
            item_counts['B'] = max(0, item_counts['B'] - free_bs)

        total_price = 0
        for item, count in item_counts.items():
            item_total = 0
            remaining_count = count

            if item in special_offers:
                for offer in special_offers[item]:
                    offer_quantity = offer['quantity']
                    offer_price = offer['price']
                    
                    num_of_offers = remaining_count // offer_quantity
                    item_total += num_of_offers * offer_price
                    remaining_count %= offer_quantity
            
            item_total += remaining_count * prices[item]
            total_price += item_total
                
        return total_price
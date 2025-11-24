
class CheckoutSolution:

    def checkout(self, skus):
        import collections
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
            "F": 10,
            "G": 20,
            "H": 10,
            "I": 35,
            "J": 60,
            "K": 70,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 20,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 17,
            "Y": 20,
            "Z": 21
        }

        special_offers = {
            'A': [{'quantity': 5, 'price': 200}, {'quantity': 3, 'price': 130}],
            'B': [{'quantity': 2, 'price': 45}],
            'F': [{'quantity': 3, 'price': 20}],
            'H': [{'quantity': 10, 'price': 80}, {'quantity': 5, 'price': 45}],
            'K': [{'quantity': 2, 'price': 120}],
            'P': [{'quantity': 5, 'price': 200}],
            'Q': [{'quantity': 3, 'price': 80}],
            'U': [{'quantity': 4, 'price': 120}],
            'V': [{'quantity': 3, 'price': 130}, {'quantity': 2, 'price': 90}]
        }

        free_gift_offers = {
            'E': {'quantity': 2, 'free_item': 'B'},
            'N': {'quantity': 3, 'free_item': 'M'},
            'R': {'quantity': 3, 'free_item': 'Q'}
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

        if 'N' in item_counts and 'M' in item_counts:
            free_ms = item_counts['N'] // free_gift_offers['N']['quantity']
            item_counts['M'] = max(0, item_counts['M'] - free_ms)

        if 'R' in item_counts and 'Q' in item_counts:
            free_qs = item_counts['R'] // free_gift_offers['R']['quantity']
            item_counts['Q'] = max(0, item_counts['Q'] - free_qs)

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






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

        group_offers = {
            'items': ('S','T','X','Y','Z'),
            'quantity': 3,
            'price': 45
        }

        if not isinstance(skus, str):
            return -1

        item_counts = collections.Counter(skus)

        for item in item_counts:
            if item not in prices:
                return -1
        
        for trigger_item, offer in free_gift_offers.items():
            if trigger_item in item_counts:
                free_item = offer['free_item']
                if free_item in item_counts:
                    num_offers = item_counts[trigger_item] // offer['quantity']
                    item_counts[free_item] = max(0, item_counts[free_item] - num_offers)

        total_price = 0

        group_items_in_basket = []
        sorted_group_skus = sorted(group_offers['items'], key=lambda i: prices[i], reverse=True)
        
        for item in sorted_group_skus:
            if item in item_counts:
                group_items_in_basket.extend([item] * item_counts[item])
        
        num_bundles = len(group_items_in_basket) // group_offers['quantity']
        if num_bundles > 0:
            total_price += num_bundles * group_offers['price']
            items_in_bundles = group_items_in_basket[:num_bundles * group_offers['quantity']]
            item_counts.subtract(collections.Counter(items_in_bundles))

        for item, count in item_counts.items():
            item_total = 0
            remaining_count = count

            if item in special_offers:
                for offer in special_offers[item]:
                    num_offers = remaining_count // offer['quantity']
                    item_total += num_offers * offer['price']
                    remaining_count %= offer['quantity']
            
            item_total += remaining_count * prices[item]
            total_price += item_total
                
        return total_price
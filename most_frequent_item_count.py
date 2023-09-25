from collections import Counter

def most_frequent_item_count(collection):
    # Do your magic. :)
    
    if not collection:
        return 0
    else:
        counter = Counter(collection)
        return counter.most_common(1)[0][1]

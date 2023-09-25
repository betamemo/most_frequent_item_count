def most_frequent_item_count(collection):
    # Do your magic. :)
    
    item_dict = {}
    freq_item = 0
    
    for c in collection:
        if c in item_dict:
            item_dict[c] = item_dict[c] + 1
        else:
            item_dict[c] = 1
    
    for d in item_dict:
        if item_dict[d] > freq_item:
            freq_item = item_dict[d]
    return freq_item

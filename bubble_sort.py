def bubble_sort(item,greatest = True):
    """
    Parameters:
    
    item - is assumed to be a list item 
    greatest - if true returned order is greatest to least. Else it is least to greatest
    """
    
    for element in range(len(item)):
        for element2 in range(element,len(item)):
            if item[element] < item[element2]:
                x = item[element]
                item[element] = item[element2]
                item[element2] = x
            else:
                pass
    
    if not greatest:
        item.reverse()
    return item

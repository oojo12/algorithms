def bubble_sort(item,least = False):
    """Implementation of bubble sort"""

    """
    Parameters:

    item - is assumed to be a list item
    least - if true returned order is least to greatest. Else it is greatest to least
    """
    __author__ = "Femi"
    __version__ = "1"
    __status__ = "Done"
    
    for element in range(len(item)):
        for element2 in range(element,len(item)):
            if item[element] < item[element2]:
                x = item[element]
                item[element] = item[element2]
                item[element2] = x
            else:
                pass

    if least:
        item.reverse()
    return item

def insertion_sort(item, least = False):
    """Implementation of insertion sort"""

    """
    Parameters:

    item - is assumed to be a list item
    least - if true returned order is least to greatest. Else it is greatest to least
    """
    __author__ = "Femi"
    __version__ = "1"
    __status__ = "Done"
    
    for curr in range(len(item)):
        for next in range(len(item)):
            if (item[curr] <= item[next]):
                pass
            else:
                item[curr],item[next] = item[next], item[curr]
    if least:
        item.reverse()
    else:
        pass
    return item

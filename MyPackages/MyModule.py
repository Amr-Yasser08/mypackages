def top_n (items,n):

    """Return the top n items in array, in desc order.

    Args: 
        items (array): list or array-lke object
        n (int): num of items to return
    
    Return: 
        array: top n items, in desc order
    
    Egs:
        >>> top_n([8,3,2,7,4],3)
        [8,7,3]

    """
    for i in range(n): # keep sorting unntill we have the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]: #iif this item is bigger than the next item..
                items[j], items[j+1] = items[j+1], items [j] #Swap the 2
    #get last 2 items
    top_n = items[-n:]
    #return in desc order
    return top_n[::-1]
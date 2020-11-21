def sorterDicLen(dictionary):
    '''
        Method that sorts decremental length key 

        :param dictionary: Dictionary to sort
        :type dictionary: dict
        :returns: Sorted  dictionary by key decremental length
        :rtype: dict

        :Example:
            In [1]: from dictionarySorter import sorterDicLen

            In [2]: dict = {"abcd":"this is abcd",
                "ab":"this is ab",
                "aaaaa":"this is 5 times a",
                "aaa":"this is 3 times a"}

            In [3]: sorterDicLen(dict)
            Out[3]:
                {'aaaaa': 'this is 5 times a',
                 'abcd': 'this is abcd',
                 'aaa': 'this is 3 times a',
                 'ab': 'this is ab'}

        .. todo:: Find a more efficient method?

    '''
    newDict={}
    # sort the keys into a list  by lenght in a reverse order
    sortedKeysList = sorted(dictionary, key=len, reverse=True)
    # fill a new dictionary with the list order
    for key in sortedKeysList:
        newDict[key] = dictionary[key]
    # return the new Dictionary
    return newDict


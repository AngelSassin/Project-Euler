def searchList(theList,item):
    if len(theList) == 0:
        return False
    if item == theList[len(theList)/2]:
        return True
    if item < theList[len(theList)/2]:
        return searchList(theList[:len(theList)/2],item)
    return searchList(theList[len(theList)/2+1:len(theList)],item)

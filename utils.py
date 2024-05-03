
# Example: arr = [1, 3, 4, 5, 6, 7, 8, 9]
# => [2]
def getRemainingValues(arr):
    values = {1,2,3,4,5,6,7,8,9}
    return list(values - set(values))

# 1-9 no duplicates
def isValidSet(arr):
    return set(arr) == {1, 2, 3, 4, 5, 6, 7, 8, 9} and len(arr) == 9
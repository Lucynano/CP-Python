# an iterative binary search 
def iterative_search(arr, low, high, x):
    while(low <= high):
        mid = low + ((high - low) // 2)
        if(arr[mid] < x):
            low = mid + 1
        elif(arr[mid] > x):
            high = mid - 1
        else:
            return mid
    return -1

# an recursive binary search 
def recursive_search(arr, low, high, x):
    if(low <= high):
        mid = low + ((high - low) // 2)
        if(arr[mid] < x):
            return recursive_search(arr, mid - 1, high, x)
        elif(arr[mid] > x):
            return recursive_search(arr, low, mid + 1, x)
        else:
            return mid
    else:
        return -1

if __name__ == "__main__":
    arr = [-3, -1, 0, 3, 7, 11, 13, 16, 34]
    res = recursive_search(arr, 0, (len(arr) - 1), 1)
    if(res == -1):
        print("NO")
    else:
        print("YES")
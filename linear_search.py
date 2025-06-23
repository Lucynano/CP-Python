def search(arr, l, x):
    for i in range(0, l):
        if(x == arr[i]):
            return i
    return -1

if __name__ == "__main__":
    arr = [3, 6, 3, 7, 9, 10, 5, 25]
    l = len(arr)

    res = search(arr, l, 11)
    if(res == -1):
        print("NO")
    else:
        print("YES")
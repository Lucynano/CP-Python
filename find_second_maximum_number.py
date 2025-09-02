if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s = set(arr)
    l = sorted(s, reverse = True)
    print(l[1])
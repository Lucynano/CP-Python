if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())   
        l.append([name, score])
    second = min(s for n, s in l if s != min(s for n, s in l))
    names_low_grd = sorted(n for n, s in l if s == second)
    for n in names_low_grd:
        print(n)
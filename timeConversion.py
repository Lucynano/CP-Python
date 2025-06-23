def timeConversion(s):
    period = s[-2:]
    hour = int(s[:2])
    rest = s[2:-2]
    
    if hour == 12 and period == "AM":
        hour = 0
    if hour != 12 and period != "AM":
        hour += 12
        
    return f"{hour :02d}{rest}"
        

if __name__ == '__main__':
    s = str(input())

    print(timeConversion(s))

def timeConversion(s):
    hour = int(s[0:2])
    
    formato  = s[-2:]
    new_formato = '00:00:00'
    if hour == 12 and formato == 'AM':
        hour = '00'
        new_formato = str(hour) + ':' + s[3:5] + ':' + s[6:8]
    elif hour == 12:
        new_formato = str(hour) + ':' + s[3:5] + ':' + s[6:8]
    elif formato == 'AM':
        new_formato = s[0:2] + ':' + s[3:5] + ':' + s[6:8]
    elif formato == 'PM':
        new_formato = str(hour + 12) + ':' + s[3:5] + ':' + s[6:8]
        
    return new_formato
s = input()

result = timeConversion(s)
print(result)
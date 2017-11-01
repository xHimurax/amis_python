n=int(input('Hello, please, enter the number of minutes:',))
d1=n//60
d2=n%60
d3=n%1440
d4=d3//60
d5=d3%60
if (n<=0):
    print('the time is:', '00',':','00')
else:
    if(0<n<60):
        print('the time is:', '00',':','n')
    else:
        if(60<n<1440):
            print('the time is:',d1,':',d2)
        else:
            if (1440<=n):
                    print('the time is:',d4,':',d5)

#complete
months = [31,28,31,30,31,30,31,31,30,31,30,31]
fmonths = [31,29,31,30,31,30,31,31,30,31,30,31]
mon = []
fmon = []
for n,  month in enumerate(months):
    if n > 0:
        mon.append(months[n] + mon[n-1])
    else:
        mon.append(months[n])
for n,  month in enumerate(fmonths):
    if n > 0:
        fmon.append(fmonths[n] + fmon[n-1])
    else:
        fmon.append(fmonths[n])

print(mon)
print(fmon)
sundays = 0
cumulative = 365
for year in range(1901, 2001):
    if year%4 == 0 :
        for fmonth in fmonths:
            if cumulative%7 == 1:
                sundays += 1
            cumulative += fmonth
    else: 
        for month in months:
            if cumulative%7 == 1:
                sundays += 1
            cumulative += month
print(sundays)

swimming = int(input("Enter Swim (in minutes) ? "))
cycling = int(input("Enter Cycling (in minutes) ? "))
running = int(input("Enter Running (in minutes) ? "))

total_time = swimming + cycling + running
print(total_time)

if total_time <= 100:
    print("Provincial colours")
elif total_time <= 105:
    print("Provincial half colours")
elif total_time <= 110: 
    print("Provinvial Scroll")
else:
    print("No Award")
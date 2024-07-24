print('Travel fom city A to City B')

time = int(input("Enter time: "))
longer = int(input("Define longer: "))

if(time>=longer):
    price = int(input("Enter Price: "))
    higher = int(input("Define higher: "))
    if(price>=higher):
        print('Train')
    else:
        print("Coach")

else:
    price = int(input("Enter Price: "))
    higher = int(input("Define higher: "))
    if(price>=higher):
        print('Day time flight')
    else:
        print("Red eye flight")

print('Arrive City B')
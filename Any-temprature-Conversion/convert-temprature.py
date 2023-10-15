choose = int(input('1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius\n3. Fahrenheit to Kelvin\n4. Kelvin to Fahrenheit\n5. Kelvin to Celsius\n6. Celsius to Kelvin\n Choose Your option :  '))

if choose == 1 :
    c = int(input('Enter Temprature in celcius : '))

    def far(cel) :
       return (cel * 9/5) + 32
    temp = far(c)
    print(f"{c}°C = {temp}°F")
elif choose == 2 :
    f = int(input('Enter Temprature in Fahrenheit : '))
    def cel(far) :
        return (5/9)*(f-32)
    temp = cel(f)
    print(f"{f}°F = {temp}°C")
elif choose == 3 :
    f = int(input('Enter Temprature in Fahrenheit : '))  
    def kel(far) :
        return ((f + 459.67) * 5/9)
    temp = kel(f)
    print(f"{f}°F = {temp}°K")
elif choose == 4 :
    k = int(input('Enter Temprature in Kelvin : '))
    def far(kel) :
        return (k*(9/5))-459.67
    temp  = far(k)
    print(f"{k}°K = {temp}°F")
elif choose == 5 :
    k = int(input('Enter Temprature in kelvin : '))
    def cel(kel):
        return k - 273.75
    temp = cel(k)
    print(f"{k}°K = {temp}°C")
elif choose == 6 :
    c = int(input('Enter Temprature in Celcius : '))
    def kel(cel):
        return c + 273.75
    temp = kel(c)
    print(f"{c}°C = {temp}°K")
else : print("Please enter from above options only")

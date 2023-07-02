# This is just my practice

# Program Converting Temperatur

print("Program Konversi Temperature")

input_celcius = float(input("Masukan suhu dalam celcius : "))
print(f"suhu dalam celcius adalah {input_celcius} C")


def From_Celcius():
    '''from Celcius to Reamur'''
    reamur = (4/5)*input_celcius
    print(f"suhu dalam reamur adalah {reamur} R")

    '''from Celcius to Fahrenheit'''
    fahrenheit = (9/5) * input_celcius + 32
    print(f"suhu dalam fahrenheit adalah {fahrenheit} F")

    '''from Celcius to Kelvin'''
    kelvin = input_celcius + 273
    print(f"suhu kelvin adalah {kelvin} K")

From_Celcius()

input_reamur = float(input("Masukan suhu dalam reamur :  "))
print(f"suhu dalam reamur adalah {input_reamur} R")

def From_Reamur():
    '''from Reamur to Celcius'''
    celcius = (5/4)*input_reamur
    print(f"suhu dalam celcius adalah {celcius} C")

    '''from Reamur to Fahrenheit'''
    fahrenheit = (9/4)*input_reamur + 32
    print(f"suhu dalam fahrenheit adalah {fahrenheit} F")

    '''from Reamur to Kelvin'''
    kelvin = (5/4) * input_reamur + 273
    print(f"suhu dalam kelvin adalah {kelvin} K")


From_Reamur()
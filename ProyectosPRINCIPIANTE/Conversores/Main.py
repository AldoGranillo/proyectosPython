print("Ingrese que a que quiere convertir \n 1.-De Celcius a Fahrenheit \n 2.-De Fahrenheit a Celcius \n "
      "3.-De Celcius a Kelvin \n 4.-De Kelvin a Celcius \n 5.-De Kelvin a Fahrenheit \n 6.-De Fahrenheit a Kelvin")
opcion = int(input("Ingrese la opcion: "))
grados = int(input("Ingrese los grados: "))


def celcius_F(grados):
    gradosF = (grados * 1.8) + 32
    return gradosF


def fahrenheit_C(grados):
    gradosC = (grados - 32) / 1.8
    return gradosC


def celcius_K(grados):
    gradosK = grados + 273.15
    return gradosK


def kelvin_C(grados):
    gradosC = grados - 273.15
    return gradosC


def fahrenheit_K(grados):
    gradosK = ((grados - 32) / 1.8) + 273.15
    return gradosK


def kelvin_F(grados):
    gradosF = ((grados - 273.15) * 1.8) + 32
    return gradosF


if opcion == 1:
    conv1 = celcius_F(grados)
    print(conv1)
elif opcion == 2:
    conv2 = fahrenheit_C(grados)
    print(conv2)
elif opcion == 3:
    conv3 = celcius_K(grados)
    print(conv3)
elif opcion == 4:
    conv4 = kelvin_C(grados)
    print(conv4)
elif opcion == 5:
    conv5 = fahrenheit_K(grados)
    print(conv5)
else:
    conv6 = kelvin_F(grados)
    print(conv6)

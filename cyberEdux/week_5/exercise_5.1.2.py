# Exercise 5.1.2

def input_validation(type):
    match type:
        case "Weight":
            weight = float(input("Weight: "))
            while weight <= 0:
                weight = float(input("Weight: "))
            return weight
        case "Height":
            height = float(input("Height: "))
            while height <= 0:
                height = float(input("Height: "))
            return height
        
def imc_calculation(weight, height):
    return weight/height**2

def imc_classification(imc):
    if imc < 18.5:
        return "Abaixo do peso!"
    elif 18.5 < imc <= 25:
        return "Normal."
    elif 25 < imc <= 30:
        return "Sobrepeso!"
    else:
        return "Obesidade!"
    
weight = input_validation("Weight")
height = input_validation("Height")

print(imc_classification(imc_calculation(weight, height)))
            



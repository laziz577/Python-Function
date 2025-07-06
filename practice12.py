def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi
def bmi_status(bmi):
    if bmi <= 18.5: print("ozg'in")
    elif 18.5 < bmi <= 25: print("normal")
    elif 25 < bmi <= 30: print("ortiqcha vazn")
    else: print("semiz")

w = float(input("ogirlik:"))
h = float(input("bo'y:")) 

bmi = calculate_bmi(w,h)
bmi_status(bmi)

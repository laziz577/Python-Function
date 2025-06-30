def phone_number(phone):
    return len(phone) == 9

phone = input("phone:")
if phone_number(phone):
    print("tug'ri raqam")
else:
    print("xato raqam") 
       
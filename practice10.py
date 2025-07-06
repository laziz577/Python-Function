def strong_password(password :str):

    if len(password) >= 8 and password.isalnum() :
        text = "sizning parolingiz kuchli"
        return text
    else:
        text = "parolingiz kuchli emas"
        return text
def main():
    password = input("parolingizni kiriting: ")
    print(strong_password(password))
main()
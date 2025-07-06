def is_palindrome(a):
    if a == a[::-1]:
        return 'palindrom suz'
    else:
        return "palindrom suz emas"
    
def qidiruv() :
    suz = input("suzni kiriting:")
    print(is_palindrome(suz))

qidiruv()

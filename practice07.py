def savol_javob(savol):
    javob = input(savol)
    return(savol)
def tugri_javob(kerakli_javob,qisqa_javob):
    return kerakli_javob == qisqa_javob
savol = "2 + 2 = "
javob = savol_javob(savol)
tugri = tugri_javob(javob,"4")

if tugri:
    print("ajoyib")
    
else:
    print("afsus xato")


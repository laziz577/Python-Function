def ball_hisobi(bal):
  if 90 <= bal <= 100:
    return "A"
  elif 80 <= bal <= 89:
    return "B"
  elif 70 <= bal <= 79:
    return "C"
  elif 60 <= bal <= 69:
    return "D"
  elif 0 <= bal <= 59:
    return "F"
  else:
    return "Xatolik"
ball = int(input("Ballni kiriting:"))
hisob = ball_hisobi(ball)

print(hisob)


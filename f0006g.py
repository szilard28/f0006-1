#Kérdezd meg a felhasználótól a nevét, a nemét és a napszakot, majd köszöntsd őt a napszaknak megfelelően, angolul (vagy németül, vagy franciául, vagy akárhogy, ahol tudsz a nemnek megfelelő, Mr. illetve Ms. – jellegű előtagot)! Először állítsd elő a köszöntést, és egyetlen sorban használj print-et, mint a b feladatban!
print('Kérem a nevedet! ')
name = input() 
print('Fiú vagy vagy lány? ')
gender = input()
print('Milyen napszak van most? ')
daytime = input()

if gender == 'fiu':
  k2 = 'Hello Mr. '
else:
  k2 = 'Hello Ms. '

if daytime == "reggel":
  k1 = "Good morning."
else:
  k1 = "Good evening"
print(k1, k2, name )
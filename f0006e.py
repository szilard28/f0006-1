# "A háromszög bármely oldalának hossza kisebb a másik két oldal hosszának összegénél” – így a tétel. Írj programot, amely bekéri a b és c hosszát, majd megmondja, hogy szerkeszthető-e a háromszög."
a = 3
b = 6
c = 5

if a + b > c and a + c > b and b + c > a:
  print('Szerkeszthető. ')
else: 
  print('Nem szerkeszthető. ')
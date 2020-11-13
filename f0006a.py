évszak = input('Melyik évszak van? (ny/ő) ')
esik = input('Esik? (i/n) ')
szél = input('Fúj a szél? (i/n) ')
 
if (évszak == 'ny' and szél == 'n') or (évszak == 'ő' and esik == 'n' \
                                        and szél == 'n'):
    print('megyünk')
else:
    print('maradunk')
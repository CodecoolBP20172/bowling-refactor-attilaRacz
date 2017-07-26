def score(game): # az argument az eredmény stringként kifejezve
    result = 0 # az eredmény számláló
    frame = 1 # a kör számláló
    first_roll = True # a kör első gurítása
    for i in range(len(game)): # végigiterál az eredmény karakterein
        if game[i] == '/': # ha spare van, a következő kör első gurításának eredménye ide számlálódik bónuszként
            result += 10 - get_value(game[i-1]) # hozzáadja a következő gurítás első eredményét bónuszként
        else:
            result += get_value(game[i]) # hozzáadja az aktuális értéket
        # if not first_roll:
            # frame += 1
        if frame < 10  and get_value(game[i]) == 10: # ha 10 kör alatt vagyunk
            if game[i] in 'xX/': # ha spare van, hozzáadjuk a következő kör első értékét is
                result += get_value(game[i+1])
                if game[i] in 'xX' and game[i+2] == '/': # ha a strike után kettőve spare-t gurítunk, hozzáadjuk a spare értékét
                    result += 10 - get_value(game[i+1]) # a spare értéke
                elif game[i] in 'xX' and game[i+2] != '/':
                    result += get_value(game[i+2]) # hozzáadjuk a következő gurítás értékét is
        if not first_roll: # a második kör végén hozzáad egyet a körszámlálóhoz
            frame += 1
        if first_roll: # az első gurítás végén átvált a második felére
            first_roll = False
        else:
            first_roll = True # egyébként hagyja
        if game[i] in 'xX': # ha strike-ot gurítottunk, a következő kör első gurítása jön
            first_roll = True
            frame += 1
    return result

def get_value(char): # az inteket intként adja vissza, a strike-ot, a spare-t a megfelelő értékként
    if char in '123456789':
        return int(char)
    elif char in 'xX/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

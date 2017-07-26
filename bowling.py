def score(game): # az argument az eredmény stringként kifejezve
    result = 0 # az eredmény számláló
    frame = 1 # a kör számláló
    in_first_half = True # a kör első gurítása
    for i in range(len(game)): # végigiterál az eredmény karakterein
        if game[i] == '/': # ha spare van, a következő kör első gurításának eredménye ide számlálódik bónuszként
            result += 10 - last # hozzáadja a következő gurítás első eredményét bónuszként
        else:
            result += get_value(game[i]) # hozzáadja az aktuális értéket
        # if not in_first_half:
            # frame += 1
        if frame < 10  and get_value(game[i]) == 10: # ha 10 kör alatt vagyunk
            if game[i] == '/': # ha spare van, hozzáadjuk a következő kör első értékét is
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x': # ha strike van, hozzáadjuk a következő kör első értékét is
                result += get_value(game[i+1])
                if game[i+2] == '/': # ha a strike után kettőve spare-t gurítunk, hozzáadjuk a spare értékét
                    result += 10 - get_value(game[i+1]) # a spare értéke
                else:
                    result += get_value(game[i+2]) # hozzáadjuk a következő gurítás értékét is
        last = get_value(game[i]) # ???
        if not in_first_half: # a második kör végén hozzáad egyet a körszámlálóhoz
            frame += 1
        if in_first_half == True: # az első gurítás végén átvált a második felére 
            in_first_half = False
        else:
            in_first_half = True # egyébként hagyja
        if game[i] == 'X' or game[i] == 'x': # ha strike-ot gurítottunk, a következő kör első gurítása jön
            in_first_half = True
            frame += 1
    return result

def get_value(char): # az inteket intként adja vissza, a strike-ot, a spare-t a megfelelő értékként
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

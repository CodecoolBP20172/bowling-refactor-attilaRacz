def score(game):
    result = 0
    frame = 1
    first_roll = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - get_value(game[i-1])
        else:
            result += get_value(game[i])
        if frame < 10  and get_value(game[i]) == 10:
            if game[i] in 'xX/':
                result += get_value(game[i+1])
                if game[i] in 'xX' and game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                elif game[i] in 'xX' and game[i+2] != '/':
                    result += get_value(game[i+2])
        if not first_roll:
            frame += 1
        if first_roll:
            first_roll = False
        else:
            first_roll = True
        if game[i] in 'xX':
            first_roll = True
            frame += 1
    return result

def get_value(char):
    if char in '123456789':
        return int(char)
    elif char in 'xX/':
        return 10
    elif char == '-':
        return 0


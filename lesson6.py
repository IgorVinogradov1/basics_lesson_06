password = input('Введите пароль: ')

def is_very_long(password):
    result = len(password) >= 12
    return result
def has_digit(password):
	return any(symbol.isdigit() for symbol in password)
def has_lower_letters(password):
	return any(symbol.islower() for symbol in password)
def has_upper_letters(password):
	return any(symbol.isupper() for symbol in password)
def has_symbols(password):
    return any(not (symbol.isdigit() or symbol.isalpha()) for symbol in password)
def rating_calculation():
    score = 0
    checklist = [
        is_very_long(password),
        has_digit(password),
        has_lower_letters(password),
        has_upper_letters(password),
        has_symbols(password)
    ]
    for i in range(len(checklist)):
    	if checklist[i]:
            score += 2
    print('Рейтинг пароля: ', score)
rating_calculation()




import random

def guess_number():
    # Загадываем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    print("Для выхода введи '0'")
    
    while True:
        try:
            # Получаем ввод от пользователя
            guess = input("Введи свое предположение: ")
            
            # Проверяем, хочет ли пользователь выйти
            if guess == '0':
                print(f"Игра окончена. Загаданное число было: {secret_number}")
                break
            
            # Преобразуем ввод в число
            guess = int(guess)
            attempts += 1
            
            # Проверяем диапазон
            if guess < 1 or guess > 100:
                print("Пожалуйста, введи число от 1 до 100!")
                continue
            
            # Сравниваем с загаданным числом
            if guess < secret_number:
                print("Мое число больше!")
            elif guess > secret_number:
                print("Мое число меньше!")
            else:
                print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                break
                
        except ValueError:
            print("Пожалуйста, введи целое число!")

# Запускаем игру
if __name__ == "__main__":
    guess_number()
def talking(message: str) -> str:
    '''Чат-бот, который отвечает на "привет", "как дела" и "пока"
    message - входящее сообщение
    return - ответ бота
    '''
    if message.lower() in ["привет", "здравствуйте", "здравствуй"]:
        return "Здравствуйте!"
    elif message.lower() == "как дела?":
        return "Лучше всех :)"
    elif message.lower() in ["пока", "до свидания"]:
        return "До свидания!"
    elif message.lower() == "кто ты?":
        return "Я чат-бот"
    elif message.lower() == "реши уравнение":
        return "Введите коэффициенты a, b, c через запятую"
    elif message.lower() == "посчитай":
        return "Введите выражение вида 'a + b'"
    elif message.lower() == "проверь на палиндром":
        print('Бот: "Введите слово"')
        return palindrome_checker(input("Пользователь: "))
    else:
        return "Я вас не понимаю"


def calculator(a: int, b: int, operation: str) -> str:
    '''Калькулятор
    a, b - числа
    operation - операция
    return - результат
    '''
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b


def solver(a: int, b: int, c: int) -> str:
    '''Решение квадратного уравнения
    a, b, c - коэффициенты
    return - результат
    '''
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return f"x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b / (2*a)
        return f"x = {x}"
    else:
        return "Корней нет"


def palindrome_checker(word: str) -> str:
    '''Проверка на палиндром
    word - слово
    return - "Это палиндром", если палиндром, "Это не палиндром" - если не палиндром
    '''
    if word == word[::-1]:
        return "Это палиндром"
    return "Это не палиндром"


def main():
    while True:
        user_input = input("Пользователь: ")
        try:
            if user_input == "stop":
                break
            elif user_input.split()[1] in ["+", "-", "*", "/"]:
                a = int(user_input.split()[0])
                b = int(user_input.split()[2])
                operation = user_input.split()[1]
                print(f'Бот: "{calculator(a, b, operation)}"')
            elif (
                    int(user_input.split(", ")[0]) and
                    int(user_input.split(", ")[1]) and
                    int(user_input.split(", ")[2])
                    ):
                a = int(user_input.split(", ")[0])
                b = int(user_input.split(", ")[1])
                c = int(user_input.split(", ")[2])
                print(f'Бот: "{solver(a, b, c)}"')
        except Exception as ex:
            print(f'Бот: "{talking(user_input)}"')


if __name__ == "__main__":
    main()

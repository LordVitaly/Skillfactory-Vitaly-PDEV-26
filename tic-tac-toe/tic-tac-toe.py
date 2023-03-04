slots = [str(i + 1) for i in range(9)]


def field(slots):  # Функция выведения игрового поля
    for n in range(3):
        print(f" {slots[n * 3]} | {slots[n * 3 + 1]} | {slots[n * 3 + 2]}")
        if n != 2:
            print("————————————")


def win_check(slots):  # Функция проверки победителя
    # Ищем одинаковые символы по горизонтали
    for line in range(3):
        if slots[line * 3] == slots[line * 3 + 1] == slots[line * 3 + 2]:
            return 1
    # Ищем одинаковые символы по вертикали
    for column in range(3):
        if slots[column] == slots[column + 3] == slots[column + 6]:
            return 1
    # Ищем одинаковые символы по диагонали - слева направо
    if slots[0] == slots[4] == slots[8]:
        return 1
    # Ищем одинаковые символы по диагонали - справа налево
    if slots[2] == slots[4] == slots[6]:
        return 1
    # Ничья - проверяем, есть ли еще свободные клетки на поле (смотрим, все ли клетки заполнены символами, а не цифрами)
    if turn > 9:
        return 2


def game_restart():  # Функция повторной игры
    q = 0
    while q == 0:  # Спрашиваем, пока не будет утвердительного ответа, либо пока игрок не решит окончить игру
        game_restart_decision = int(input("Сыграть еще матч? (1 = Да, 2 = Нет). Выбор: "))
        if game_restart_decision == 1:  # Начинаем следующий матч
            q = 1
        elif game_restart_decision == 2:  # оканчиваем игру
            exit()
        else:  # Если что-то не то введено, то переспрашиваем
            print("Ошибка ввода, используйте только вариант 1 или 2")


# Приветствие на старте
print('''
        Игра "Крестики-нолики" v.0.5 (для двух игроков). Автор скрипта: Соколов Виталий (LordVitaly)
        
        Реализовано:
        - игровое поле;
        - выбор фигуры для первого игрока;
        - ход для каждого игрока (с учетом выбранной фигуры);
        - проверка выигрышных позиций;
        - общий счет.
        
        =========================================
    ''')

# Предлагаем начать игру
while True:  # Спрашиваем, пока не будет утвердительного ответа, либо пока игрок не передумает начинать игру
    game_start_decision = int(input("Начать игру? (1 = Да, 2 = Нет). Выбор: "))
    if game_start_decision == 1:  # Начинаем
        break
    elif game_start_decision == 2:  # Закрываем игру
        exit()
    else:  # Если что-то не то введено, то переспрашиваем
        print("Ошибка ввода, используйте только вариант 1 или 2")

# Игра идет до тех пор, пока игрок хочет начинать следующий матч,
# иначе - показывает финальный общий счет и скрипт останавливается
winner = 0
match_going = 1
player1_score = 0
player2_score = 0
player_1 = "Игрок 1"
player_2 = "Игрок 2"
while True:
    p1fig = None
    p2fig = None
    fig_choice = int(input("Фигура для Игрока 1 (1 = Х, 2 = О): "))
    if fig_choice == 1:
        p1fig = "X"
        p2fig = "O"
        match_going = 1
    elif fig_choice == 2:
        p1fig = "O"
        p2fig = "X"
        match_going = 1
    else:  # Если что-то не то введено, то переспрашиваем
        print("Ошибка ввода, используйте только вариант 1 или 2")

    # Сама игра
    turn = 1
    while match_going == 1:  # Матч будет идти, пока не сработает триггер окончания матча
        field(slots)  # Выводим игровое поле
        print(f"Номер хода: {turn}")
        # Проводим присваивание очередности ходов
        current_player_symbol = p1fig if (turn + fig_choice) % 2 == 0 else p2fig
        # Кто из игроков сейчас ходит
        current_player_name = player_1 if (turn + fig_choice) % 2 == 0 else player_2
        number_check = 1
        while number_check == 1:  # Запрашиваем ввод, пока не получим удобоваримый результат
            player_input = input(f"Ходит {current_player_name} ({current_player_symbol}). Выберите незанятую позицию (от 1 до 9): ")
            if not player_input.isdigit() or not (0 < int(player_input) < 10):
                print("Пожалуйста, введите число в диапазоне от 1 до 9")
            elif not slots[int(player_input)-1].isdigit():
                print("Выбранная ячейка уже занята, выберите другую")
            else:
                slots[int(player_input)-1] = current_player_symbol
                number_check = 0  # Заканчиваем цикл проверки ввода
        turn += 1  # Увеличиваем счетчик ходов на один. Если окажется более 9 ходов - ничья
        # Проверяем, не определился ли победитель
        winner = win_check(slots)
        if winner == 1 or winner == 2:  # Если сработал триггер победы или ничьей, то...
            field(slots)  # Показываем снова игровое поле, чтобы видеть, где победа (или ничья)
            if winner == 1:
                if current_player_name == player_1:
                    player1_score += 1
                else:
                    player2_score += 1
                print(f"{current_player_name} победил!")
                print("Общий счет")
                print(f"Игрок 1: {player1_score} | Игрок 2: {player2_score}")
            elif winner == 2:
                print("Ничья!")
                print(f"Игрок 1: {player1_score} | Игрок 2: {player2_score}")
            game_restart()  # Предлагаем сыграть еще раз
            i = 0  # Обнуляем переменную
            slots = [str(i + 1) for i in range(9)]  # Чистим игровое поле
            match_going = 0  # Заканчиваем матч, чтобы вернуться на выбор фигуры для игрока

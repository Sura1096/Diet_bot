CANCEL_LEXICON: dict[str, str] = {
    'valid_cancel': 'Чтобы снова перейти к заполнению анкеты - отправьте команду /go',
    'invalid_cancel': 'Отменять нечего.\n\n'
                      'Чтобы перейти к заполнению анкеты - отправьте команду /go',
}

QUESTIONS_LEXICON: dict[str, str] = {
    'name': 'Введите ваше ФИО.\n'
            'Пример ответа: Иванов Иван Иванович',
    'gender': 'Укажите свой пол.',
    'age': 'Укажите свой возраст.\n'
           'Пример ответа: Возраст 27 лет',
    'weight': 'Укажите свой вес.\n'
              'Пример ответа: Вес 95 кг',
    'height': 'Укажите свой рост.\n'
              'Пример ответа: Рост 183 см',
    'goal': 'Какова ваша цель?\n'
            'Пример ответа: Цель похудеть на 12 кг следующие 3 месяца',
    'allergy': 'Есть ли у вас на что-то аллергия?\n'
               'Пример ответа: Аллергия на цветение',
    'sport': 'Заниматесь ли вы спортом?\n'
             'Пример ответа: Занимаюсь 1 раз в неделю',
    'job': 'Как выглядит ваш типичный рабочий день?\n'
           'Пример ответа: Сидячая работа из дома за компьютером',
    'unwanted_products': 'Что из продуктов вы не употребляете?\n'
                         'Пример ответа: Не ем свинину, гречку, острое и креветки',
    'current_diet': 'Какой у вас рацион питания на данный момент?\n'
                    'Пример ответа: 3-х разовое питание с 2 перекусами',
    'schedule': 'Какой у вас график в течении недели?\n'
                'Пример ответа: Просыпаюсь в 7 часов утра, ложусь в 23 часов вечера. '
                'С понедельника по пятницу работаю',
    'bad_habits': 'Какие у вас есть вредные привычки?\n'
                  'Пример ответа: Вредных привычек нет',
    'digestive_problems': 'Есть ли у вас проблемы с пищеварением?\n'
                          'Пример ответа: Состояние пищеварения нормальное, болезней нет'
}

INCORRECT_DATA_LEXICON: dict[str, str] = {
    'name': 'ФИО введено некорректно. Пожалуйста, введите ваше ФИО.\n'
            'Пример ответа: Иванов Иван Иванович',
    'gender': 'Пол введен некорректно. Пожалуйста, укажите ваш пол.',
    'age': 'Возраст введен некорректно. Пожалуйста, укажите ваш возраст.\n'
           'Пример ответа: Возраст 27 лет',
    'weight': 'Вес введен некорректно. Пожалуйста, укажите ваш вес.\n'
              'Пример ответа: Вес 95 кг',
    'height': 'Рост введен некорректно. Пожалуйста, укажите ваш рост.\n'
              'Пример ответа: Рост 183 см'
}

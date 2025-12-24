from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    keyboard_button,
)


months = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь",
}


section = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Добавить трату", callback_data="add"),
            InlineKeyboardButton(text="Показать траты", callback_data="show"),
        ]
    ]
)


exit = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Выйти", callback_data="exit"),
        ]
    ]
)


def getYearsButton(years: list):
    years_button = [
        [InlineKeyboardButton(text=f"{year}", callback_data=f"year:{year}")]
        for year in years
    ]
    years_button.append([InlineKeyboardButton(text="Отменить", callback_data="exit")])
    return InlineKeyboardMarkup(inline_keyboard=years_button)


def getMonths():
    months_button = []
    row = []

    for num, name in months.items():
        row.append(InlineKeyboardButton(text=name, callback_data=f"month:{num}"))
        if len(row) == 3:
            months_button.append(row)
            row = []
    if row:
        months_button.append(row)

    months_button.append([InlineKeyboardButton(text="Отменить", callback_data="exit")])
    return InlineKeyboardMarkup(inline_keyboard=months_button)

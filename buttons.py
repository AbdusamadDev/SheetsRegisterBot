from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

region_button01 = KeyboardButton("Namangan")
region_button02 = KeyboardButton("Farg'ona")
region_button03 = KeyboardButton("Andijon")
region_button04 = KeyboardButton("Toshkent")
region_button05 = KeyboardButton("Samarqand")
region_button06 = KeyboardButton("Navoi")
region_button07 = KeyboardButton("Buxoro")
region_button09 = KeyboardButton("Sirdaryo")
region_button10 = KeyboardButton("Qashqadaryo")
region_button11 = KeyboardButton("Qoraqalpog'iston")
region_button12 = KeyboardButton("Jizzax")
region_button13 = KeyboardButton("Xorazm")
region_button13 = KeyboardButton("Surxondaryo")

button = ReplyKeyboardMarkup(row_width=3).add(
    region_button01,
    region_button02,
    region_button03,
    region_button04,
    region_button05,
    region_button06,
    region_button07,
    region_button09,
    region_button10,
    region_button11,
    region_button12,
    region_button13
)

# Create button classes
button1 = KeyboardButton("1 - sinf")
button2 = KeyboardButton("2 - sinf")
button3 = KeyboardButton("3 - sinf")
button4 = KeyboardButton("4 - sinf")
button5 = KeyboardButton("5 - sinf")
button6 = KeyboardButton("6 - sinf")
button7 = KeyboardButton("7 - sinf")
button8 = KeyboardButton("8 - sinf")
button9 = KeyboardButton("9 - sinf")
button10 = KeyboardButton("10 - sinf")
button11 = KeyboardButton("11 - sinf")

# Create keyboard markup
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
keyboard.row(button1, button2, button3)
keyboard.row(button4, button5, button6)
keyboard.row(button7, button8, button9)
keyboard.add(button10, button11)

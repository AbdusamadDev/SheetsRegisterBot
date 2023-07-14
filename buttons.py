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

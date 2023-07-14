from aiogram import Dispatcher, types, executor, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import logging
import dotenv
import os

import states, write, buttons


REGIONS = [
    "Namangan", 
    "Qashqadaryo", 
    "Toshkent", 
    "Farg'ona", 
    "Andijon", 
    "Buxoro", 
    "Navoi", 
    "Samarqand", 
    "Sirdaryo", 
    "Qoraqalpog'iston", 
    "Surxondaryo", 
    "Xorazm",
    "Jizzax"
]
storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
dotenv.load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))
disp = Dispatcher(bot=bot, storage=storage)


@disp.message_handler(commands=["start", "help"])
async def start_bot(message: types.Message):
    await message.answer("Hello! Bot is started Mr.{}".format(message.from_user.username))
    await message.answer("Enter your fullname, please: ")
    await states.UserDetails.fullname.set()

@disp.message_handler(state=states.UserDetails.fullname)
async def fullname(message: types.Message, state: FSMContext):
    if len(message.text.split(" ")) < 2:
        await message.answer("🧐")
        await message.answer("Enter both first name and last name")
    else:
        await state.update_data(fullname=message.text)   
        await message.answer("Enter your Region: ", reply_markup=buttons.button)
        await states.UserDetails.region.set()
    print((await state.get_data()))

@disp.message_handler(state=states.UserDetails.region)
async def region(message: types.Message, state: FSMContext):
    if message.text not in REGIONS:
        await message.answer("🧐")
        await message.answer("Please enter valid region!")
    else:
        await state.update_data(region=message.text)   
        await message.answer("Enter your Phone Number: ")
        await states.UserDetails.phone.set()
    print((await state.get_data()))

@disp.message_handler(state=states.UserDetails.phone)
async def phone(message: types.Message, state: FSMContext):
    phone_number = message.text

    
    if phone_number[1:].isdigit():
        if not phone_number.startswith("+"):
            phone_number = "+" + phone_number
        await state.update_data(phone=phone_number)
        await message.answer("How did you hear about us?")
        await states.UserDetails.identified_from.set()
    else:
        await message.answer("🧐")
        await message.answer("Enter valid numbers")


    print((await state.get_data()))
@disp.message_handler(state=states.UserDetails.identified_from)
async def phone(message: types.Message, state: FSMContext):
    await state.update_data(identified_from=message.text)
    print((await state.get_data()))
    data = await state.get_data()
    values = list(data.values()) + [message.from_user.id, message.from_user.username]
    print(values)
    print(write.append(sheets="Users!A:E", values=values))
    await message.answer("Data saved successfully!")
    await message.answer("🥳")
    await state.finish()



if __name__ == "__main__":
    executor.start_polling(dispatcher=disp, skip_updates=True)
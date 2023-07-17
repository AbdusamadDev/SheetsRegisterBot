from aiogram import Dispatcher, types, executor, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import logging
import dotenv
import os
import write
import buttons

from states import UserDetails

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
bot = Bot(token=str(os.getenv("TOKEN")))
disp = Dispatcher(bot=bot, storage=storage)


@disp.message_handler(commands=["start", "help"])
async def start_bot(message: types.Message):
    await message.answer("Assalomu alaykum {}".format(message.from_user.username))
    await message.answer("Ismingiz va familiyangizni kiriting: ")
    await UserDetails.fullname.set()


@disp.message_handler(state=UserDetails.fullname)
async def fullname(message: types.Message, state: FSMContext):
    if len(message.text.split(" ")) < 2:
        await message.answer("🧐")
        await message.answer("Iltimos, xato qilmay ismingiz va familiyangizni to'liq kiriting:")
    else:
        await state.update_data(fullname=message.text)
        await message.answer("Sinfingizni tanlang: ", reply_markup=buttons.keyboard)
        await UserDetails.course.set()
    print((await state.get_data()))


@disp.message_handler(state=UserDetails.course)
async def course(message: types.Message, state: FSMContext):
    labels = [f"{str(i)} - sinf" for i in range(1, 12)]
    if message.text in labels:
        await state.update_data(course=message.text)
        await message.answer("Shahringizni tanlang: ", reply_markup=buttons.button)
        await UserDetails.region.set()
    else:
        await message.answer(
            "Sinf xato kiritildi, iltimos tugmachalardan birini tanlang",
            reply_markup=buttons.keyboard
        )


@disp.message_handler(state=UserDetails.region)
async def region(message: types.Message, state: FSMContext):
    region = message.text

    if region not in REGIONS:
        await message.answer("🧐")
        await message.answer("Shahar xato kiritildi, iltimos tugmachalardan birini tanlang")
    else:
        await state.update_data(region=region)
        await message.answer("Tumaningizni kiriting: ")
        await UserDetails.strict.set()

    print((await state.get_data()))


@disp.message_handler(state=UserDetails.strict)
async def strict(message: types.Message, state: FSMContext):
    strict_input = message.text.strip()
    await state.update_data(strict=strict_input)
    await message.answer("Telefon raqamingizni kiriting:")
    await UserDetails.phone.set()


@disp.message_handler(state=UserDetails.phone)
async def phone(message: types.Message, state: FSMContext):
    phone_number = message.text

    if phone_number.isdigit():
        phone_number = "+" + phone_number  # Add "+" sign if missing
        await state.update_data(phone=phone_number)
        await message.answer("Qo'shimcha telefon raqamingiz bor bo'lsa kiriting, aks holda shunchaki yo'q deb davom eting:")
        await UserDetails.optional_phone.set()
    else:
        await message.answer("🧐")
        await message.answer("Iltimos yaroqli telefon raqam kiriting:")

    print((await state.get_data()))

@disp.message_handler(state=UserDetails.optional_phone)
async def optional_phone_number_message_handler(message: types.Message, state: FSMContext):
    phone_number = message.text

    if phone_number == "":
        await state.update_data(optional_phone="")
        await message.answer("Imtihon uchun o'zingizga qulay kunni kiriting: ")
        await UserDetails.exam_date.set()
    elif phone_number.isdigit():
        phone_number = "+" + phone_number  # Add "+" sign if missing
        await state.update_data(optional_phone=phone_number)
        await message.answer("Imtihon uchun o'zingizga qulay kunni kiriting: ")
        await UserDetails.exam_date.set()
    else:
        await message.answer("🧐")
        await message.answer("Iltimos, yaroqli telefon raqam kiriting:")

    print((await state.get_data()))


@disp.message_handler(state=UserDetails.exam_date)
async def exam_date(message: types.Message, state: FSMContext):
    await state.update_data(exam_date=message.text)
    await message.answer("Biz haqimizda qayerdan xabar topdingiz?")
    await UserDetails.identified_from.set()
    print((await state.get_data()))


@disp.message_handler(state=UserDetails.identified_from)
async def identified_from(message: types.Message, state: FSMContext):
    await state.update_data(identified_from=message.text)
    print((await state.get_data()))
    data = await state.get_data()
    values = list(data.values())
    values.extend([message.from_user.id, message.from_user.username])
    print(values)
    write.append(sheets="Users!A:I", values=values)
    await message.answer(f"Tabriklaymiz @{message.from_user.username}, Siz ro'yxatdan muvaffaqiyatli o'tdingiz")
    await message.answer("🥳")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dispatcher=disp, skip_updates=True)

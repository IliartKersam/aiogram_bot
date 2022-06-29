import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

API_TOKEN = '5031871873:AAE6gTk7vLBngVmHlpg-rxdDwFNk-DLcM6w'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

qwest = {
    'qwestion': 'Как только все "Боги" оказались на правой стороне реки, обсидиановая плита в дальнем' 
                'конце зала бесшумно выдвинулась вперёд и отошла в сторону. Вы вошли в открывшийся проход' 
                'и увидели однообразные ряды огромных обсидиановых плит в несколько метров высотой, прикосновение'
                'к которым вызывало появление на их поверхности постоянно меняющейся вязи из мелких и непонятных' 
                'белых значков. Что ж, если это действительно библиотека Ваа, то расшифровка их языка и поиск нужных'
                'сведений может затянуться на столетия. Но вас это, впрочем, не касается - свою часть работы вы сделали'
                'и можете лететь на <FromPlanet> за заслуженной наградой... \n \nПопрощавшись с учеными, при виде пресловутых'
                'плит забывшими обо всем на свете, вы вернулись на свой корабль.',
    'answers': {
        'answer_1' : 'Какой то ответ_1',
        'answer_2' : 'Какой то ответ_2',
        'answer_3' : 'Какой то ответ_3',
        'answer_4' : 'Какой то ответ_4',
    }          
}

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for value in qwest['answers'].values():
        keyboard.add(value)
    await message.answer(qwest['qwestion'], reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
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
                'и можете лететь на <FromPlanet> за заслуженной наградой... \n\nПопрощавшись с учеными, при виде пресловутых'
                'плит забывшими обо всем на свете, вы вернулись на свой корабль.',
    'answers': {
        'Какой то ответ_1' : {
            'qwestion' : 'новый вопрос_1',
            'answers': {
                'Какой то новый ответ_1' : 'Еще вопрос_1',
                'Какой то новый ответ_2' : 'Еще вопрос_2',
                'Какой то новый ответ_3' : 'Еще вопрос_3'
            }
            },
        'Какой то ответ_2' : {
            'qwestion' : 'новый вопрос_2',
            'answers': {
                'Какой то новый ответ_1' : 'Еще вопрос_1',
                'Какой то новый ответ_2' : 'Еще вопрос_2',
                'Какой то новый ответ_3' : 'Еще вопрос_3'
            }
            },
        'Какой то ответ_3' : {
            'qwestion' : 'новый вопрос_3',
            'answers': {
                'Какой то новый ответ_1' : 'Еще вопрос_1',
                'Какой то новый ответ_2' : 'Еще вопрос_2',
                'Какой то новый ответ_3' : 'Еще вопрос_3'
            }
            },
        'Какой то ответ_4' : {
            'qwestion' : 'новый вопрос_4',
            'answers': {
                'Какой то новый ответ_1' : 'Еще вопрос_1',
                'Какой то новый ответ_2' : 'Еще вопрос_2',
                'Какой то новый ответ_3' : 'Еще вопрос_3'
            }
            },
    }          
}

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for key in qwest.get('answers').keys():
        keyboard.add(key)
    await message.answer(qwest.get('qwestion'), reply_markup=keyboard)

@dp.message_handler()
async def any_text_message(message: types.Message):
    for key in qwest.get('answers').keys():
        if message.text == key:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            for keyb in qwest.get('answers').get(key).get('answers').keys():
                keyboard.add(keyb)
            await message.answer(qwest.get('answers').get(key).get('qwestion'), reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
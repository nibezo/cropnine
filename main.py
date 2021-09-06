import vktoken
import logging
from cropping import cropping, check_size
from PIL import Image
from vkwave.bots import SimpleLongPollBot

bot = SimpleLongPollBot(tokens=vktoken.token, group_id=206983513)
logging.basicConfig(level="DEBUG")


@bot.message_handler(bot.text_contains_filter(["Start", "Начало", "Начать", "Старт"]))
async def start(event: bot.SimpleBotEvent):
    await event.answer("Привет, я умею только одну вещь - обрезать фото на 9 равных частей. \n\n Убедись, "
                       "что присылаешь мне квадратное фото, я могу обрезать только такие. \n\n Присылай мне фото 📸")


if check_size(Image.open("image.png")):
    # call cropping function
    cropping("image.png")
else:
    print("Please, crop the image to a square.")

bot.run_forever()

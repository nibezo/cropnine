import vktoken
import logging
from cropping import cropping, check_size
from PIL import Image
from vkwave.bots import SimpleLongPollBot
from vkwave.api import API
from vkwave.bots.utils.uploaders import PhotoUploader
from vkwave.client import AIOHTTPClient
from vkwave.types.objects import MessagesMessageAttachmentType
import os.path
from os import path

# check path exist
if path.exists("../cropnine/cropped"):
    pass
else:
    os.mkdir("../cropnine/cropped")

bot = SimpleLongPollBot(tokens=vktoken.token, group_id=206983513)
logging.basicConfig(level="DEBUG")

api = API(clients=AIOHTTPClient(), tokens=vktoken.token)
uploader = PhotoUploader(api.get_context())


@bot.message_handler(bot.text_contains_filter(["Start", "Начало", "Начать", "Старт"]))
async def start(event: bot.SimpleBotEvent):
    await event.answer("Привет, я умею только одну вещь - обрезать фото на 9 равных частей. \n\n Убедись, "
                       "что присылаешь мне квадратное фото, я могу обрезать только такие. \n\n Присылай мне фото 📸")


@bot.message_handler(bot.attachment_type_filter(attachment_type=MessagesMessageAttachmentType.PHOTO))
async def image_cropping(event: bot.SimpleBotEvent):
    """If an user send an image, the program will work"""

    # save an image
    await event.attachments[0].save("image.jpg")

    # check image size
    if check_size(Image.open("image.jpg")):
        # call cropping function
        cropping("image.jpg")

        # send cropped images to an user
        big_attachment = await uploader.get_attachments_from_paths(
            peer_id=event.object.object.message.peer_id,
            file_paths=["cropped/im1.jpg", "cropped/im2.jpg", "cropped/im3.jpg", "cropped/im4.jpg",
                        "cropped/im5.jpg", "cropped/im6.jpg", "cropped/im7.jpg", "cropped/im8.jpg", "cropped/im9.jpg"]
        )
        await api.get_context().messages.send(
            user_id=event.object.object.message.peer_id, attachment=big_attachment, random_id=0
        )

    else:
        await event.answer("Пожалуйста, обрежь изображение. Я принимаю только квадратные!")

bot.run_forever()

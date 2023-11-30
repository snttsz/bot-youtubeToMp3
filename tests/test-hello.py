import pyrogram
from pyrogram import filters

@pyrogram.Client.on_message()
async def main(app: pyrogram.Client, message: pyrogram.types.Message):

    receivedMessage = message.text

    print(receivedMessage)

    person_name = message.from_user.first_name

    user_id = message.from_user.id

    # Answering a "how are you"
    if (receivedMessage == "how are you?"):

        messageToUser = "I'm great! How are you?"

        await app.send_message(user_id, messageToUser)

    # Getting the username and returning it with a Hello message
    else:

        messageToUser = "Hello {}!".format(person_name)

        await app.send_message(user_id, messageToUser)





       


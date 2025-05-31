import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType


TOKEN = 'YOUR_TOKEN'

vk = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)


def send_messages(chat_id, text):
    random_id = randint(1, 1000000)
    vk.method('messages.send', {'chat_id': chat_id, 'message': text, 'random_id': random_id})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text
                chat_id = event.chat.id
                bad_words = ['The list of forbidden words in your group']
                if msg in bad_words:
                    send_messages(chat_id, 'You used profanity')
                else:
                    send_messages(chat_id, msg)
                    
    if event.type == VkBotEventType.GROUP_JOIN:
        print(f'{event.obj.user_id} joined a group!')
        
    if event.type == VkBotEventType.MESSAGE_TYPING_STATE:
        print(f'Typing {event.obj.from_id} to {event.obj.to_id}')

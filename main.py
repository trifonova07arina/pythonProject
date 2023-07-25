token = "vk1.a._urxs2yegbH-ARp4BjAE1oOlfN2m6CxEmr4lxjaU6-OG7LZDDZUHhroCR6zGo690FVT-gyRonuqYO54uQyuLz-ovPbSLIpQ1NwRYkOKeFn8W76HsKUebTKGn54jxnHWxnp8Yl0dh3YHojDZUNpDIjZ9OOq1uTk1nJVXb7cLxvp_7TUn_HkD6KSFexLlfVs5s3L8LER1XSfww3peS8NnAAw"

import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
import random
from course import get_course
from wiki import get_wiki_article

def main():
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    hello_msg = 'Привет! Я бот Ксюха, я могу выполнять следующие команды:\n' \
                '-к - курс валют\n' \
                '-в "запрос" - статья из википедии по запросу'
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower()
            user_id = event.user_id
            random_id = random.randint(1, 9999999)
            print(f'{user_id}: {msg}')

            if msg[:2] == '-к':
                response = '{0} рублей за 1 евро\n' \
                           '{1} рублей за 10 юаней\n' \
                           '{2} рублей за 1 фунт\n'.format(get_course('R01239'),
                                                           get_course('R01375'),
                                                           get_course('R01035'))
            #if msg[:2] == '-к':
             #   valuta =msg[3:]
              #  response = get_course('valuta') + f'рублей за 1 {valuta}'

            elif msg.startswith('-в'):
                article = msg[3:]
                response = get_wiki_article(article)[:4096]

            else:
                response = hello_msg
            vk.messages.send(random_id=random_id, user_id=user_id, message=response)
main()
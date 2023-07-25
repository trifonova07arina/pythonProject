token = 'vk1.a.e48_Tq11W_0Y8veV2SB-uiaSRC_lq5vcMoTKyXJVmB-rvAZsB6xfguX932OZg8-oEfVaXlKeixj71Pd5Da73rhSTmyQ_kbtUI7hmSi5rVVorSsEAD-gWcdE3A5UA65mTYY6m_vDztUp91wSWAUMwtTsReh1y6SryYO2H2UT4Sh7MAsRxvBq5fuDppJ4C9WkyJJ_XO6FOKSUcHIllfEmFiA'
import vk_api
from random import choice, randint
import course
vk = vk_api.VkApi(token=token)
vk._auth_token()

answer = ['сам клоун',
                  'дратут',
                  'привет земляне от бородатой ксении',
                  'салам',
                  'отвернись!!',
                  'ответ загружается.....']

while True:
    messages = vk.method('messages.getConversations', {'count':20, 'filter':'unanswered'})
    if messages['count'] >= 1:

        id = messages['items'][0]['last_message']['from_id']
        # message_id = messages['items'][0]['last_message']['id']
        text = messages['items'][0]['last_message']['text']
        if text.lower() == 'курс':
            vk.method('messages.send', {'peer_id': id, 'random_id': randint(1, 1000), 'message':  course.get_course('R01235') + ' рублей за 1 доллар.'})
        else:
            vk.method('messages.send', {'peer_id':id, 'random_id':randint(1,1000), 'message': choice(answer)})

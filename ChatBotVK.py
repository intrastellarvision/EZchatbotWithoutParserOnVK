import vk_api
import requests
from datetime import datetime, date, time
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:		
        if event.text == 'Привет' or event.text == 'Как тебя зовут': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='Привет меня зовут Супер-бот'
                            )

        elif event.text == 'Что ты умеешь' or event.text == 'Для чего ты нужен': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''Могу рассказать о погоде("Погода"),
                            актуальные новости, подсказать время''')
        elif event.text == 'Ogon': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''BlaBlaBla''')

        elif event.text == 'Погода': 
            if event.from_user:
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message=''' ''')

        elif event.text == '1': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''''')

        elif event.text == '2': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''''')

        elif event.text == '3': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''''')

        elif event.text == '4': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''''')

        elif event.text == 'Меню': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''Меню:Бот,что ты умеешь?
                                             Как тебя зовут?
                                             Погода?
                                             Московское время?
                                             Интересные новости?''')

        elif event.text == 'Бот,что ты умеешь?': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''Могу рассказать о погоде(Погода?), интересные новости(Интересные новости?) или же Московское время(Московское время?)''')

        elif event.text == 'Как тебя зовут?': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''Меня зовут Чат-бот!''')

        elif event.text == 'Московское время?': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''15:00!''')

        elif event.text == 'Интересные новости?': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''''')

        elif event.text == 'Help': 
            if event.from_user: 
                vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''Help: Всегда вводите комманды с восклицательным знаком и с вопросительным знаком, с большой буквы!''')

                
        elif event.text == 'Время': 
            if event.from_user: 
                vk.messages.send(
                user_id=event.user_id,
                random_id=event.random_id,
                message='Московское время: ' +
                str(datetime.strptime("", "%d/%m/%y %H:%M"))
                )
        else:
            if event.from_user: 
                 vk.messages.send( 
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='''Неизвестная комманда! Введите меню! Или же введите Help''')
            

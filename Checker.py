import colorama
import requests
import time
import os

if not os.path.exists('username.txt'):
    print("-"*40)
    print(colorama.Fore.RED+'!ФАЙЛ КУДА БУДУТ НУЖНО ЗАПИСЫВАТЬ ТЕГИ СОЗДАН!',end="")
    print(colorama.Fore.RESET)
    username = open("username.txt", "w+")
    username.write("Mowaly")
if not os.path.isdir('Results'):
    print("-"*40)
    print(colorama.Fore.RED+'!ПАПКА КУДА БУДУТ ВЫВОДИТСЯ ОТВЕТЫ СОЗДАНА!',end="")
    print(colorama.Fore.RESET)
    os.system('mkdir Results')


available_file = open('Results/valid.txt', 'w',encoding='utf-8')
wrong_file = open('Results/wrong.txt', 'w',encoding='utf-8')
chats_file = open('Results/chat.txt','w',encoding='utf-8')
uncorrect_file = open('Results/uncorrect.txt','w',encoding='utf-8')
group_file = open('Results/group.txt','w',encoding='utf-8')
usernames_file = open('username.txt', 'r',encoding='utf-8')

if os.path.getsize('username.txt') ==  0:
    print("-"*40)
    print(colorama.Fore.RED+'Файл username.txt пуст!',end="")
    print(colorama.Fore.RESET)

url_list = list(sorted(set([line.strip() for line in usernames_file.readlines()])))

colorama.init()

print("-"*42)
print(colorama.Fore.WHITE + 'Checker '+colorama.Fore.CYAN+'Telegram'+colorama.Fore.WHITE+' Accounts | By '+colorama.Fore.RED+'Mowaly'+colorama.Fore.WHITE+'.')
print(f'Загруженно строк: '+colorama.Fore.BLACK+colorama.Back.WHITE+f'{len(url_list)}'+colorama.Fore.RESET+colorama.Back.RESET)
print("-"*42)

valid = 0 
uncorrect = 0
group = 0 
chat = 0 
wrong = 0

start_time = time.time()
for url in url_list: 
    urls = (f'https://t.me/{url}')
    NameWithTags = (f'@{url}')
    if len(url)<5 or len(url)>31:
        print(colorama.Fore.WHITE)
        print(f'@{url} не корректный тег.',end="")
        print(NameWithTags, file = uncorrect_file)
        uncorrect = uncorrect+1
    elif 'tgme_icon_user' in requests.get(urls).text:
        print(colorama.Fore.RED)
        print(f'@{url} не валид.',end="")
        wrong = wrong+1
        print(NameWithTags, file = wrong_file)
    elif '<div class="tgme_page_title">' in requests.get(urls).text:
        print(colorama.Fore.GREEN)
        print(f'@{url} валид.',end="")
        valid  = valid+1
        print(NameWithTags, file = available_file)
    elif 'tgme_page_context_link' in requests.get(urls).text:
        print(colorama.Fore.CYAN)
        print(f'@{url} группа.',end="")
        chat = chat+1
        print(NameWithTags, file = chats_file)
    elif 'View in Telegram' in requests.get(urls).text:
        print(colorama.Fore.YELLOW)
        print(f'@{url} чат.',end="")
        group = group+1
        print(NameWithTags, file = group_file)

FullCheck = (valid+uncorrect+group+chat+wrong)

print('')
print('')
print(colorama.Fore.WHITE+'-'*25)
print(colorama.Fore.RED+'Не валидных строк: '+str(wrong)+'.')
print(colorama.Fore.GREEN+'Валидых строк: '+str(valid+group+chat)+'.')
print(colorama.Fore.WHITE+'Не корректных строк: '+str(uncorrect)+'.')
print(colorama.Fore.WHITE+'-'*25)
print('Всего чекнуто строк:'+str(FullCheck)+'.')
print(colorama.Fore.WHITE+'-'*25,end='')
print(colorama.Fore.WHITE)
print(colorama.Back.RED)
print("Программа сделала свою работу за  %s секунд." % (time.time() - start_time),end=""+colorama.Back.RED)

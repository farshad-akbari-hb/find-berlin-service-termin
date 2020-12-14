import subprocess
import time
import pync
from datetime import datetime
import logging

import bs4
import requests

# url = 'http://service.berlin.de/terminvereinbarung/termin/tag.php?termin=1&dienstleister%5B%5D=122210&dienstleister%5B%5D=122217&dienstleister%5B%5D=122219&dienstleister%5B%5D=122227&dienstleister%5B%5D=122231&dienstleister%5B%5D=122238&dienstleister%5B%5D=122243&dienstleister%5B%5D=122252&dienstleister%5B%5D=122260&dienstleister%5B%5D=122262&dienstleister%5B%5D=122254&dienstleister%5B%5D=122271&dienstleister%5B%5D=122273&dienstleister%5B%5D=122277&dienstleister%5B%5D=122280&dienstleister%5B%5D=122282&dienstleister%5B%5D=122284&dienstleister%5B%5D=122291&dienstleister%5B%5D=122285&dienstleister%5B%5D=122286&dienstleister%5B%5D=122296&dienstleister%5B%5D=150230&dienstleister%5B%5D=122301&dienstleister%5B%5D=122297&dienstleister%5B%5D=122294&dienstleister%5B%5D=122312&dienstleister%5B%5D=122314&dienstleister%5B%5D=122304&dienstleister%5B%5D=122311&dienstleister%5B%5D=122309&dienstleister%5B%5D=317869&dienstleister%5B%5D=324433&dienstleister%5B%5D=325341&dienstleister%5B%5D=324434&dienstleister%5B%5D=324435&dienstleister%5B%5D=122281&dienstleister%5B%5D=324414&dienstleister%5B%5D=122283&dienstleister%5B%5D=122279&dienstleister%5B%5D=122276&dienstleister%5B%5D=122274&dienstleister%5B%5D=122267&dienstleister%5B%5D=122246&dienstleister%5B%5D=122251&dienstleister%5B%5D=122257&dienstleister%5B%5D=122208&dienstleister%5B%5D=122226&anliegen%5B%5D=120686&herkunft=%2Fterminvereinbarung%2F'
url = 'https://service.berlin.de/terminvereinbarung/termin/tag.php?termin=1&anliegen[]=327537&dienstleisterlist=122210,122217,122219,122227,122231,122238,122243,122252,122260,122262,122254,122271,122273,122277,122280,122282,122284,327539,122291,122285,122286,122296,150230,122301,122297,122294,122312,122304,122311,122309,317869,324434,122281,122279,122276,122274,122267,122246,122251,122257,122208,122226&herkunft=http%3A%2F%2Fservice.berlin.de%2Fdienstleistung%2F327537%2F'
headers = {
    'User-Agent': 'Mozilla/5.0',
    'refer':'www.google.com'
}

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    response = requests.get(url, headers=headers)
    body = bs4.BeautifulSoup(response.content,features="html.parser")
    try:
        links = body.select('.calendar-month-table')[0].select('td.buchbar a')
    except:
        print('Exception fired at: ',current_time)
        time.sleep(60)
    print(len(links), 'found','at time: ',current_time)
    if links:
        args = ['osascript', '-e', 'display notification',
                'Found an appoitment', 'check the logs']
        days = ''
        print('\n')

        for link in links[:10]:
            if 'href' in link.attrs:
                day = int(link.text.strip())
                final_link = '{}: http://service.berlin.de{} '.format(day, link.attrs['href'])
                print(final_link)
                pync.notify( final_link)

            
    time.sleep(200)
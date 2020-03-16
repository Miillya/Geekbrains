import requests
import json
import time
import re

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.132 Safari/537.36',
           }
URL = 'https://5ka.ru/api/v2/special_offers/'
CAT_URL = 'https://5ka.ru/api/v2/categories/'


def x5ka(url, params=None):
    result = []
    while url:
        response = requests.get(url, headers=headers, params=params) if params else requests.get(url, headers=headers)
        params = None
        data = response.json()
        if isinstance(data, dict):
            result.extend(data.get('results'))
            url = data.get('next')
        elif isinstance(data, list):
            return data
        else:
            print(f'Ошибка данных')
            return None
        time.sleep(1)
    return result


if __name__ == '__main__':
    categories = x5ka(CAT_URL)
    for item in categories:
        parameters = {'records_per_page': 20, 'categories': item['parent_group_code']}
        special_offers = x5ka(URL, parameters)
        re_name = re.sub(r'[#%!@*/\"\n]', '', item['parent_group_name'])
        if len(special_offers) > 0:
            with open(f'{re_name}.json', 'w') as file:
                file.write(json.dumps(special_offers))
                print(f'Файл {re_name}.json записан')

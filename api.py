from requests.cookies import cookiejar_from_dict
from typing import Generator

import requests
import re
import base64
import json
import time


class FacebookAPI(requests.Session):
    cookie = None
    user_agent = None

    def __init__(self, cookie: str, user_agent: str):
        super().__init__()

        self.cookie = cookie.strip()
        self.user_agent = user_agent

        self.cookies = cookiejar_from_dict({key: value for key, value in self.parse_cookie_string()})
        self.headers.update({'User-Agent': self.user_agent})

    def get_pages(self) -> list:
        dtsg = self.get_dtsg('https://www.facebook.com/')
        variables = {
            'count': 10,
            'filter_ids': None,
            'scale': 1,
            'search': None
        }
        headers = {
            'Sec-Fetch-Site': 'same-origin',
        }

        has_next_page = True
        pages = []

        while has_next_page:
            start_time = time.time()

            data = {
                'variables': json.dumps(variables),
                'fb_dtsg': dtsg,
                'doc_id': '6394626757239207'
            }
            response = self.post('https://www.facebook.com/api/graphql/', data, headers=headers)
            data = response.json()
            profiles = data['data']['viewer']['actor']['profiles']
            page_info = profiles['page_info']
            has_next_page = page_info['has_next_page']

            if has_next_page:
                variables.update({'cursor': page_info['end_cursor']})

            for item in profiles['edges']:
                profile = item['node']['profile']
                page_id = profile['id']
                page_name = profile['name']

                print(page_id, page_name)

                pages.append([page_id, page_name])

            end_time = time.time() + (time.time() - start_time)
            while True:
                if time.time() > end_time:
                    break
                
                remainning_time = end_time - time.time()
                print(f'Se tiep tuc sau: {remainning_time}')

                time.sleep(1)

        return pages

    def get_dtsg(self, url: str) -> str:
        response = self.get(url)
        dtsg = re.findall('\["DTSGInitialData",\[],{"token":"(.*?)"},\d+]', response.text)
        if not dtsg:
            return None
        return dtsg[-1]

    def parse_cookie_string(self) -> Generator:
        cookie_pairs = self.cookie.split(';')
        for item in cookie_pairs:
            if not item:
                continue
            yield item.strip().split('=')


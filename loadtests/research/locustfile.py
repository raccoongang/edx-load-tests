import random

from locust import  *
import requests

URL = 'https://lms-lakeside-stage.raccoongang.com'


class Search(TaskSet):

    def value_1(self):
        file = open('string_value.txt', 'r')
        fileList = []
        for line in file.readlines():
            fileList.append(line.replace('\r\n', ''))
        return random.choice(fileList)

    def value_2(self):
        file = open('categories.txt', 'r')
        fileList = []
        for line in file.readlines():
            fileList.append(line.replace('\r\n', ''))
        return random.choice(fileList)

    def get_csrftoken(self):
        csrftoken = None
        client = requests.session()
        client.get(URL, headers= {'referer':'https://lms-lakeside-stage.raccoongang.com/'})
        if 'csrftoken' in client.cookies:
            csrftoken = client.cookies['csrftoken']
        else:
            csrftoken = client.cookies['csrf']
        return csrftoken

    @task(1)
    def test_search_1(self):
        csrftoken = self.get_csrftoken()
        self.client.post('/search/course_discovery/',
                        {'search_string': self.value_1, 'page_size': '100', 'page_index': '0'},
                        headers ={'x-csrftoken': csrftoken,
                                  'referer': 'https://lms-lakeside-stage.raccoongang.com/',
                                  'cookie': 'csrftoken=' + csrftoken
                        },
                        name='Search 1'
        )

    @task(1)
    def test_search_2(self):
        csrftoken = self.get_csrftoken()
        self.client.post('/search/course_discovery/',
                         {'search_string': '', 'page_size': '100', 'page_index': '0', 'category': self.value_2},
                         headers={'x-csrftoken': csrftoken,
                                  'referer': 'https://lms-lakeside-stage.raccoongang.com/',
                                  'cookie': 'csrftoken=' + csrftoken
                                  },
                         name='Search 2'
                         )

class WebsiteUser(HttpLocust):
    task_set = Search
    min_wait = 5
    max_wait = 5
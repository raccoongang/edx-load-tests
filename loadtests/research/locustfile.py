import os

import requests
from locust.core import TaskSet, task, HttpLocust


class SearchOnMainPage(TaskSet):
    """
    Load test for searching on main page:
    1. Search by some text
    2. Search by some Categories
    """
    def on_start(self):
        self.fileToSearchBySomeText = self.getValueToSearchBySomeText()
        self.fileToSearchByCategories = self.getValueToSearchByCategories()
        self.csrftoken = self.get_csrftoken()

    def getValueToSearchBySomeText(self):
        with open(os.path.realpath('.') + "/loadtests/research/string_value.txt") as file:
            return file.read()

    def getValueToSearchByCategories(self):
        with open(os.path.realpath('.') + "/loadtests/research/categories.txt") as file:
            return file.read()

    def get_csrftoken(self):
        client = requests.session()
        client.get(self.locust.host, headers={'referer': self.locust.host})
        if 'csrftoken' in client.cookies:
            csrftoken = client.cookies['csrftoken']
        else:
            csrftoken = client.cookies['csrf']
        return csrftoken

    def _create_post_request(self, name, **kwargs):
        post_req = self.client.post(
            '/search/course_discovery/',
            kwargs,
            headers={
                'x-csrftoken': self.csrftoken,
                'referer': self.locust.host,
                'cookie': 'csrftoken=' + self.csrftoken,
            },
            name=name
        )
        return post_req

    @task(1)
    def test_search_1(self):
        data = {'search_string': self.fileToSearchBySomeText, 'page_size': '100', 'page_index': '0'}
        response = self._create_post_request(
            'Search 1',
            **data
        )

    @task(2)
    def test_search_2(self):
        data = {'search_string': '', 'page_size': '100', 'page_index': '0', 'category': self.fileToSearchByCategories}
        response = self._create_post_request(
            'Search 2',
            **data
        )


class WebsiteUser(HttpLocust):
    task_set = SearchOnMainPage
    min_wait = 5
    max_wait = 25

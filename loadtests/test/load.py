import requests
import re
import csv
from os import getcwd


def LoginViaSSO(username, password):
    session = requests.session()

    #go to ytp portal
    portal = session.get('https://courses.youngthinker.org/auth/login/drupal-oauth2/?auth_entry=login&next=%2Fcourses', allow_redirects = True)

    #get token from from_text
    pattern = '<input type="hidden" name="form_build_id" value=[^>]+>'
    result = re.search(pattern, portal.text)
    result_str = str((result.group(0)))
    token = ''.join(result_str.split('"')[-2:-1])



    #put token and perform post creds
    data = {'name': username, 'pass': password, 'form_build_id': token, 'form_id': 'user_login', 'op': 'Sign+In'}


    #data = 'name=test&pass=test&form_build_id={}&form_id=user_login&op=Sign+In'.format(token)
    portal_post = session.post('https://youngthinker.org/en/user/login?destination=oauth2/authorize', data=data)

    #get oauth2 authorized to get the code
    get_edx = session.get('https://en-courses.youngthinker.org/auth/login/drupal-oauth2/?auth_entry=login&next=%2Fcourses')


    ytp_edx = session.get('https://en-courses.youngthinker.org/courses')
    print (session.cookies)



def extract_creds(file):

    with open(file, 'r+') as users_csv:
        users_reader = csv.reader(users_csv)
        list_creds = []
        for row in users_reader:
            creds_edit = row[0].split(';')
            list_creds.append(creds_edit)
        return list_creds




def check_login():
    list_of_credentials = extract_creds('users_txt.txt')
    for i in range(0, len(list_of_credentials)):
        username = list_of_credentials[i][0]
        password = list_of_credentials[i][1]
        SSO_Login = LoginViaSSO(username, password)




a = check_login()
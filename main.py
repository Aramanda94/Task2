import requests
import pathlib
import yadisk
import os
from pathlib import Path


class Yan_Disk:

    def __init__(self, _token: str):
        self.token = _token

    def create_folder(self, path):
        rez_create_folder = requests.put(f'{URL}?path={path}', headers=headers)
        if rez_create_folder.status_code == 201:
            print(f'Папка {path} на Я-диске создана')
        elif rez_create_folder.status_code == 409:
            print(f'Папка {path} на Я-диске уже существует')

    def upload_file(self, loadfile, savefile, replace=False):

        res_url = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
        with open(loadfile, 'rb') as f:
            try:
                res_load_file = requests.put(res_url['href'], files={'file': f})
                if res_load_file.status_code == 201:
                    print(f'Загрузка файла {f.name} завершена')
            except KeyError:
                print(f'{res_url=}')

if __name__ == '__main__':
    token = ''

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'

    uploader = Yan_Disk(token)
    path_f = r'C:/Users/Pavel/PycharmProjects/python_yandisk/SECNT-8  Преобразование сетевых адресов (NAT).pdf'
    name = path_f.split('/')[-1]
    path_p = 'python_yandisk'

    uploader.create_folder('python_yandisk')
    uploader.upload_file(path_f, f'{path_p}/{name}')

from pprint import pprint

import requests

token = "y0_AQAAAAAASRvfAADLWwAAAADLFaZrcj2WwkIaQ2qcF2c3urTXV10ViL8"
# url_upload = "https://cloud-api.yandex.net/v1/disk/resources/upload"
# headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
url = "/home/vitaly/Документы/Нетология/HomeWorks/Hello.txt"


# f = open("/home/vitaly/Документы/Нетология/HomeWorks/Hello.txt", "r", encoding='UTF-8')
# print(f.read())
# f.close()

# r = requests.get(url_query, headers=headers)
# print(r)


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def headers(self):
        return {
            'Content-Type': 'application/json', 'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload_link(self, disk_file_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url_upload = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        resp = requests.get(url_upload, headers=headers, params=params)
        pprint(resp.json())
        return resp.json()

        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

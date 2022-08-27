from pprint import pprint

import requests

# filename = '/home/vitaly/Изображения/2face.jpg'


class YaUploader:
    def __init__(self, token):
        self.token = token

    def headers(self):
        return {
            'Content-Type': 'application/json', 'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload_link(self, disk_file_path):
        url_upload = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        resp = requests.get(url_upload, headers=headers, params=params)
        pprint(resp.json())
        return resp.json()

    def upload_file(self, disk_file_path, filename):
        href = self.upload_link(disk_file_path=disk_file_path).get("href", "")
        resp = requests.put(href, data=open(filename, 'rb'))
        resp.raise_for_status()
        if resp.raise_for_status() == None:
            print("File uploaded to disk")


if __name__ == '__main__':
    yandex_file = YaUploader(token=token)
    yandex_file.upload_file("2face.jpg", filename)

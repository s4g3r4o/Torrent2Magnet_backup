import os
import sys
import hashlib
import requests
import bencodepy
from binascii import hexlify
from fake_useragent import UserAgent


def magnet_to_torrent(magnet):
    headers = {'User-Agent': UserAgent().random}

    if magnet.startswith('magnet:'):
        magnet = magnet[20:60]

    torrent_name = f'{magnet}.torrent'
    folder_path = os.path.join(os.getcwd(), 'torrents')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, torrent_name)

    url = f'http://itorrents.org/torrent/{torrent_name}'
    response = requests.get(url, headers=headers)

    with open(file_path, 'wb') as f:
        f.write(response.content)

    return file_path


def torrent_to_magnet(torrent_file_path):
    with open(torrent_file_path, 'rb') as f:
        torrent_data = f.read()

    metadata = bencodepy.decode(torrent_data)
    info_hash = hashlib.sha1(bencodepy.encode(metadata[b'info'])).digest()
    hex_hash = hexlify(info_hash).decode('utf-8')

    magnet_uri = 'magnet:?xt=urn:btih:' + hex_hash

    return magnet_uri

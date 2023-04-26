import os
import time
from utils import magnet_to_torrent, torrent_to_magnet

def main():
    check = input(
        '\033[94;1m[1]Magnet to Torrent\n[2]Torrent to Magnet\n\n\033[96;1mSelect an action:\033[0m ')

    if check == '1':
        try:
            magnet = input('\033[96;1mPaste Magnet Link:\033[0m ')
            if magnet.startswith('magnet:'):
                main = magnet_to_torrent(magnet=magnet)
                print(f'\n\033[92;1mYour Torrent file here ↓\033[0m\n{main}')
            else:
                print('\033[91;1mEnter the correct magnet link!!\033[0m')
        except:
            print('\033[91;1mYour magnet is not correct!!\033[0m')

    elif check == '2':
        try:
            print(
                '\033[93;1mEXAMPLE: C:\\Users\\User\\torrent2magnet\\torrents\\Tor.torrent\033[0m')
            torrent = input('\033[96;1mPaste Torrent file link:\033[0m ')
            if torrent.endswith('.torrent'):
                main = torrent_to_magnet(torrent_file_path=torrent)
                print(f'\033[92;1mYour Magnet ↓\033[0m\n{main}')
            else:
                print('\033[91;1mEnter the correct torrent file!!\033[0m')
        except:
            print('\033[91;1mYour file may be empty or not working!!\033[0m')
    else:
        print('\033[93;1mCheck correct action\033[0m')


main()

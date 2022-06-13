import downloader
import db
import telebot
import info
import time
import glob
import os.path
import os

bot = telebot.TeleBot(info.bot_token)

def main():
    try:
        url = db.get_url()
        print (url)
        downloader.download_by_url(url)
        tgid = db.get_tgid_by_url(url)
        db.delete_url_by_tgid(tgid, url)
        bot.send_message(tgid,'Видео скачано')
        bot.send_video(tgid, video=open(f'{get_title_in_folder()}.mp4', 'rb'), supports_streaming=True)
        os.remove(f'{get_title_in_folder()}.mp4')
    except Exception as ex :
        print (f'ERROR {ex}')

def get_title_in_folder():
    try:
        dir = '.'
        files = glob.glob(os.path.join(dir, '*.mp4'))[0][2:-4]
        print (files)   
        return files
    except Exception as ex :
        print (f'ERROR {ex}')
        

while True:
    try:
        main()
        time.sleep(20)
    except Exception as ex :
        print (f'ERROR {ex}')    



import json
import requests
import urllib
import time

token= "462576274:AAGvI1uMdnuL_CPNR60-xI1BPkIlb99ql0c"
URL="https://api.telegram.org/bot{}/".format(token)

def get_url(url):
    R=requests.get(url)
    content = R.content.decode("utf8")
    return content
def get_json_from_url(url):
    content=get_url(url)
    js=json.loads(content)
    return js
def get_updates(offset=None):
    url=URL+ "getupdates?timeout=100"
    if offset:
        url+="&offset={}".format(offset)
    js=get_json_from_url(url)
    return js
def send_message(text,chat_id):
    text=urllib.parse.quote_plus(text)
    url=URL+"sendmessage?text={}&chat_id={}".format(text,chat_id)
    get_url(url)
def get_last_update_id(updates):
    update_ids=[]
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)
def echo_all(updates):
    for update in updates["result"]:
        try:
            text=update["message"]["text"]
            chat=update["message"]["chat"]["id"]
            send_message(text,chat)
        except Exception as e:
            print(e)
def main():
    last_update_id=None
    while True:
        updates=get_updates(last_update_id)
        if len(updates["result"])>0:
            last_update_id=get_last_update_id(updates)+1
            echo_all(updates)
        time.sleep(0.5)

if __name__=='__main__':
    main()
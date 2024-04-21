import requests
from tkinter import *

def send_message_to_telegram_bot(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Error sending message: Status Code: {response.status_code}")

def start():
    message_to_send = f"nam={pyaz1.get()} \n yozer={pyam2.get()}"
    send_message_to_telegram_bot(telegram_bot_token, chat_id, message_to_send)

tk = Tk()
Label(tk, text="nam", font=20).pack()
pyaz1 = Entry(tk)
pyaz1.pack()
Label(tk, text="yozer", font=20).pack()
pyam2 = Entry(tk)
pyam2.pack()

telegram_bot_token = "7137018261:AAFGKTJMM_zlstifux43lz8VNtPTVRhX7DY"
chat_id = "6894281096"

Button(tk, text="start", width=15, height=3, command=start).pack()

tk.mainloop()
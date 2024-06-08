import tkinter as tk
from tkinter import scrolledtext
import re
import random

# İlgili cevaplar ve örnekler
pairs = [
    [
        r"merhaba|selam|hey",
        ["Merhaba!", "Selam!", "Hey! Nasıl yardımcı olabilirim?"],
    ],
    [
        r"nasılsın|naber",
        ["Ben bir yapay zeka botuyum, sizinle konuşmaktan mutluluk duyuyorum.",],
    ],
    [
        r"senin adın ne?",
        ["Benim adım ChatBot ve sizinle konuşmak için buradayım.",],
    ],
    [
        r"quit|exit",
        ["Görüşürüz, umarım tekrar görüşürüz!"],
    ],
]

# ChatBot'u oluştur
def chat_bot():
    chatbot_response.config(state=tk.NORMAL)
    chatbot_response.insert(tk.END, "ChatBot: Merhaba! Nasıl yardımcı olabilirim?\n")
    chatbot_response.config(state=tk.DISABLED)

def send_message():
    user_input = user_message.get()
    chatbot_response.config(state=tk.NORMAL)
    chatbot_response.insert(tk.END, f"Sen: {user_input}\n")
    for pattern, responses in pairs:
        if re.match(pattern, user_input):
            response = random.choice(responses)
            chatbot_response.insert(tk.END, f"ChatBot: {response}\n")
            break
    else:
        chatbot_response.insert(tk.END, "ChatBot: Üzgünüm, bu konuda size yardımcı olamıyorum.\n")
    chatbot_response.config(state=tk.DISABLED)
    user_message.delete(0, tk.END)

# Tkinter uygulamasını oluştur
root = tk.Tk()
root.title("ChatBot")

# Sohbet penceresi
chatbot_response = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD, font=("Helvetica", 10), bg="lightgray")
chatbot_response.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Kullanıcı girişi
user_message = tk.Entry(root, width=50, font=("Helvetica", 10))
user_message.grid(row=1, column=0, padx=10, pady=10)

# Gönder düğmesi
send_button = tk.Button(root, text="Gönder", command=send_message, bg="lightblue", font=("Helvetica", 10, "bold"))
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# ChatBot'u başlat
chat_bot()

# GUI'yi çalıştır
root.mainloop()

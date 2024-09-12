


import pandas as pd 
import nltk 
from nltk.tokenize import word_tokenize

# TDK verilerini yükle
df = pd.read_csv('tdk_word_meaning_data.csv')

# Kullanıcıdan gelen kelimeyi ve cümleyi analiz etme fonksiyonu
def analyze_sentence(sentence):
    tokens = word_tokenize(sentence.lower())
    
    if "kelime" in tokens or "anlam" in tokens:
        # Kullanıcının kelime anlamı sorduğunu anla
        return "kelime_anlam"
    else:
        return "bilinmiyor"

# Chatbot'a TDK verilerini entegre edelim
def chatbot():
    print("Merhaba! Ben senin gelişmiş chatbot'unum.")
    
    while True:
        user_input = input("Sen: ")
        
        # Kullanıcı girdisini analiz et
        analysis = analyze_sentence(user_input)
        
        if analysis == "kelime_anlam":
            # Kullanıcının kelime sorması durumunda
            kelime = input("Hangi kelimenin anlamını öğrenmek istiyorsunuz? ")
            if kelime in df['madde'].values:
                anlam = df.loc[df['madde'] == kelime, 'anlam'].values[0]
                print(f"Chatbot: {kelime} kelimesinin anlamı: {anlam}")
            else:
                print(f"Chatbot: {kelime} kelimesini TDK'da bulamadım.")
        
        elif user_input.lower() == "çık":
            print("Chatbot: Görüşürüz!")
            break
        
        else:
            print("Chatbot: Bu konuda yardımcı olamıyorum.")
import random

# Rastgele cevaplar oluştur
greeting_responses = ["Merhaba!", "Selam!", "Merhaba, size nasıl yardımcı olabilirim?"]

def chatbot():
    print("Merhaba! Ben senin chatbot'unum.")
    
    while True:
        user_input = input("Sen: ")
        
        if user_input.lower() in ["merhaba", "selam", "hey"]:
            print(f"Chatbot: {random.choice(greeting_responses)}")
        
        elif user_input.lower() == "nasılsın":
            print("Chatbot: Ben bir botum, her zaman iyiyim!")
        
        elif user_input.lower() == "çık":
            print("Chatbot: Görüşürüz!")
            break
        
        else:
            print("Chatbot: Bu konuda yardımcı olamıyorum.")

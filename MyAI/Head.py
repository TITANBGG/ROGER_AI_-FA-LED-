# Gerekli kütüphaneleri içe aktaralım
import pandas as pd  # Verilerle çalışmak için pandas kütüphanesini kullanacağız
import nltk  # Doğal dil işleme (NLP) için gerekli kütüphane
nltk.download('punkt')
from nltk.corpus import stopwords  # Stop words (gereksiz kelimeler) listesini almak için
nltk.download('stopwords')  # Stop words'leri indirir
from nltk.tokenize import word_tokenize  # Metni kelimelere bölmek için tokenize aracı
import matplotlib.pyplot as plt  # Verileri görselleştirmek için matplotlib
from wordcloud import WordCloud  # Kelime bulutu oluşturmak için WordCloud kütüphanesi

# CSV dosyasını pandas ile yüklüyoruz
df = pd.read_csv('netflix_data.csv')

# 'description' sütunundaki tüm verileri alıyoruz ve boş olanları (NaN) atıyoruz
# Bu sütundaki metinleri kelime analizine tabi tutacağız
descriptions = df['description'].dropna()

# Küçük harfe çevirme ve tokenize işlemi yapabilmek için NLTK kütüphanesinden gerekli verileri indiriyoruz
# 'punkt' paketi, cümleleri ve kelimeleri tokenlere (parçalara) ayırabilmek için gerekli
nltk.download('punkt')
# 'stopwords' ise gereksiz kelimeler listesini içerir (örneğin: 'the', 'is', 'and' gibi)
nltk.download('stopwords')

# İngilizce stop words (gereksiz kelimeler) listesini alıyoruz
stop_words = set(stopwords.words('english'))

# Metni işlemek için bir fonksiyon oluşturuyoruz
def process_text(text):
    # Metni önce küçük harflere çeviriyoruz (örneğin: 'THE' -> 'the')
    # Ardından word_tokenize ile kelimelere ayırıyoruz (örn: 'This is a test.' -> ['This', 'is', 'a', 'test'])
    tokens = word_tokenize(text.lower())
    
    # Stop words ve alfanümerik olmayan karakterleri (noktalama işaretleri gibi) filtreliyoruz
    # Yani yalnızca harf ve rakam içeren kelimeler kalacak (örn: 'test')
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    
    # İşlenmiş kelimeleri geri döndürüyoruz
    return filtered_tokens

# Tüm 'description' sütunundaki metinleri tek tek işleyeceğiz
# Kelimeleri birleştirip bir listeye atayacağız
all_words = []
for description in descriptions:
    # Her bir açıklamayı işleyip kelimelerini all_words listesine ekliyoruz
    all_words.extend(process_text(description))

# İşlenmiş tüm kelimeleri aldıktan sonra, frekansını hesaplıyoruz
# nltk.FreqDist fonksiyonu her kelimenin kaç kez geçtiğini bulur
word_freq = nltk.FreqDist(all_words)

# En sık kullanılan 10 kelimeyi ekrana yazdırıyoruz
print(word_freq.most_common(10))

# İsteğe bağlı olarak kelime bulutu oluşturuyoruz
# Kelime bulutu, kelimelerin sıklığını görsel bir şekilde gösterir
wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_freq)

# Kelime bulutunu görselleştiriyoruz
plt.figure(figsize=(10, 5))  # Görüntü boyutunu belirliyoruz (10x5 inç)
plt.imshow(wordcloud, interpolation='bilinear')  # Kelime bulutunu ekranda göster
plt.axis('off')  # Eksenleri kapatıyoruz çünkü kelime bulutunda eksene gerek yok
plt.show()  # Kelime bulutunu ekranda göster

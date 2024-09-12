#N-gram'lar, ardışık kelime çiftleri ya da üçlüleri gibi 
#gruplar oluşturarak metni analiz etmeye yarar. Örneğin, 
#"machine learning" bir 2-gram'dır (bigram).
from nltk import ngrams


# 2- gram(bigram) ouşturmak için bir fonksiyon yazıyoruz
def get_bigrams(text):
    ## Küçük harfe çevirip tokenize ediyoruz
    tokens = word_tokenize(text.lower())
 # 2-gram oluşturuyoruz
    bigrams = list(ngrams(tokens, 2))

    return bigrams


# Tüm description sütunundaki bigram'ları birleştiriyoruz
all_bigrams = []

for description in description:
    all_bigrams.extend(get_bigrams(description))

# Bigram frekanslarını hesaplıyoruz
bigram_freq = nltk.FreqDist(all_bigrams)

# En sık kullanılan 10 bigramı yazdırıyoruz
print(bigram_freq.most_common(10))


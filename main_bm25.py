import math
import string
import nltk
nltk.download('omw-1.4')
from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer, PorterStemmer
def preprocess(input_text):
    # Create a stop word list for English
    stop_words = ["n't", 'was', "couldn't", "hadn't", "aren't", "shouldn't", "couldn't", "hasn't", "that'll", "you've", "mightn't", "wouldn't", "doesn't", "wasn't", "haven't", "mustn'", 'mightn', 'shan', "needn't", 'that', "she's", "shouldn't", 'now', "weren't", "don't", "mustn't", "hadn't", "weren't", "won't", "you'd", "needn't", "aren't", "wasn'", "didn't", 'didn', "it's", "isn't", "hasn'", 'wouldn', "doesn'", 'to', 'how', 'we', 'not', 'where', 'he', 'itself', 'can', 'nor', 'few', 'had', 'here', 'them', 'hers', 'this', 'under', 'all', 'same', 'by', 'yourself', 'other', 'out', 'my', 'about', 'will', 'some', 'herself', 'as', 'these', 'do', 'very', 'from', 'then', 'yourselves', 'above', 'most', 'it', 'any', 'only', 'ma', 'for', 'no', 'you', 'between', 'such', 'your', 'ain', 'in', 'being', 'up', 'because', 'him', 'more', 'while', 'were', 'into', 'haven', 'his', 'both', 'having', 'myself', 'is', 'than', 'ourselves', 'but', "should've", 'when', 'hadn', 'himself', "you'll", 'its', 'until', 'are', 'and', 'further', 'if', 'off', 'won', 'who', 'i', 'has', 'during', 'so', 'isn', "you're", 'have', 'again', 'does', 'below', 'theirs', 'ours', 'the', 'through', 'own', 'those', 'too', 'be', 'on', 'doing', 'don', 'me', 'should', 'down', 'which', 'after', 're', 'once', 'their', 'against', 'whom', 'they', 'what', 'an', 'each', 'at', 'themselves', 'been', "shan't", 'she', 'did', 'with', 'our', 'there', 'just', 'over', 'why', 'll', 'before', 'of', 'her', 'or', 'yours', 've', 'am', 'y', "'s", 'o', 'm', 'd', "a"]
   
    tokenizing_sentence = [word for word in word_tokenize(input_text.lower()) if word not in stop_words]
    # print(tokenizing_sentence)
    porter = PorterStemmer()    
    wnl = WordNetLemmatizer()    
    
    # NEW FORMULA WITH PORTER AND WNL
    new_sentence = []
    i = 0
    while(i<len(tokenizing_sentence)):
        if(str(tokenizing_sentence[i]).endswith('e')):
            lemmatized_word_e = wnl.lemmatize(str(tokenizing_sentence[i]))
            new_sentence.append(lemmatized_word_e)
            # print(lemmatized_word)
        elif(str(tokenizing_sentence[i]).endswith('s')):
            lemmatized_word_s = wnl.lemmatize(str(tokenizing_sentence[i]))
            new_sentence.append(lemmatized_word_s)
            # print(lemmatized_word_s)
        elif(str(tokenizing_sentence[i]).endswith('y')):
            new_sentence.append(str(tokenizing_sentence[i]))
        elif(str(tokenizing_sentence[i]).endswith('ed')):
            lemmatized_word_ed = wnl.lemmatize(str(tokenizing_sentence[i]), pos='v')
            new_sentence.append(lemmatized_word_ed)
            # print(lemmatized_word_ed)
        else:
            stemmed_words = porter.stem(str(tokenizing_sentence[i]))
            new_sentence.append(stemmed_words)
            # print(stemmed_words)
        i+=1
    # tokens_without_punct
    without_punctuation = [token for token in new_sentence if token not in string.punctuation]
    final_sentence = ' '.join(without_punctuation)
    return final_sentence

def calculate_bm25(query, document, corpus, k1, b):
    score = 0.0
    N = len(corpus)  # Jumlah total dokumen dalam koleksi
    avgdl = calculate_avgdl(corpus)  # Panjang rata-rata dokumen dalam koleksi
    
    # Menghitung IDF untuk setiap term dalam query
    idf_scores = {}
    for term in query.split():
        n = sum(1 for doc in corpus if term in doc)  # Jumlah dokumen yang mengandung term
        idf_scores[term] = math.log((N - n + 0.5) / (n + 0.5))
    
    # Menghitung skor BM25
    for term in query.split():
        if term in document:
            f = document.count(term)  # Frekuensi kemunculan term dalam dokumen
            dl = len(document)  # Panjang dokumen dalam jumlah term
            score += idf_scores[term] * (f * (k1 + 1)) / (f + k1 * (1 - b + b * (dl / avgdl)))
    
    return score

def calculate_avgdl(corpus):
    total_length = sum(len(doc) for doc in corpus)
    return total_length / len(corpus)

# Contoh penggunaan

# Dokumen dalam koleksi
corpus = [
    "Blue is my favorite color, i can use this everytime i see blue",
    "Sky is blue and sea is blue, i can see blue everywhere",
    "sky is blue and sky is beautiful, i can see blue everywhere",
]

# Parameter BM25
k1 = 1.2
b = 0.75

# Contoh query
query1 = "blue favorite color"
query2 = "blue beautiful sky"
query3 = "blue sky everywhere"

# Melakukan preprocessing pada dokumen dalam koleksi
corpus = [preprocess(doc) for doc in corpus]

# Melakukan preprocessing pada query
query1 = preprocess(query1)
# query2 = preprocess(query2)
# query3 = preprocess(query3)

# Menghitung skor BM25 untuk setiap dokumen
scores = []
for i, doc in enumerate(corpus):
    doc_score = calculate_bm25(query1, doc, corpus, k1, b)
    scores.append((i+1, doc_score))  # Menyimpan nomor dokumen dan skor
    
# Melakukan perangkingan berdasarkan skor
ranked_scores = sorted(scores, key=lambda x: x[1],  reverse=True)

# Menampilkan hasil perangkingan
for rank, (doc_id, score) in enumerate(ranked_scores):
    print(f"Peringkat {rank+1}: Dokumen {doc_id}, Skor: {score}")
print(corpus)
print(query1)

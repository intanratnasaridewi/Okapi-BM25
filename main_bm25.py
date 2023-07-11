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
def calculate_Lave(corpus):
    # rata-rata panjang dokumen dari semua koleksi
    total_length = sum(len(doc) for doc in corpus)
    return total_length / len(corpus)
def calculate_idfalternative(query,corpus):
    # Menghitung IDF untuk setiap term dalam query
    N = len(corpus)  # Jumlah total dokumen dalam koleksi
    idf_scores = {}
    for term in query.split():
        dft = sum(1 for doc in corpus if term in doc)  # Jumlah dokumen yang mengandung term
        idf_scores[term] = math.log(N-dft+0.5) / (dft+0.5)
    return idf_scores

def calculate_idf0(query,corpus):
    # Menghitung IDF untuk setiap term dalam query
    N = len(corpus)  # Jumlah total dokumen dalam koleksi
    idf_scores = {}
    for term in query.split():
        dft = sum(1 for doc in corpus if term in doc)  # Jumlah dokumen yang mengandung term
        idf_scores[term] = math.log(N / dft)
    return idf_scores

def standar_bm25(query, document, k1, b, idf_scores, Lave):
    score = 0.0
    Lave = calculate_Lave(corpus)  # Panjang rata-rata dokumen dalam koleksi
    idf_scores = calculate_idf0(query,corpus)
    
    # Menghitung skor BM25
    for term in query.split():
        if term in document:
            tf_td = document.count(term)  # Frekuensi kemunculan term dalam dokumen
            Ld = len(document)  # Panjang dokumen dalam jumlah term
            Ld=abs(Ld)
            score += idf_scores[term] * tf_td * (k1 + 1) / tf_td  + k1 * ((1 - b) + b * (Ld / Lave))  
    return score

def long_bm25(query, document, k1, b, k3, idf_scores, Lave):
    score = 0.0
    
    # Menghitung skor BM25
    for term in query.split():
        tf_tq = query.count(term)  # Frekuensi kemunculan term dalam query
        if term in document:
            tf_td = document.count(term)  # Frekuensi kemunculan term dalam dokumen
            Ld = len(document)  # Panjang dokumen dalam jumlah term
            Ld=abs(Ld)
            score += idf_scores[term] * tf_td * (k1 + 1) / tf_td  + k1 * ((1 - b) + b * (Ld / Lave))*(k3+1)*tf_tq/k3+tf_tq
    return score

def main(query, document, corpus):
    k1 = 1.2
    b = 0.75
    k3=1.2
    Lave = calculate_Lave(corpus)  # Panjang rata-rata dokumen dalam koleksi
    #kalkulasi idf alternative: intinya kalo gaada kata di dokumen, idfnya ga 0, jadi ga error
    idf_scoresAlter = calculate_idfalternative(query,corpus)
    #kalkulasi idf standar: kelemahannya kalo query != dokumen manapun, pasti bakal error soalnya ada pembagian 0
    idf_score0 = calculate_idf0(query,corpus)
    #pake idf alternative dan algortima standar = dia cocok buat query singkat
    scoreAlterstandar=standar_bm25(query, document, k1, b, idf_scoresAlter, Lave)
    #pake idf alternative dan algortima long = dia cocok buat query panjang
    scoreAlterlong=long_bm25(query, document, k1, b, k3, idf_scoresAlter, Lave)
    #pake idf standar dan algortima standar = dia cocok buat query singkat
    score0standar=standar_bm25(query, document, k1, b, idf_score0, Lave)
    #pake idf standar dan algortima long = dia cocok buat query panjang
    score0long=long_bm25(query, document, k1, b, k3, idf_score0, Lave)

    return scoreAlterlong


#COBA ALGORTIMA DI TERMINAL


corpus = [ "The bluebirds chirped a melodious tune in the morning",
    "The blue cotton candy melted in my mouth, leaving a sugary sweetness",
    "The blue hour before sunrise cast a magical glow over the landscape",
    "The blue tang fish swam gracefully in the coral reef",
    "The blue sea glass sparkled in the sunlight, hidden among the sand",
    "The blue hiking trail led us through a dense forest",
    "The blue hydrangea bush bloomed with clusters of beautiful flowers",
    "The blue suede shoes were my favorite pair",
    "The blue dragon kite flew high in the sky, trailing its tail behind",
    "The blueberry yogurt was a healthy and delicious snack",
    "The clear blue water of the swimming pool beckoned on a hot summer day",
    "The blue hydrangea bouquet added a pop of color to the wedding",
    "The blue eyes of the husky dog were striking against its white fur",
    "The blue sailboat glided across the calm blue sea"]




# Contoh query
query1 = "blue dragon"


# Melakukan preprocessing pada dokumen dalam koleksi
corpus = [preprocess(doc) for doc in corpus]

# Melakukan preprocessing pada query
query1 = preprocess(query1)


# Menghitung skor BM25 untuk setiap dokumen
scores = []
for i, doc in enumerate(corpus):
    doc_score = main(query1, doc, corpus)
    scores.append((i, doc_score))  # Menyimpan nomor dokumen dan skor
    
# Melakukan perangkingan berdasarkan skor
ranked_scores = sorted(scores, key=lambda x: x[1],  reverse=True)

# Menampilkan hasil perangkingan
for rank, (doc_id, score) in enumerate(ranked_scores):
    print(f"Peringkat {rank+1}: Dokumen {doc_id}, Skor: {score}")
print(corpus)
print(query1)


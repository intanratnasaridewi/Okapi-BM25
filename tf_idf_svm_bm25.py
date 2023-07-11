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

def calculate_bm25(query, document, corpus, k1, b, k3):
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
        tf_tq = query.count(term)  # Frekuensi kemunculan term dalam query
        if term in document:
            tf_td = document.count(term)  # Frekuensi kemunculan term dalam dokumen
            dl = len(document)  # Panjang dokumen dalam jumlah term
            score += idf_scores[term] * (tf_td * (k1 + 1)) / (tf_td  + (k1 * (1 - b)+ b * (dl / avgdl)))
    
    return score

def calculate_avgdl(corpus):
    total_length = sum(len(doc) for doc in corpus)
    return total_length / len(corpus)

def evaluate_bm25(query, relevant_docs, corpus, k1, b, k3):
    tp = 0  # True Positive
    fp = 0  # False Positive
    fn = 0  # False Negative
    
    
    for doc_id, document in enumerate(corpus):
        score = calculate_bm25(query, document, corpus, k1, b, k3)
        
        if doc_id in relevant_docs:
            # Dokumen yang relevan
            if score > threshold:
                tp += 1
            else:
                fn += 1
        else:
            # Dokumen yang tidak relevan
            if score > threshold:
                fp += 1
        
    # Handle division by zero
    if tp + fp == 0:
        precision = 0
    else:
        precision = tp / (tp + fp)
    
    recall = tp / (tp + fn)
    
    # Handle division by zero
    if precision + recall == 0:
        f1_score = 0
    else:
        f1_score = 2 * ((precision * recall) / (precision + recall))
    
    return precision, recall, f1_score

# Contoh penggunaan
# Dokumen yang relevan untuk query tertentu
relevant_docs = {0}  # Misalnya, dokumen 0 dan 2 dianggap relevan

# Dokumen dalam koleksi
corpus = [
    "Blue is my favorite color, i can use this everytime i see blue",
    "Sky is blue and sea is blue, i can see blue everywhere",
    "sky is blue and sky is beautiful, i can see blue everywhere",
]

# Parameter BM25
k1 = 1.2
b = 0.75
k3=1.2
threshold = 0.0  # Nilai ambang batas

# Contoh query
query1 = "blue favorite color use everytime see blue"
# query2 = "blue beautiful sky"
# query3 = "blue sky everywhere"

# Melakukan preprocessing pada dokumen dalam koleksi
corpus = [preprocess(doc) for doc in corpus]

# Melakukan preprocessing pada query
query1 = preprocess(query1)
# query2 = preprocess(query2)
# query3 = preprocess(query3)

# Menghitung skor BM25 untuk setiap dokumen
scores = []
for i, doc in enumerate(corpus):
    doc_score = calculate_bm25(query1, doc, corpus, k1, b, k3)
    scores.append((i, doc_score))  # Menyimpan nomor dokumen dan skor
    
# Melakukan perangkingan berdasarkan skor
ranked_scores = sorted(scores, key=lambda x: x[1],  reverse=True)

precision, recall, f1_score = evaluate_bm25(query1, relevant_docs, corpus, k1, b, k3)



# Menampilkan hasil perangkingan
for rank, (doc_id, score) in enumerate(ranked_scores):
    print(f"Peringkat {rank+1}: Dokumen {doc_id}, Skor: {score}")
print(corpus)
print(query1)
# Menampilkan hasil evaluasi
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1_score)

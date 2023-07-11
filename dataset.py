# import string
# import nltk
# nltk.download('omw-1.4')
# from nltk.tokenize import word_tokenize

# from nltk.stem import WordNetLemmatizer, PorterStemmer

# def preprocess(input_text):
#     # Create a stop word list for English
#     stop_words = ["n't", 'was', "couldn't", "hadn't", "aren't", "shouldn't", "couldn't", "hasn't", "that'll", "you've", "mightn't", "wouldn't", "doesn't", "wasn't", "haven't", "mustn'", 'mightn', 'shan', "needn't", 'that', "she's", "shouldn't", 'now', "weren't", "don't", "mustn't", "hadn't", "weren't", "won't", "you'd", "needn't", "aren't", "wasn'", "didn't", 'didn', "it's", "isn't", "hasn'", 'wouldn', "doesn'", 'to', 'how', 'we', 'not', 'where', 'he', 'itself', 'can', 'nor', 'few', 'had', 'here', 'them', 'hers', 'this', 'under', 'all', 'same', 'by', 'yourself', 'other', 'out', 'my', 'about', 'will', 'some', 'herself', 'as', 'these', 'do', 'very', 'from', 'then', 'yourselves', 'above', 'most', 'it', 'any', 'only', 'ma', 'for', 'no', 'you', 'between', 'such', 'your', 'ain', 'in', 'being', 'up', 'because', 'him', 'more', 'while', 'were', 'into', 'haven', 'his', 'both', 'having', 'myself', 'is', 'than', 'ourselves', 'but', "should've", 'when', 'hadn', 'himself', "you'll", 'its', 'until', 'are', 'and', 'further', 'if', 'off', 'won', 'who', 'i', 'has', 'during', 'so', 'isn', "you're", 'have', 'again', 'does', 'below', 'theirs', 'ours', 'the', 'through', 'own', 'those', 'too', 'be', 'on', 'doing', 'don', 'me', 'should', 'down', 'which', 'after', 're', 'once', 'their', 'against', 'whom', 'they', 'what', 'an', 'each', 'at', 'themselves', 'been', "shan't", 'she', 'did', 'with', 'our', 'there', 'just', 'over', 'why', 'll', 'before', 'of', 'her', 'or', 'yours', 've', 'am', 'y', "'s", 'o', 'm', 'd', "a"]
   
#     tokenizing_sentence = [word for word in word_tokenize(input_text.lower()) if word not in stop_words]
#     # print(tokenizing_sentence)
#     porter = PorterStemmer()    
#     wnl = WordNetLemmatizer()    
    
#     # NEW FORMULA WITH PORTER AND WNL
#     new_sentence = []
#     i = 0
#     while(i<len(tokenizing_sentence)):
#         if(str(tokenizing_sentence[i]).endswith('e')):
#             lemmatized_word_e = wnl.lemmatize(str(tokenizing_sentence[i]))
#             new_sentence.append(lemmatized_word_e)
#             # print(lemmatized_word)
#         elif(str(tokenizing_sentence[i]).endswith('s')):
#             lemmatized_word_s = wnl.lemmatize(str(tokenizing_sentence[i]))
#             new_sentence.append(lemmatized_word_s)
#             # print(lemmatized_word_s)
#         elif(str(tokenizing_sentence[i]).endswith('y')):
#             new_sentence.append(str(tokenizing_sentence[i]))
#         elif(str(tokenizing_sentence[i]).endswith('ed')):
#             lemmatized_word_ed = wnl.lemmatize(str(tokenizing_sentence[i]), pos='v')
#             new_sentence.append(lemmatized_word_ed)
#             # print(lemmatized_word_ed)
#         else:
#             stemmed_words = porter.stem(str(tokenizing_sentence[i]))
#             new_sentence.append(stemmed_words)
#             # print(stemmed_words)
#         i+=1
#     # tokens_without_punct
#     without_punctuation = [token for token in new_sentence if token not in string.punctuation]
#     final_sentence = ' '.join(without_punctuation)
#     return final_sentence

# def evaluate_bm25(query, relevant_docs, corpus, k1, b):
#     tp = 0  # True Positive
#     fp = 0  # False Positive
#     fn = 0  # False Negative
    
    
#     for doc_id, document in enumerate(corpus):
#         score = standar_bm25(query, document, corpus, k1, b)
        
#         if doc_id in relevant_docs:
#             # Dokumen yang relevan
#             if score > 0:
#                 tp += 1
#             else:
#                 fn += 1
#         else:
#             # Dokumen yang tidak relevan
#             if score > 0:
#                 fp += 1
        
#     # Handle division by zero
#     if tp + fp == 0:
#         precision = 0
#     else:
#         precision = tp / (tp + fp)
    
#     recall = tp / (tp + fn)
    
#     # Handle division by zero
#     if precision + recall == 0:
#         f1_score = 0
#     else:
#         f1_score = 2 * ((precision * recall) / (precision + recall))
    
#     return precision, recall, f1_score
# relevant_docs = {0}  # Misalnya, dokumen 0 dan 2 dianggap relevan
# precision, recall, f1_score = evaluate_bm25(query1, relevant_docs, corpus, k1, b)
# # Menampilkan hasil evaluasi
# print("Precision:", precision)
# print("Recall:", recall)
# print("F1-score:", f1_score)

# def list_corpus_preprocess(corpus):
    
#     corpus = [
#     "Blue is my favorite color, I can use this everytime I see blue",
#     "Sky is blue and sea is blue, I can see blue everywhere",
#     "Sky is blue and sky is beautiful, I can see blue everywhere",
#     "The ocean reflects the blue sky, creating a serene view",
#     "In my painting, I always choose shades of blue to depict calmness",
#     "The bluebird flew gracefully across the clear blue sky",
#     "The flowers in the garden are various shades of blue",
#     "The artist used blue hues to create a sense of tranquility",
#     "The blue dress she wore matched perfectly with her eyes",
#     "The sky turned dark blue as the sun started to set",
#     "The underwater world is full of vibrant blue colors",
#     "The blueberry pie was delicious, with a sweet and tangy taste",
#     "The blue velvet curtains added an elegant touch to the room",
#     "The baby's eyes sparkled with a deep blue color",
#     "I love the feeling of the cool blue water against my skin",
#     "The blue jay chirped loudly from the tree branch",
#     "The blue whale is the largest mammal on Earth",
#     "The painting depicted a vast blue ocean with crashing waves",
#     "The blue mosaic tiles adorned the swimming pool",
#     "The clear blue sky made for a perfect day at the beach",
#     "The blue butterfly fluttered its wings gracefully",
#     "The blue ink spilled on the paper, creating a beautiful pattern",
#     "The sky was painted in shades of blue and orange during the sunset",
#     "The blue-eyed cat purred softly as it curled up in my lap",
#     "The blue jeans I wore were faded and comfortable",
#     "The robin's eggs were a delicate shade of blue",
#     "The ocean breeze brushed against my face as I sailed on the blue sea",
#     "The blue dragonfly hovered above the water, mesmerizing to watch",
#     "The blue hydrangea flowers bloomed in the garden, adding a pop of color",
#     "The blue ice popsicles were a refreshing treat on a hot summer day",
#     "The blue pen ran out of ink as I was writing a letter",
#     "The blue ribbon adorned the gift, making it look even more special",
#     "The blue moon appeared in the night sky, a rare sight to behold",
#     "The blue tile mosaic created an intricate pattern on the wall",
#     "The deep blue sea stretched out as far as the eye could see",
#     "The blue heron gracefully spread its wings and took flight",
#     "The blueberry pancakes were fluffy and delicious",
#     "The blue sports car sped down the highway, leaving a trail of dust behind",
#     "The clear blue lake reflected the surrounding mountains",
#     "The blueberry muffins were a hit at the breakfast table",
#     "The blue balloon floated up into the sky, carried by the wind",
#     "The peacock proudly displayed its vibrant blue feathers",
#     "The ocean waves crashed against the rocky blue cliffs",
#     "The blue kite soared high in the air, dancing with the wind",
#     "The blue eyes of the newborn baby were full of wonder",
#     "The blue tile roof of the house glistened under the sunlight",
#     "The blueberry smoothie was a refreshing drink on a hot summer afternoon",
#     "The blue umbrella provided shade from the scorching sun",
#     "The blue mosaic artwork adorned the walls of the art gallery",
#     "The blue lagoon was a popular tourist destination",
#     "The bluebirds chirped a melodious tune in the morning",
#     "The blue cotton candy melted in my mouth, leaving a sugary sweetness",
#     "The blue hour before sunrise cast a magical glow over the landscape",
#     "The blue tang fish swam gracefully in the coral reef",
#     "The blue sea glass sparkled in the sunlight, hidden among the sand",
#     "The blue hiking trail led us through a dense forest",
#     "The blue hydrangea bush bloomed with clusters of beautiful flowers",
#     "The blue suede shoes were my favorite pair",
#     "The blue dragon kite flew high in the sky, trailing its tail behind",
#     "The blueberry yogurt was a healthy and delicious snack",
#     "The clear blue water of the swimming pool beckoned on a hot summer day",
#     "The blue hydrangea bouquet added a pop of color to the wedding",
#     "The blue eyes of the husky dog were striking against its white fur",
#     "The blue sailboat glided across the calm blue sea",
#     "The blue ink stain on my shirt was difficult to remove",
#     "The blue jays squabbled over the last remaining breadcrumbs",
#     "The blueberry farm was a popular destination for berry picking",
#     "The blue lapis lazuli gemstone had a rich and deep hue",
#     "The clear blue sky stretched out above the open field",
#     "The blue butterfly fluttered from flower to flower, collecting nectar",
#     "The blue glass vase was a beautiful centerpiece on the table",
#     "The blue heron stood still in the shallow water, waiting for its prey",
#     "The blueberry cobbler smelled heavenly as it baked in the oven",
#     "The blue-eyed girl smiled brightly as she played in the park",
#     "The blue sail of the yacht billowed in the wind",
#     "The blueberry bushes were heavy with ripe fruit",
#     "The blue dragonfly perched on a leaf, its wings shimmering in the sunlight",
#     "The blue peacock strutted around, showing off its elaborate plumage",
#     "The blueberry pancakes were topped with a dollop of whipped cream",
#     "The deep blue sky was dotted with twinkling stars",
#     "The blueberry bushes rustled as a gentle breeze passed through",
#     "The blue butterfly emerged from its chrysalis, spreading its wings for the first time",
#     "The blue tang fish swam gracefully among the colorful coral",
#     "The blue hydrangea blooms attracted bees and butterflies",
#     "The blue marbles rolled across the floor, making a clicking sound",
#     "The bluebird's song filled the air with melodious notes",
#     "The blue velvet cake was a decadent dessert at the party",
#     "The clear blue lake was a popular spot for fishing",
#     "The blue ink pen glided smoothly across the paper as I wrote",
#     "The blue ribbon was tied around the gift with a neat bow",
#     "The blue moon illuminated the night, casting an ethereal glow",
#     "The blue tile mosaic created a stunning visual display",
#     "The deep blue sea was home to a diverse range of marine life",
#     "The blue heron waded through the shallow water, searching for food",
#     "The blueberry muffins were freshly baked and still warm",
#     "The blue balloon floated high above the crowd, drawing everyone's attention",
#     "The peacock proudly displayed its beautiful blue and green feathers",
#     "The crashing waves against the blue cliffs created a mesmerizing sound",
#     "The blue kite soared gracefully in the sky, guided by the wind",
#     "The blue eyes of the baby sparkled with innocence",
#     "The blue tile roof of the house stood out against the surrounding landscape",
#     "The blueberry smoothie was a refreshing drink on a hot summer day",
#     "The blue umbrella provided shade from the scorching sun",
#     "The blue mosaic artwork added a vibrant touch to the art gallery",
#     "The blue lagoon was a hidden gem, surrounded by lush greenery",
#     "The bluebirds chirped happily in the trees, filling the air with their melodies",
#     "The blue cotton candy melted in my mouth, leaving behind a sugary sweetness",
#     "The blue hour before sunrise cast a mystical glow over the horizon",
#     "The blue tang fish swam gracefully in the crystal-clear water",
#     "The blue sea glass glistened in the sunlight, scattered along the sandy beach",
#     "The blue hiking trail led us through a dense forest, showcasing the beauty of nature",
#     "The blue hydrangea bush was in full bloom, covering the garden with colorful flowers",
#     "The blue suede shoes were my go-to footwear for special occasions",
#     "The blue dragon kite soared high in the sky, its tail trailing behind",
#     "The blueberry yogurt was a healthy and delicious snack for breakfast",
#     "The clear blue water of the swimming pool provided relief from the scorching heat",
#     "The blue hydrangea bouquet added a touch of elegance to the wedding ceremony",
#     "The blue eyes of the husky dog captivated everyone's attention",
#     "The blue sailboat glided gracefully across the tranquil blue sea",
#     "The blue ink stain on my shirt was stubborn and difficult to remove",
#     "The blue jays chirped loudly, competing for the attention of the nearby birds",
#     "The blueberry farm was a popular destination for families to enjoy berry picking",
#     "The blue lapis lazuli gemstone had a deep and rich color",
#     "The clear blue sky stretched out endlessly, blending seamlessly with the horizon",
#     "The blue butterfly fluttered from flower to flower, collecting nectar for sustenance",
#     "The blue glass vase added a touch of sophistication to the table setting",
#     "The blue heron stood still in the shallow water, patiently waiting for its prey",
#     "The blueberry cobbler filled the kitchen with a mouthwatering aroma",
#     "The blue-eyed girl had a radiant smile that brightened up the room",
#     "The blue sail of the yacht billowed in the wind, propelling it forward",
#     "The blueberry bushes were heavy with plump and juicy berries",
#     "The blue dragonfly perched delicately on a leaf, its iridescent wings shimmering",
#     "The blue peacock proudly displayed its magnificent tail feathers",
#     "The blueberry pancakes were served piping hot, topped with a drizzle of maple syrup",
#     "The deep blue sky was adorned with a blanket of twinkling stars",
#     "The blueberry bushes rustled gently in the breeze, as if whispering secrets",
#     "The blue butterfly emerged gracefully from its chrysalis, revealing its vibrant wings",
#     "The blue tang fish gracefully glided among the vibrant coral reef",
#     "The blue hydrangea blooms attracted bees and butterflies, buzzing with life",
#     "The blue marbles rolled across the floor, creating a symphony of sounds",
#     "The bluebird's melodious song filled the air, bringing joy to all who listened",
#     "The blue velvet cake was a decadent dessert that melted in your mouth",
#     "The clear blue lake was a tranquil oasis, inviting visitors to relax and unwind",
#     "The blue ink pen flowed smoothly across the paper, capturing thoughts and ideas",
#     "The blue ribbon added a touch of elegance to the gift, making it even more special",
#     "The blue moon cast an enchanting glow, illuminating the night sky",
#     "The blue tile mosaic created a stunning visual masterpiece, capturing the imagination",
#     "The deep blue sea teemed with a diverse array of marine life, a hidden world of wonders",
#     "The blue heron gracefully waded through the shallow water, searching for its next meal",
#     "The blueberry muffins were freshly baked, with a golden crust and bursting with flavor",
#     "The blue balloon floated effortlessly above the crowd, capturing everyone's attention",
#     "The peacock proudly displayed its magnificent blue and green plumage, a sight to behold",
#     "The crashing waves against the towering blue cliffs created a mesmerizing spectacle",
#     "The blue kite soared majestically in the sky, dancing with the wind in perfect harmony",
#     "The blue eyes of the baby sparkled with innocence and curiosity, filled with wonder",
#     "The blue tile roof of the house stood out against the backdrop of the surrounding landscape",
#     "The blueberry smoothie was a refreshing and nutritious drink, perfect for a hot summer day",
#     "The blue umbrella provided much-needed shade from the scorching heat of the sun",
#     "The blue mosaic artwork added a vibrant and captivating element to the art gallery",
#     "The blue lagoon was a hidden paradise, nestled amidst lush greenery and crystal-clear waters",
#     "The bluebirds chirped happily in the trees, their cheerful melodies filling the air",
#     "The blue cotton candy melted in my mouth, leaving behind a sugary sweetness that delighted the taste buds",
#     "The blue hour before sunrise cast a magical glow over the horizon, painting the sky with hues of blue and gold",
#     "The blue tang fish gracefully swam through the crystal-clear water, its vibrant colors shining in the sunlight",
#     "The blue sea glass glistened along the sandy shore, each piece a unique treasure waiting to be discovered",
#     "The blue hiking trail wound its way through a dense forest, offering glimpses of hidden waterfalls and breathtaking vistas",
#     "The blue hydrangea bush was in full bloom, its clusters of delicate flowers adding a touch of beauty to the garden",
#     "The blue suede shoes were my favorite pair, comfortable and stylish, perfect for any occasion",
#     "The blue dragon kite soared high in the sky, its long tail trailing behind, a playful dance with the wind",
#     "The blueberry yogurt was a healthy and delicious snack, packed with antioxidants and natural sweetness",
#     "The clear blue water of the swimming pool provided a welcome escape from the heat, inviting everyone to take a refreshing dip",
#     "The blue hydrangea bouquet added a touch of elegance to the wedding ceremony, its soft blooms complementing the bride's gown",
#     "The blue eyes of the husky dog were striking and captivating, reflecting a deep intelligence and gentle spirit",
#     "The blue sailboat glided gracefully across the tranquil blue sea, its white sails billowing in the breeze",
#     "The blue ink stain on my shirt stubbornly refused to come out, a reminder of a clumsy mishap",
#     "The blue jays chirped loudly, their vibrant blue feathers contrasting against the lush green foliage",
#     "The blueberry farm was a popular destination for families to enjoy a day of berry picking, creating lasting memories",
#     "The blue lapis lazuli gemstone had a deep and rich color, symbolizing wisdom, truth, and spiritual enlightenment",
#     "The clear blue sky stretched out endlessly, merging seamlessly with the horizon, a vast expanse of infinite possibilities",
#     "The blue butterfly fluttered from flower to flower, delicately sipping nectar, a graceful dance of nature's beauty",
#     "The blue glass vase added a touch of sophistication to the table setting, showcasing a vibrant bouquet of fresh flowers",
#     "The blue heron stood still in the shallow water, patiently waiting for its prey, its long neck poised for a strike",
#     "The blueberry cobbler filled the kitchen with a mouthwatering aroma, its bubbling fruit and buttery crust tempting all who entered",
#     "The blue-eyed girl had a radiant smile that brightened up the room, her eyes sparkling with joy and warmth",
#     "The blue sail of the yacht billowed in the wind, carrying the vessel across the vast blue expanse, a symbol of freedom and adventure",
#     "The blueberry bushes were heavy with plump and juicy berries, ready to be harvested and enjoyed",
#     "The blue dragonfly perched delicately on a leaf, its iridescent wings shimmering in the sunlight, a jewel of nature's creation",
#     "The blue peacock proudly displayed its magnificent tail feathers, spreading them wide in a grand spectacle of beauty",
#     "The blueberry pancakes were served piping hot, topped with a drizzle of maple syrup, a breakfast treat to savor",
#     "The deep blue sky was adorned with a blanket of twinkling stars, each one a distant sun in a vast cosmic tapestry",
#     "The blueberry bushes rustled gently in the breeze, as if whispering secrets to the passing wind",
#     "The blue butterfly emerged gracefully from its chrysalis, revealing its vibrant wings for the first time, a symbol of transformation and rebirth",
#     "The blue tang fish gracefully glided among the vibrant coral reef, its bright colors blending with the underwater paradise",
#     "The blue hydrangea blooms attracted bees and butterflies, buzzing with life as they collected nectar and pollinated the flowers",
#     "The blue marbles rolled across the floor, creating a symphony of sounds, their smooth surface reflecting the light",
#     "The bluebird's melodious song filled the air, bringing joy to all who listened, a sweet serenade of nature's music",
#     "The blue velvet cake was a decadent dessert that melted in your mouth, its rich flavor and velvety texture a true indulgence",
#     "The clear blue lake was a tranquil oasis, inviting visitors to relax and unwind, its calm waters reflecting the surrounding mountains",
#     "The blue ink pen flowed smoothly across the paper, capturing thoughts and ideas, the ink forming elegant strokes on the page",
#     "The blue ribbon added a touch of elegance to the gift, making it even more special, a symbol of appreciation and celebration",
#     "The blue moon cast an enchanting glow, illuminating the night sky and filling the world with a sense of wonder",
#     "The blue tile mosaic created a stunning visual masterpiece, each piece meticulously placed to form a work of art",
#     "The deep blue sea teemed with a diverse array of marine life, a hidden world of wonders waiting to be explored",
#     "The blue heron gracefully waded through the shallow water, searching for its next meal, its long legs and sharp beak poised for action",
#     "The blueberry muffins were freshly baked, with a golden crust and bursting with flavor, a delicious treat to start the day",
#     "The blue balloon floated effortlessly above the crowd, capturing everyone's attention, a beacon of joy and celebration",
#     "The peacock proudly displayed its magnificent blue and green plumage, each feather a vibrant testament to its beauty",
#     "The crashing waves against the towering blue cliffs created a mesmerizing spectacle, their powerful force echoing through the air",
#     "The blue kite soared majestically in the sky, dancing with the wind in perfect harmony, a symbol of freedom and possibility",
#     "The blue eyes of the baby sparkled with innocence and curiosity, filled with wonder and the promise of a bright future",
#     "The blue tile roof of the house stood out against the backdrop of the surrounding landscape, a charming and picturesque sight",
#     "The blueberry smoothie was a refreshing and nutritious drink, perfect for a hot summer day, a burst of fruity goodness",
#     "The blue umbrella provided much-needed shade from the scorching heat of the sun, offering relief on a sweltering day",
#     "The blue mosaic artwork added a vibrant and captivating element to the art gallery, drawing the gaze of all who entered",
#     "The blue lagoon was a hidden paradise, nestled amidst lush greenery and crystal-clear waters, a serene haven of tranquility",
#     "The bluebirds chirped happily in the trees, their cheerful melodies filling the air, a chorus of nature's delight",
#     "The blue cotton candy melted in my mouth, leaving behind a sugary sweetness that delighted the taste buds, a guilty pleasure",
#     "The blue hour before sunrise cast a magical glow over the horizon, painting the sky with hues of blue and gold, a moment of serene beauty",
#     "The blue tang fish gracefully swam through the crystal-clear water, its vibrant colors shining in the sunlight, a dazzling sight",
#     "The blue sea glass glistened along the sandy shore, each piece a unique treasure waiting to be discovered, a gift from the ocean",
#     "The blue hiking trail wound its way through a dense forest, offering glimpses of hidden waterfalls and breathtaking vistas, an adventure in nature's embrace",
#     "The blue hydrangea bush was in full bloom, its clusters of delicate flowers adding a touch of beauty to the garden, a floral masterpiece",
#     "The blue suede shoes were my go-to footwear for special occasions, their elegant and timeless design making a statement",
#     "The blue dragon kite soared high in the sky, its long tail trailing behind, a playful dance with the wind, a symbol of joy and freedom",
#     "The blueberry yogurt was a healthy and delicious snack, packed with antioxidants and natural sweetness, a guilt-free indulgence",
#     "The clear blue water of the swimming pool provided a welcome escape from the heat, inviting everyone to take a refreshing dip, a source of cool respite",
#     "The blue hydrangea bouquet added a touch of elegance to the wedding ceremony, its soft blooms complementing the bride's gown, a symbol of love and purity",
#     "The blue eyes of the husky dog were striking and captivating, reflecting a deep intelligence and gentle spirit, a window to its soul",
#     "The blue sail of the yacht billowed in the wind, carrying the vessel across the vast blue expanse, a symbol of adventure and exploration",
#     "The blue ink stain on my shirt stubbornly refused to come out, a reminder of a clumsy mishap, a mark of a momentary lapse",
#     "The blue jays chirped loudly, their vibrant blue feathers contrasting against the lush green foliage, a burst of color and sound",
#     "The blueberry farm was a popular destination for families to enjoy a day of berry picking, creating lasting memories, a bonding experience",
#     "The blue lapis lazuli gemstone had a deep and rich color, symbolizing wisdom, truth, and spiritual enlightenment, a stone of significance",
#     "The clear blue sky stretched out endlessly, merging seamlessly with the horizon, a vast expanse of infinite possibilities, a canvas for dreams",
#     "The blue butterfly fluttered from flower to flower, delicately sipping nectar, a graceful dance of nature's beauty, a symbol of transformation",
#     "The blue glass vase added a touch of sophistication to the table setting, showcasing a vibrant bouquet of fresh flowers, a centerpiece of elegance",
#     "The blue heron stood still in the shallow water, patiently waiting for its prey, its long neck poised for a strike, a master of patience and precision",
#     "The blueberry cobbler filled the kitchen with a mouthwatering aroma, its bubbling fruit and buttery crust tempting all who entered, a tantalizing treat",
#     "The blue-eyed girl had a radiant smile that brightened up the room, her eyes sparkling with joy and warmth, a beacon of happiness",
#     "The blue sail of the yacht billowed in the wind, carrying the vessel across the vast blue expanse, a symbol of freedom and adventure, a voyage of discovery",
#     "The blueberry bushes were heavy with plump and juicy berries, ready to be harvested and enjoyed, a fruitful bounty",
#     "The blue dragonfly perched delicately on a leaf, its iridescent wings shimmering in the sunlight, a jewel of nature's creation, a fleeting beauty",
#     "The blue peacock proudly displayed its magnificent tail feathers, spreading them wide in a grand spectacle of beauty, a regal presence",
#     "The blueberry pancakes were served piping hot, topped with a drizzle of maple syrup, a breakfast treat to savor, a delightful indulgence",
#     "The deep blue sky was adorned with a blanket of twinkling stars, each one a distant sun in a vast cosmic tapestry, a celestial wonder",
#     "The blueberry bushes rustled gently in the breeze, as if whispering secrets to the passing wind, a chorus of nature's whispers",
#     "The blue butterfly emerged gracefully from its chrysalis, revealing its vibrant wings for the first time, a symbol of transformation and rebirth, a metamorphosis complete",
#     "The blue tang fish gracefully glided among the vibrant coral reef, its bright colors blending with the underwater paradise, a marine ballet",
#     "The blue hydrangea blooms attracted bees and butterflies, buzzing with life as they collected nectar and pollinated the flowers, a buzzing symphony",
#     "The blue marbles rolled across the floor, creating a symphony of sounds, their smooth surface reflecting the light, a playful dance",
#     "The bluebird's melodious song filled the air, bringing joy to all who listened, a sweet serenade of nature's music, a joyful melody",
#     "The blue velvet cake was a decadent dessert that melted in your mouth, its rich flavor and velvety texture a true indulgence, a slice of heaven",
#     "The clear blue lake was a tranquil oasis, inviting visitors to relax and unwind, its calm waters reflecting the surrounding mountains, a serene sanctuary",
#     "The blue ink pen flowed smoothly across the paper, capturing thoughts and ideas, the ink forming elegant strokes on the page, a conduit of creativity",
#     "The blue ribbon added a touch of elegance to the gift, making it even more special, a symbol of appreciation and celebration, a token of affection",
#     "The blue moon cast an enchanting glow, illuminating the night sky and filling the world with a sense of wonder, a celestial spectacle",
#     "The blue tile mosaic created a stunning visual masterpiece, each piece meticulously placed to form a work of art, a testament to craftsmanship",
#     "The deep blue sea teemed with a diverse array of marine life, a hidden world of wonders waiting to be explored, an underwater paradise",
#     "The blue heron gracefully waded through the shallow water, searching for its next meal, its long legs and sharp beak poised for action, a hunter's instinct",
#     "The blueberry muffins were freshly baked, with a golden crust and bursting with flavor, a delicious treat to start the day, a morning delight",
#     "The blue balloon floated effortlessly above the crowd, capturing everyone's attention, a beacon of joy and celebration, a symbol of festivity",
#     "The peacock proudly displayed its magnificent blue and green plumage, each feather a vibrant testament to its beauty, a regal presence",
#     "The crashing waves against the towering blue cliffs created a mesmerizing spectacle, their powerful force echoing through the air, a symphony of nature",
#     "The blue kite soared majestically in the sky, dancing with the wind in perfect harmony, a symbol of freedom and possibility, a playful companion",
#     "The blue eyes of the baby sparkled with innocence and curiosity, filled with wonder and the promise of a bright future, a glimpse of pure joy",
#     "The blue tile roof of the house stood out against the backdrop of the surrounding landscape, a charming and picturesque sight, a cozy abode",
#     "The blueberry smoothie was a refreshing and nutritious drink, perfect for a hot summer day, a burst of fruity goodness, a revitalizing sip",
#     "The blue umbrella provided much-needed shade from the scorching heat of the sun, offering relief on a sweltering day, a shield from the elements",
#     "The blue mosaic artwork added a vibrant and captivating element to the art gallery, drawing the gaze of all who entered, a visual feast",
#     "The blue lagoon was a hidden paradise, nestled amidst lush greenery and crystal-clear waters, a serene haven of tranquility, a tropical escape",
#     "The bluebirds chirped happily in the trees, their cheerful melodies filling the air, a chorus of nature's delight, a harmonious symphony",
#     "The blue cotton candy melted in my mouth, leaving behind a sugary sweetness that delighted the taste buds, a guilty pleasure, a sugary delight",
#     "The blue hour before sunrise cast a magical glow over the horizon, painting the sky with hues of blue and gold, a moment of serene beauty, a tranquil awakening",
#     "The blue tang fish gracefully swam through the crystal-clear water, its vibrant colors shining in the sunlight, a dazzling sight, a living gem",
#     "The blue sea glass glistened along the sandy shore, each piece a unique treasure waiting to be discovered, a gift from the ocean, a hidden gem",
#     "The blue hiking trail wound its way through a dense forest, offering glimpses of hidden waterfalls and breathtaking vistas, an adventure in nature's embrace, a journey of exploration",
#     "The blue hydrangea bush was in full bloom, its clusters of delicate flowers adding a touch of beauty to the garden, a floral masterpiece, a colorful oasis",
#     "The blue suede shoes were my go-to footwear for special occasions, their elegant and timeless design making a statement, a touch of sophistication",
#     "The blue dragon kite soared high in the sky, its long tail trailing behind, a playful dance with the wind, a symbol of joy and freedom, a soaring companion",
#     "The blueberry yogurt was a healthy and delicious snack, packed with antioxidants and natural sweetness, a guilt-free indulgence, a creamy delight",
#     "The clear blue water of the swimming pool provided a welcome escape from the heat, inviting everyone to take a refreshing dip, a source of cool respite, a pool of rejuvenation",
#     "The blue hydrangea bouquet added a touch of elegance to the wedding ceremony, its soft blooms complementing the bride's gown, a symbol of love and purity, a bouquet of dreams",
#     "The blue eyes of the husky dog were striking and captivating, reflecting a deep intelligence and gentle spirit, a window to its soul, a gaze of understanding",
#     "The blue sail of the yacht billowed in the wind, carrying the vessel across the vast blue expanse, a symbol of freedom and adventure, a journey of discovery",
#     "The blue ink stain on my shirt stubbornly refused to come out, a reminder of a clumsy mishap, a mark of a momentary lapse, a stain of memories",
#     "The blue jays chirped loudly, their vibrant blue feathers contrasting against the lush green foliage, a burst of color and sound, a song of nature",
#     "The blueberry farm was a popular destination for families to enjoy a day of berry picking, creating lasting memories, a bonding experience, a fruitful adventure",
#     "The blue lapis lazuli gemstone had a deep and rich color, symbolizing wisdom, truth, and spiritual enlightenment, a stone of significance, a jewel of the earth",
#     "The clear blue sky stretched out endlessly, merging seamlessly with the horizon, a vast expanse of infinite possibilities, a canvas for dreams, a limitless expanse",
#     "The blue butterfly fluttered from flower to flower, delicately sipping nectar, a graceful dance of nature's beauty, a symbol of transformation, a delicate visitor",
#     "The blue glass vase added a touch of sophistication to the table setting, showcasing a vibrant bouquet of fresh flowers, a centerpiece of elegance, a floral masterpiece",
#     "The blue heron stood still in the shallow water, patiently waiting for its prey, its long neck poised for a strike, a master of patience and precision, a hunter's focus",
#     "The blueberry cobbler filled the kitchen with a mouthwatering aroma, its bubbling fruit and buttery crust tempting all who entered, a tantalizing treat, a slice of heaven",
#     "The blue-eyed girl had a radiant smile that brightened up the room, her eyes sparkling with joy and warmth, a beacon of happiness, a source of light",
#     "The blue sail of the yacht billowed in the wind, carrying the vessel across the vast blue expanse, a symbol of freedom and adventure, a voyage of discovery",
#     "The blueberry bushes were heavy with plump and juicy berries, ready to be harvested and enjoyed, a fruitful bounty, a taste of summer",
#     "The blue dragonfly perched delicately on a leaf, its iridescent wings shimmering in the sunlight, a jewel of nature's creation, a fleeting beauty, a delicate visitor",
#     "The blue peacock proudly displayed its magnificent tail feathers, spreading them wide in a grand spectacle of beauty, a regal presence, a sight to behold",
#     "The blueberry pancakes were served piping hot, topped with a drizzle of maple syrup, a breakfast treat to savor, a delightful indulgence, a stack of goodness",
#     "The deep blue sky was adorned with a blanket of twinkling stars, each one a distant sun in a vast cosmic tapestry, a celestial wonder, a nocturnal marvel",
#     "The blueberry bushes rustled gently in the breeze, as if whispering secrets to the passing wind, a chorus of nature's whispers, a serenade of the forest",
#     "The blue butterfly emerged gracefully from its chrysalis, revealing its vibrant wings for the first time, a symbol of transformation and rebirth, a metamorphosis complete, a new beginning",
#     "The blue tang fish gracefully glided among the vibrant coral reef, its bright colors blending with the underwater paradise, a marine ballet, a dance of the sea",
#     "The blue hydrangea blooms attracted bees and butterflies, buzzing with life as they collected nectar and pollinated the flowers, a buzzing symphony, a vibrant ecosystem",
#     "The blue marbles rolled across the floor, creating a symphony of sounds, their smooth surface reflecting the light, a playful dance, a game of chance",
#     "The bluebird's melodious song filled the air, bringing joy to all who listened, a sweet serenade of nature's music, a joyful melody, a song of happiness",
#     "The blue velvet cake was a decadent dessert that melted in your mouth, its rich flavor and velvety texture a true indulgence, a slice of heaven, a taste of luxury",
#     "The clear blue lake was a tranquil oasis, inviting visitors to relax and unwind, its calm waters reflecting the surrounding mountains, a serene sanctuary, a mirror of tranquility",
#     "The blue ink pen flowed smoothly across the paper, capturing thoughts and ideas, the ink forming elegant strokes on the page, a conduit of"]
    
#     return [preprocess(doc) for doc in corpus]
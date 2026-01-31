import re

texts = [
    "I Love this movie!!! #awesome #friday",
    "I Love this movie ,but the seats were bad",
    "Loved it! Best.Moive.Ever"
]

stop_words = {"i", "this", "the", "it", "were", "but", "a"}

def clean_text(sentence):
    
    sentence = sentence.lower()
    
    sentence = re.sub(r'[^a-z\s]', '', sentence)
    
    words = sentence.split()
    
    words = [w for w in words if w not in stop_words]
    
    cleaned_words = []
    for word in words:
        if word.endswith("ing"):
            word = word[:-3]
        elif word.endswith("ed"):
            word = word[:-2]
        elif word.endswith("es"):
            word = word[:-2]
        elif word.endswith("s"):
            word = word[:-1]
        cleaned_words.append(word)
    
    return cleaned_words

for i, text in enumerate(texts, start=1):
    cleaned = clean_text(text)
    print(f"Input {i} cleaned:", cleaned)
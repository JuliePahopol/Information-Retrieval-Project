import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

if __name__ == "__main__":
    text = "This is an example sentence demonstrating the removal of stopwords."
    print(f"Original text: {text}")
    print(f"After stopwords removal: {remove_stopwords(text)}")

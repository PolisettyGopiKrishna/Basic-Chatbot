import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download resources based on user preference
download_wordnet = input("Do you want to download WordNet for lemmatization? (y/n): ")

if download_wordnet.lower() == "y":
  nltk.download('wordnet')
  lemmatizer = WordNetLemmatizer()
else:
  lemmatizer = None

nltk.download('punkt')
stop_words = set(stopwords.words("english"))

def conversation(user_input):
  # Preprocess user input
  user_input = user_input.lower()  # Lowercase
  tokens = nltk.word_tokenize(user_input)  # Tokenize

  # Filter tokens based on stop words and lemmatization option
  if lemmatizer:
    filtered_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
  else:
    filtered_tokens = [token for token in tokens if token not in stop_words]

  processed_input = " ".join(filtered_tokens)  # Join tokens back into a string

  # Define basic responses
  responses = {
    "hello": "Hi there! How can I help you today?",
  }

  # Check for predefined responses
  if processed_input in responses:
    return responses[processed_input]
  else:
    # Fallback response for unknown inputs
    return "Sorry, I don't understand your question. Can you rephrase it?"

# Start the conversation
print("Hi there! I'm Chatbot. Let's chat!")
while True:
  user_input = input("> ")
  if user_input == "bye":
    break
  response = conversation(user_input)
  print(f"Chatbot: {response}")

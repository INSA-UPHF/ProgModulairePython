from math_utils import add, subtract
from string_utils import capitalize_words, count_words
import config

def main():
    num1, num2 = 5, 3
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Soustraction: {num1} - {num2} = {subtract(num1, num2)}")

    sentence = "bonjour le monde"
    print(f"Phrase original: {sentence}")
    print(f"Phrase capitalisée: {capitalize_words(sentence)}")
    print(f"Nombre de mots: {count_words(sentence)}")

    print(f"Application: {config.APP_NAME} (Version: {config.VERSION})")

if __name__ == "__main__":
    main()

def capitalize_words(sentence):
    """Met en majuscule chaque mot dans une phrase."""
    return ' '.join(word.capitalize() for word in sentence.split())

def count_words(sentence):
    """Compte le nombre de mots dans une phrase."""
    return len(sentence.split())

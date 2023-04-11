import string


def replace_abbreviations_naive(tweet, abbreviations_dict):
    
    results = []
    for sentence in tweet:
        words = sentence.split()
        for i, word in enumerate(words):
            stripped_word = word.strip(string.punctuation)
            for key, value in abbreviations_dict.items():
                if stripped_word == key:
                    words[i] = value+ word[len(stripped_word):]
                    break
        results.append(" ".join(words))
    return results
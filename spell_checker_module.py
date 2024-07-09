from pyvi import ViTokenizer, ViPosTagger

class CustomSpellChecker:
    def __init__(self, dictionary_file):
        self.words = set()
        self.load_dictionary(dictionary_file)

    def load_dictionary(self, dictionary_file):
        with open(dictionary_file, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                self.words.add(word)
    
    def correction(self, word):
        if word in self.words:
            return word
        
        closest_match = min(self.words, key=lambda w: self.levenshtein_distance(w, word))
        return closest_match
    
    @staticmethod
    def levenshtein_distance(s1, s2):
        if len(s1) < len(s2):
            return CustomSpellChecker.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]

def correct_spelling(tokens, pos_tags, spell_checker):
    corrected_tokens = []
    for token, pos in zip(tokens, pos_tags):
        if pos in ['N', 'V', 'A']:
            corrected_token = spell_checker.correction(token)
        else:
            corrected_token = token
        corrected_tokens.append(corrected_token)
    corrected_text = ' '.join(corrected_tokens)
    return corrected_text

def spell_check_ocr_result(ocr_text, spell_checker):
    tokens = ViTokenizer.tokenize(ocr_text).split(' ')
    pos_tags = ViPosTagger.postagging(' '.join(tokens))[1]
    corrected_text = correct_spelling(tokens, pos_tags, spell_checker)
    return corrected_text

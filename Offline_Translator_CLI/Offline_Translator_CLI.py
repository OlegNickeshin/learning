from datetime import datetime
import argparse
import json
import re
with open('dict.json', 'r') as reader:
    dictionary = json.load(reader)
reversed_dictionary = {v: k for k, v in dictionary.items()}

class OfflineTranslator:
    def __init__ (self, text):
        self.text = text
        self.tokens = self.tokenize()
        
    def tokenize(self):
        return re.findall(r"\w+|[^\w\s]|\s+", self.text, re.UNICODE)

    def translate(self, direction):
        translated = ''
        is_to_ru = direction == '2ru'
        dict_source = dictionary if is_to_ru else reversed_dictionary

        for token in self.tokens:
            if token.isalpha():
                lower_token = token.lower()
                translated_word = dict_source.get(lower_token, token)
                translated += self.preserve_case(token, translated_word)
            else:
                translated += token
        return translated           
                

    def preserve_case(self, original, translated):
        result = ''
        for original_char, translated_char in zip(original, translated):
            if original_char.isupper():
                result += translated_char.upper()
            else:
                result += translated_char
        return result

        
        
    

parser = argparse.ArgumentParser(description = 'oflline ru<->en Simple Offline CLI Translator with History')
parser.add_argument('--text', type = str, nargs = '+', help = 'insert text to translate')
parser.add_argument('--dir',
    type=str,
    help='set translation direction explicitly (2en or 2ru)'
)
args = parser.parse_args()

text = ' '.join(args.text)
translator = OfflineTranslator(text)

if args.dir == '2en':
    direction = '2en'
elif args.dir == '2ru':
    direction = '2ru'
else:
    en_count = 0
    ru_count = 0
    dict_keys = set(dictionary.keys())
    dict_values = set(dictionary.values())
    for word in args.text:
        word = word.lower()
        if word in dict_keys:
            en_count += 1
        elif word in dict_values:
            ru_count += 1
    direction = '2en' if ru_count > en_count else '2ru'

translated_text = translator.translate(direction)
print(f"{text} => {translated_text}\n")

with open('translation.log', 'a', encoding='utf-8') as log_file:
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    original = text
    log_file.write(f"{timestamp} [{direction}] {text} => {translated_text}\n")

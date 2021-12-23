import re

import requests
source = "de"
target = "en"
to_translate = input("Type in the word you'd like to translate.\nDefault translation is {0} to {1}\n"
                     "type in $<source_code>-<destination_code> to get another format.\n"
                     "e.g. $en-de is English to German\n".format(source, target))
if to_translate[0] == '$':
    result = re.search(r'\$(\w\w)-(\w\w)', to_translate)
    if result:
        source = result.group(1)
        target = result.group(2)
        print('Changed the translation format to {0}-{1}'.format(source, target))
        to_translate = input('Sentence to translate:\n')
response = requests.get('https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl={0}&tl={1}&q={2}'.format(
    source, target, to_translate))
if response.status_code == 200:
    translation = re.search('"trans":"([^"]+)"', str(response.content))
    print('Translation:', translation.group(1))
else:
    print('Something went wrong with the translation! :(')
    print(response.content)

"""Description:
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !"""

def pig_it(text):
    text_words = text.split(' ')
    modified = [word[1:] + word[0] + "ay" if word[0].isalpha() else word for word in text_words]
    return ' '.join(modified)
from googletrans import Translator

function=input("""Which one do you want to perform:
a. French to English
b. English to French
c. Spanish to English
d. English to Spanish>>>>""")
print()
text=input("Enter text to translate: ")
if function=="a":
    translator=Translator()
    translated_text=translator.translate(text,src='fr',dest='en')
    print("Translated text from French to English:",translated_text.text)
elif function=="b":
    translator=Translator()
    translated_text=translator.translate(text,src='en',dest='fr')
    print("Translated text from English to French:",translated_text.text)
elif function=="c":
    translator=Translator()
    translated_text=translator.translate(text,src='es',dest='en')
    print("Translated text from Spanish to English:",translated_text.text)
elif function=="d":
    translator=Translator()
    translated_text=translator.translate(text,src='en',dest='es')
    print("Translated text from English to Spanish:",translated_text.text)








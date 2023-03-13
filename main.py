from googletrans import Translator

def rreplace(s, old, new, occurrence):

    li = s.rsplit(old, occurrence)

    return new.join(li)

if __name__ == "__main__":
    inputLocale = 'en'
    outputLocales = ['fr', 'it']

    translator = Translator()
    file = open("input.arb", "r")

    translations = {}
    
    for line in file:
        #Ignore empty lines and brackets
        if(line == '{\n' or line == '}' or line == ''):
            continue

        toTranslate = line.split('": ')[1][1:]
        toTranslate = toTranslate.split('"')[0]    

        print(toTranslate)
    
        for supporedLocale in outputLocales:
            translation = translator.translate(toTranslate, src=inputLocale, dest=supporedLocale)
            newLine = rreplace(line, toTranslate, translation.text, 1)
    
            if(supporedLocale in translations.keys()):
                translations[supporedLocale].append(newLine)
            else:
                translations[supporedLocale] = [newLine]
    
    for key in translations.keys():
        with open("result/app_" + key + ".arb", "w", encoding="utf-8") as f:
            f.write('{\n')
            for line in translations[key]:
                f.write(line)
            f.write('}')
            f.close()
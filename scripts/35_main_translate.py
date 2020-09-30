from translate import Translator
translator= Translator(to_lang="ja") #en es pt zh

try :		
        with open('tot.txt',mode='r') as my_file:
                text=my_file.read()
                translation =	translator.translate(text)
                print(translation)
except FileNotFoundError as er:
	     print('you wrote wrong directory')                

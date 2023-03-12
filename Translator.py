from googletrans import Translator
from bs4 import BeautifulSoup
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os



"""
Sometimes you can encounter an error that your computer disagree with writing on terminal as "pip install library_name"
so you had better write get_ipython() code here then run and refresh the console or you can encountered "AttributeError" 
from Translator() function at the time you should download googletrans 4.0.0rc1 version as writing inside the comment below
"""


#get_ipython().system('pip install googletrans==3.1.0a0')


#----------------------

"""
You must write here document access route into your computer

"""


files_from_folder = r"C:\My Web Sites\one_deep"


use_translate_folder = False

extension_file = ".html"

translator = Translator()
directory = os.fsencode(files_from_folder)


for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith(extension_file):
        html = open(os.path.join(files_from_folder, filename), encoding='utf-8')
        soup = BeautifulSoup(html,"html.parser")
        text_elements = [element for element in soup.find_all(string=True) if element.parent.name not in ['script', 'style']]

        for element in text_elements:

            # Extract the text from the element
            text = element.get_text(strip=True)

            # Skip the element if it's empty
            if not text:
                continue
            # Translate the text

            translated_text = translator.translate(text,dest='hi')
            print(translated_text.origin)
            print(translated_text.text)

            # Replace the text in the element
            element.replace_with(translated_text.text)
            print("done.")
        with open(filename, "wb") as f_output:
            print(filename)
            f_output.write(soup.prettify("utf-8"))
    else:
        pass



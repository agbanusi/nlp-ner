'''This program takes in picture or text format, determines what it is, extract the text and get the amount of errors 
in the document, also outputs the name of the company and location of the address found in the picture or text'''
from nltk.corpus import stopwords #download by python -m nltk.downloader stopwords in the cmd
import nltk #download the tokenizer english by python -m nltk.downloader punkt in the cmd
#before you use pytesseract by google download the api from https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20191010.exe
#then change the type pytesseract.pytesseract.tesseract_cmd = Installed loaction/folder
import pytesseract as pt
from PIL import Image
from gingerit.gingerit import GingerIt
import spacy
import en_core_web_sm #install by python -m spacy download en'
nlp = en_core_web_sm.load()

stop_words = stopwords.words("english")
extensions = ['jpg','png','jpeg']
#picture function
def picture(filename):
    s = Image.open(filename)
    text = pt.image_to_string(s)
    return text
#text function
def txt(text):
    t = text
    return t
#get the words
def word(filename_or_text, final_type):
   try:
       if filename_or_text.rsplit('.',1)[1].lower() in extensions:
           c = picture(filename_or_text)
       else:
           c = txt(filename_or_text)
   except IndexError:
       c= txt(filename_or_text)       
   tok_text = nltk.sent_tokenize(c)
   for s in tok_text:
       tk_txt = nltk.word_tokenize(s) 
   final_text = []
   for i in tk_txt:
       if i not in stop_words:
           final_text.append(i)
   if final_type == 'sentence':
       return tok_text
   elif final_type == 'word':
       return final_text
   else:
       return 'Not applicable'
#check for grammar and spelling errors          
def check(filename_or_text):
    try:
      if filename_or_text.rsplit('.',1)[1].lower() in extensions:
         text = picture(filename_or_text)
         p = GingerIt()
         q = p.parse(text)
         return len(q['corrections'])
      else:
        text = txt(filename_or_text)
        g = GingerIt()
        h = g.parse(text)
        return len(h['corrections'])
    except IndexError:
        text = txt(filename_or_text)
        g = GingerIt()
        h = g.parse(text)
        return len(h['corrections'])
def org(filename_or_text):
    try:
       if filename_or_text.rsplit('.',1)[1].lower() in extensions:
           d = picture(filename_or_text)
       else:
           d = txt(filename_or_text)
    except IndexError:
       d = txt(filename_or_text)  
       
    doc = nlp(d)
    v = []
    for x in doc:
        if (x.ent_type_)  == 'ORG':
            v.append((x))
    comp = ''
    for i in v:
        comp = comp +' '+ i.text
    return comp

def location(filename_or_text):
    loc = word(filename_or_text,'word')
    pos = word(filename_or_text,'sentences')
    locations = ['lagos','abuja','oyo','rivers','abia','adamawa','akwaibom','anambra','bauchi',
                 'benue','borno','cross river','delta','ebonyi','edo','ekiti','enugu',
                 'gombe','imo','jigawa','kaduna','kano','katsina','kebbi','kogi','kwara',
                 'nassarawa','niger','ogun','ondo','osun','plateau','sokoto','taraba','dutse','zamfara','fct']
    place = []
    ff = []
    for i in loc:
        if i.lower() in locations:
            ff.append(i)
            for j in pos:
                if i.lower() in j.lower():
                    place.append(j) 
                else:
                    place = place
        else:
            ff = ff
    return place
            
            
    

    
    
    
    
    
    
        
    


     
       








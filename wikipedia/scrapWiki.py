
# coding: utf-8

# In[1]:


import wikipediaapi
import os
import time
import sys


# In[7]:


wiki_wiki = wikipediaapi.Wikipedia('fr')

try:
    page_py = wiki_wiki.page(sys.argv[1])
except:
    print("page name missing.")
    sys.exit()


# In[11]:


def save_index(index_filename, page_title, directory):
    filename = directory + "/" + index_filename
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.isfile(filename):
        f = open(filename, "w+")
    else:
        f = open(filename, "a", encoding="utf-8")
        print(str(page_title))
        f.write(page_title+"|")
        f.close

def save_page(page_py, directory):
    filename = directory + "/" + str(page_py.title.replace("/","").replace('"',''))
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.isfile(filename):
        try:
            f = open(filename, "wb+")         
            f.write(page_py.text.encode("utf-8"))
            f.close
        except:
            print("!!! ne peux pas sauvegarder le fichier  =>" + str(filename))
    
def print_links(page):
        links = page.links
        for title in sorted(links.keys()):
            print("%s: %s" % (title, links[values]))
            
def clean_word(word_in_title):
    word_in_title = word_in_title.lower().replace(")","").replace("(","").replace("'"," ")
    return str(word_in_title)
    
def is_title_about_informatic(dict_info, words_in_title):
    for word_in_title in words_in_title:
        word_in_title = clean_word(word_in_title)
        if not word_in_title.isdigit():
            if str(" " + word_in_title.replace(" ","") + " ") in dict_info:
#                 print(word_in_title)
                return True
    return False

def is_page_about_informatic(title_page):
    wiki_wiki = wikipediaapi.Wikipedia('fr')
    page_py = wiki_wiki.page(title_page)
    if "Catégorie:Portail:Informatique" in str(page_py.categories.keys()):
        return True
    return False

def is_page_yet_parsed(page_title):
    global page_parsed
    return page_title.replace(" ","").replace(".","").lower() in page_parsed

def inc_page_parsed(page_title):
    save_index("index_file", page_title, ".")
    global page_parsed # Python recherche i en dehors de l'espace local de la fonction
    print("add element : " + page_title.replace(" ","").replace(".","").lower())
    page_parsed.append(page_title.replace(" ","").replace(".","").lower() )
            
def get_urls_from_page(page_py):
    links_from_page=[]
    save_page=False
    try:
        links = page_py.links
    except:
        return []
    for title_page in sorted(links.keys()):
#         print(title_page)
        try:
            save_page = is_page_about_informatic(title_page)
        except:
            save_page = False
        if save_page:  
            links_from_page.append(title_page)
    return links_from_page

def main(page_py):
    inc_page_parsed(page_py.title)
    time.sleep(1)
    print("=> page ===============> " + page_py.title)
    save_page(page_py, "data")
    urls_from_page = get_urls_from_page(page_py)

    for url_title in urls_from_page:
        page_py = wiki_wiki.page(url_title)
        if page_py.exists():
            try:
                save_page(page_py, "data")
            except:
                continue
    for url_title in urls_from_page:
        if not is_page_yet_parsed(url_title):
            
            print("=> page ================not yet parsed ====================> " + url_title.replace(" ","").replace(".","") + "|")
            page_py = wiki_wiki.page(url_title)   
            main(page_py)


# In[12]:


global page_parsed
page_parsed = open("./index_file", "br+")
page_parsed = page_parsed.read().decode("ISO-8859-1")
page_parsed= page_parsed.split("|")
# os.listdir("data")
for idx, item in enumerate(page_parsed):
    page_parsed[idx] = item.replace(" ","").replace(".","").lower()


# In[ ]:


main(page_py)


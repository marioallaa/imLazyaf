from template.documentProject import newDocxDocument
from scrapping.wikipediaScrapper import WikiScrapping


print("""
                                     ***
                    Do you want to change the Language? 
                                     ***    """)

changeLang = input("<y/n>")

if changeLang == 'y' or changeLang == 'Y':
        print("""                             *Im Lazy Aff*
             Chose a language according to ISO language Code 
                        *** default: <en> ***""")
        lang = input("    Language: ")
else:
    lang = 'en'

w = WikiScrapping(lang)
print(w.search(input("    What is Your Topic: ")))
title = input("    Page Title: ")
summary = w.openPage(title)
content = w.getContent()
uri, ref = w.getRef()

d = newDocxDocument(title,
                    input("     For what class do you want this project: "),
                    input("     What Class are You: "),
                    input("     What is Your Name: "),
                    input("     What is Your Teachers Name:"))

d.firstPage()
d.addInfo(summary + " \n \n " + content)
d.addRef(uri, ref)

print("""
                                     ***
            Do you want to save the Document with a specific Name? 
                                     ***    """)

changePath = input("<y/n>")
if changePath == 'y' or changePath == 'Y':
    d.saveDoc(input("Input Your Path: "))
else:
    d.saveDoc()


d.openImg()

h = input('')
d.close()





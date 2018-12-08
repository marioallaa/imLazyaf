from template.documentProject import newDocxDocument
from scrapping.wikipediaScrapper import WikiScrapping

"""
                                        *** 
                                    MIT License

                            Copyright (c) 2018 Mario Alla

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.

                                        ***


"""

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





import wikipedia as w


class WikiScrapping():


    def __init__(self, lang='en'):
        self.title = lang
        w.set_lang(lang)


    def search(self, query):
        self.query = query
        return w.search(query)

    def openPage(self, title):
        self.title = title
        self.page = w.page(self.title)
        self.summ = w.summary(title, 10)
        return self.summ

    def getContent(self):
        self.content = self.page.content
        return self.content

    def getRef(self):

        return self.page.url, self.page.references

    def openImg(self):
        import webbrowser
        url = "https://www.google.com/search?q={0}i&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig99z_ns_eAhWB_ywKHakgAQIQ_AUIDigB&biw=1662&bih=815&dpr=1.13".format([s for s in self.title.split(' ')])
        return webbrowser.open(url)

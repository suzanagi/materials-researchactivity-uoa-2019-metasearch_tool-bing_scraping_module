class ResultItem:
    title = ""
    url = ""
    abstract = ""

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def add_abstract(self, abstract):
        self.abstract = abstract

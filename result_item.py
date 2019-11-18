import re

class ResultItem:
    HIGHESTRANK = 1
    LOWESTRANK = 10

    title = ""
    url = ""
    engine = ""
    rank = 9
    abstract = ""

    def __init__(self, title, url, engine):
        self.title = title
        self.url = url
        self.engine = engine

    def add_rank(self, rank):
        self.rank = rank

    def add_abstract(self, abstract):
        self.abstract = abstract
        
    def get_domain(self):
        head = re.match(r'https?://(([a-zA-Z0-9])+(\.))+([a-zA-Z]{2,})+/', self.url)
        fragments = re.split(r'[\./]', head.group(0))
        return fragments

if __name__ == "__main__":
    # To test the get_domain function
    item = ResultItem("fucking news", "http://www.against.fucking.pusies.wikihow.com/Switch-Tabs-with-Your-Keyboard-on-PC-or-Mac/fucku", "Google")

    domains = item.get_domain()
    print(domains[-3] + "." + domains[-2])


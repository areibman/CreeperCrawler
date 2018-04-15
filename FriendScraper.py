from bs4 import BeautifulSoup
import urllib.request

class Profile:
    def __init__(self, id):
        self.id = id
        self.url = "https://www.facebook.com/search/"+self.id+"/friends/intersect" 
        html_doc = urllib.request.urlopen(self.url).read()
        self.soup = BeautifulSoup(html_doc, 'html.parser')

        noncomment = str(self.soup.find('code',{'id':'u_0_1m'}))[23:-11]
        spans = BeautifulSoup(noncomment, 'html.parser').findAll('span')
        spans = [str(s)[6:-7] for s in spans][:-1]


    def getFriends():
        """
        returns: List of tuples containing Friend name and friend URL
        """
        filter(lambda item: not containsDigit(item), spans)
        # return [(,)]

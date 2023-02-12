from bs4 import BeautifulSoup

def remove_html(text):

    return BeautifulSoup(text).get_text()

def clean(text):

    return remove_html(text).lower()

if __name__ == '__main__':

    f = open('Document.html','rb')

    print(clean(f.read()))

    f.close()



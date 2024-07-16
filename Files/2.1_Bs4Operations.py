from bs4 import BeautifulSoup
def main():
        html_doc = '''
        <html>
        <head>
            <title>All Profiles</title>
        </head>
        <body>
            <a href="/profiles/aphrodite">Aphrodite</a>
        </body>
        </html>
        '''
        soup = BeautifulSoup(html_doc, 'html.parser')

        # Extracting <title> tag
        title_tag = soup.title
        print(title_tag)  
        # Extracting text inside the <title> tag
        title_string = title_tag.string
        print(title_string) 

        # Extracting <a> tag
        a_tag = soup.a
        print(a_tag) 

        # Extracting href attribute
        a_href = a_tag['href']
        print(a_href)  

        # Extracting text inside the <a> tag
        a_text = a_tag.text
        print(a_text)
if __name__ == "__main__":
    main()
    
    
'''
Output:
$ python 2.1_Bs4Operations.py

-->soup.title: <title>All Profiles</title>

-->soup.title.string: All Profiles 

-->a_tag: <a href="/profiles/aphrodite">Aphrodite</a>

-->a_tag['href']: /profiles/aphrodite

-->a_tag.text: Aphrodite

'''  

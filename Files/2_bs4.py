#Basic bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():

        url = "http://olympus.realpython.org/profiles/dionysus"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")  #Creates a BeautifulSoup object (soup) by passing the HTML content (html) and specifying the parser -html.parser- here
        print(soup.get_text())                     #Prints the entire text content of the page


        img_tags = soup.find_all("img")            #Finds all img tags and print their count

        '''find_all:Searches for specific kinds of tags whose attributes match certain values'''
        print("Number of <img> tags found:", len(img_tags))


        for img in img_tags:                       #Prints each img tag's attributes
            print(img)
            
        # print(img1["src"])
        # print(img2["src"])

        for img in img_tags:
            print("src:", img.get("src"))
            

        '''# get() method --with the name of the attribute as a String argument
        -- to retrieve the value of an attribute from an HTML tag'''
        
if __name__ == "__main__":
    main()

    
'''
Output:
$ python 2_bs4.py

-
Profile: Dionysus

Name: Dionysus

Hometown: Mount Olympus

Favorite animal: Leopard

Favorite Color: Wine

-
Number of <img> tags found: 2
<img src="/static/dionysus.jpg"/>     
<img src="/static/grapes.png"/>
-
src: /static/dionysus.jpg
src: /static/grapes.png

'''
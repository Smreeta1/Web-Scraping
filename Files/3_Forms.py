"""
Question:

Use MechanicalSoup to provide the correct username (zeus) and password (ThunderDude) to the login form
located at the URL http://olympus.realpython.org/login.

Once the form is submitted, display the title of the current page to determine that you’ve been redirected to the /profiles page.
"""

import mechanicalsoup
import re

def main():

    # Creating a Browser instance
    browser = mechanicalsoup.Browser()

    # Specify the URL of the login page
    url = "http://olympus.realpython.org/login"

    # Request the login page and parse it with BeautifulSoup
    login_page = browser.get(url)
    page_type=type(login_page.soup)
    login_html = login_page.soup 
    print(login_page)
    print(page_type)
    print(login_html)

    # Fill out the login form
    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"         
    form.select("input")[1]["value"] = "ThunderDude"  

    # Submit the form
    profiles_page = browser.submit(form, login_page.url)
    print(f'Confirmation if directed to "/profile" page:{ profiles_page.soup.title}')

    # Check if the current page title is "All Profiles"
    if re.search("All Profiles", profiles_page.soup.title.string):
        
        '''profiles_page.soup.title is a BeautifulSoup Tag object, 
        not a string.
        profiles_page.soup.title:Gives -->TypeError: expected string or bytes-liala/Webscrapingke object, got 'Tag'
        
        '''
        print("Login Successful!")
    else:
        print("Login Failed!")
        

    # URLs of links on the profiles page
    base_url = "http://olympus.realpython.org" 
    links = profiles_page.soup.select("a")

    print ('All links on profiles_page are:')
    for link in links:
        address = base_url + link["href"]
        print (address)
if __name__ == "__main__":
    main()      

''' 
Output:
$ python 3_Forms.py
<Response [200]>
<class 'bs4.BeautifulSoup'>
<html>
<head>
<title>Log In</title>
</head>
<body bgcolor="yellow">
<center>
<br/><br/>
<h2>Please log in to access Mount Olympus:</h2>
<br/><br/>
<form action="/login" method="post" name="login">
Username: <input name="user" type="text"/><br/>
Password: <input name="pwd" type="password"/><br/><br/>
<input type="submit" value="Submit"/> 
</form>
</center>
</body>
</html>

Confirmation if directed to "/profile" page:<title>All Profiles</title>     
Login Successful!
All links on profiles_page are:       
http://olympus.realpython.org/profiles/aphrodite
http://olympus.realpython.org/profiles/poseidon
http://olympus.realpython.org/profiles/dionysus
'''



'''
#General Steps for Mech soup:
1.Install: pip install MechanicalSoup.
2.Initialize: Create a Browser() instance.
3.Fetch: Use browser.get(url) to get a webpage.
4.Interact: Fill and submit forms with browser.submit(form).
5.Parse: Access HTML content with response.soup.
6.Navigate: Find and handle <a> tags for URLs.
'''
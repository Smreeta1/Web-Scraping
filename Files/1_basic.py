from urllib.request import urlopen
def main():
        #Fetch URL
        url = "http://olympus.realpython.org/profiles/aphrodite"

        #Fetch webpage
        page = urlopen(url)

        #Read & decode HTML content
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        #Print HTML content
        print(html)

        # Find title index
        title_index = html.find("<title>") 
        start_index=title_index + len("<title>")
        end_index = html.find("</title>")
        title = html[start_index:end_index]

        # Print the extracted titles
        print("Title:", title)
if __name__ == "__main__":
            main()
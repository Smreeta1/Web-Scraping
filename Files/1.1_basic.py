#Using built_in py method
import requests
def main():

        # Making a GET request
        r = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')

        print(r)  #prints the response object with the status code

        print(r.content)    # prints the raw binary content of the response in bytes
        print(r.text) #prints the content of the response as a string(more readable and easier)
if __name__ == "__main__":
    main()
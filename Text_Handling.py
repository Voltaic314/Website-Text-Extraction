import requests
from bs4 import BeautifulSoup


def is_website_up(url: str) -> bool:
    '''
    This function pings the url's server to see if 
    the website is up and running.

    Parameters: 
    url: any website url string you wish to test like google.com

    Return: Bool - True if the website is up and running.
    '''
    response = requests.get(url)
    return response.status_code == 200


def extract_website_text(url: str) -> str:
    '''
    This function extracts the text from the given url using 
    the requests and beautiful soup library. 

    Parameters:
    url: string of url name like google.com for example

    Return: string of text from the url
    '''
    website_is_up = is_website_up(url)
    if website_is_up:

        # Send an HTTP GET request to the URL
        response = requests.get(url)

         # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Specify the elements to exclude (e.g., headers, 
        # footers, ads) based on HTML tags, classes, or attributes
        elements_to_exclude = ["header", "footer", "aside", 
                               "script", "style"]
    
        for tag in elements_to_exclude:
            for element in soup.find_all(tag):
                element.extract()  # Remove the element from the soup
        
        # Extract all the text from the parsed HTML
        return soup.get_text()
 

def write_text_to_file(text_to_write: str, text_filename: str) -> None:
    '''
    This function just writes whatever text you want to the text file.
    Specifically it appends the text rather than overwriting the file.

    Parameters: 
    text_to_write: string of whatever text you want to write to the file
    text_filename: string of whatever the text filename will be. like example.txt
    
    Return: None
    '''
    # Create or open a text file and save the extracted text to it
    with open(text_filename, "a", encoding="utf-8") as text_file:
        text_file.write(text_to_write)
        print(f"Text extracted and saved to {text_filename}")

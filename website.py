'''
Author: Logan Maupin

This module contains the website class that will hold certain meta data
about the website including it's <p> text from the HTML tags, and its domain name.
'''
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from chat_gpt import ChatGPT


class Website:

    def __init__(self, url: str) -> None:
        self.url = url
        self._last_checked = None  # To keep track of the last time the website status was checked
        self._is_up_cache = None  # To store the cached status

    @property
    def is_up(self) -> bool:
        '''
        This checks the website's status to see if it's up but doesn't check it unless
        it has been after 5 minutes of the last cached query.

        returns: bool - True if the response code was 200 within the last check
        '''
        if (
            self._last_checked is None
            or datetime.now() - self._last_checked > timedelta(minutes=5)  # Adjust the time interval as needed
        ):
            # If the website status hasn't been checked or it's been more than 5 minutes, check again
            response = requests.get(self.url)
            self._is_up_cache = response.status_code == 200
            self._last_checked = datetime.now()

        return self._is_up_cache
    
    @property
    def domain_name(self) -> str:
        '''
        This will return a string of the domain name from the url. 
        '''
        if self.is_up:
            parsed_url = urlparse(url=self.url)
            if parsed_url:
                return parsed_url.hostname

    @property
    def extracted_text(self) -> str:
        '''
        This function extracts the text from the site url using 
        the requests and beautiful soup library. 

        Parameters:
        url: string of url name like google.com for example

        Return: string of text from the url
        '''
        website_is_up = self.is_up
        if website_is_up:

            # Send an HTTP GET request to the URL
            response = requests.get(self.url)

            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Find all <p> (paragraph) tags in the HTML
            paragraph_tags = soup.find_all("p")
            
            # Extract the text from the paragraph tags and join them into one string
            extracted_text = " \n".join(tag.get_text(strip=True) for tag in paragraph_tags)        
            
            cleaned_text = " \n".join(line.strip() for line in extracted_text.splitlines() if line.strip())
            return cleaned_text
        
    @property
    def summary(self) -> str:
        summarizer = ChatGPT(nick_name="Study Bot")
        char_limit_for_discord = 2_000
        if ChatGPT.text_needs_to_be_broken(self.extracted_text):
            separated_text = ChatGPT.break_up_text(self.extracted_text)
            return summarizer.summarize_text_separated(separated_text, char_limit=char_limit_for_discord)

        else:
            return summarizer.summarize_text(text_to_summarize=self.extracted_text, char_limit=char_limit_for_discord)
    
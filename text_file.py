'''
Author: Logan Maupin

This module contains the text file class object.
'''
from website import Website


class TextFile():

    def __init__(self, filename='', url='') -> None:

        '''
        This creates an instance of the text file object, with optional parameters.

        Parameters:
        filename: str - optional string of the filename you wish to use for a custom filename
        url: str - url you wish to get extracted text from.
        '''
        self.filename = filename
        self.url = url
        if url:
            website = Website(url=self.url)
            self.website = website
            if not filename:
                self.filename = f'{self.website.domain_name}.txt'


    @property
    def header(self) -> str:
        '''
        This function takes the url and extracts the domain name from it,
        i.e. google.com into Google, then it will add that to a formatted
        header text string to add to the top of each file entry. 

        Parameters:
        url: any url string like 'google.com' for example.
        
        Return: header string to add to the top of a 
        text file with the domain name.
        '''
        website_name = self.website.domain_name
        header_padding = '-'*25 + '\n'

        output_string = header_padding
        output_string += f'The information comes from: {website_name} at {self.url}\n'
        output_string += header_padding

        return output_string
    
    def add_summary_to_header(self) -> None:
        '''
        This method will modify the header text to include a LLM AI summary of the website text.
        '''
        header_padding = '-'*25 + '\n'
        header_text_to_be_added = header_padding
        header_text_to_be_added += header_padding
        header_text_to_be_added += f"The following is a summary of the website text from ChatGPT: \n"
        header_text_to_be_added += self.website.summary + "\n"
        header_text_to_be_added += header_padding
        header_text_to_be_added += f"Here is the text from the website itself: \n"

        self.header += header_text_to_be_added

    @property
    def current_file_text(self) -> str:
        '''
        Returns a string of all the text in the text file. :)
        '''
        txtfile = open(self.filename, mode='r', encoding='UTF-8')
        text = ' '.join(txtfile.readlines())
        txtfile.close()
        return text

    @property
    def is_empty(self) -> bool:
        '''
        Returns whether the text file contains some text already or not. :)
        '''
        return bool(self.current_file_text)

        
    def write_text_to_file(self, text_to_write='') -> bool:
        '''
        This function just writes what text you want to the text file.
        Specifically it appends the text rather than overwriting the file.

        Parameters: 
        text_to_write: str - what text you want to write to the file

        Returns: True if the text was successfully written to the file
        '''

        if not text_to_write:
            text_to_write = self.website.extracted_text
        # Create or open a text file and save the extracted text to it
        with open(self.filename, "a", encoding="utf-8") as txtfile:
            txtfile.write(self.header)
            txtfile.write(self.website.extracted_text)

        if self.website.extracted_text in self.current_file_text:
            print(f"Text extracted and saved to {self.filename}\n")
            return True
        
        else:
            print(f"Text could not be written to {self.filename}\n")
            return False
'''
Author: Logan Maupin

This module contains the text file class object.
'''


class TextFile:

    def __init__(self, filename='') -> None:

        '''
        This creates an instance of the text file object, with optional parameters.

        Parameters:
        filename: str - optional string of the filename you wish to use for a custom filename
        url: str - url you wish to get extracted text from.
        '''
        self.filename = filename

    @property
    def current_file_text(self) -> str:
        '''
        Returns a string of all the text in the text file. :)
        '''
        with open(self.filename, mode='r', encoding='UTF-8') as txtfile:
            return ' '.join(txtfile.readlines())

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
        # Create or open a text file and save the extracted text to it
        with open(self.filename, "a", encoding="utf-8") as txtfile:
            txtfile.write(text_to_write)

        if text_to_write in self.current_file_text:
            print(f"Text extracted and saved to {self.filename}\n")
            return True
        
        else:
            print(f"Text could not be written to {self.filename}\n")
            return False

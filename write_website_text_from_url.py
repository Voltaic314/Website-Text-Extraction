'''
Author: Logan Maupin
Date: 09/17/2023

This python module utilizes the collection of class objects we've defined
to write a text file to the current working directory with the <p> text from
a website, with an option to summarize the data from chatGPT. 
'''
from text_file import TextFile
    

def user_input_txt_filename() -> str:
    '''
    This function is a while loop that asks the user whether or not
    they wish to provide their own filename to write to or not.

    Return: filename or '' if not.
    '''
    while True:

        # ask the user if they wish to provide a filename or not:
        custom_filename_input = input("Do you wish to use a custom filename to write to? (y/n): ").lower()
        if custom_filename_input not in ['y', 'n']:
            continue

        elif custom_filename_input == 'y':
            custom_filename = input("Please input the filename you wish to use: ").strip()
            
            if '.txt' in custom_filename.lower():
                return custom_filename
            
            else: 
                custom_filename += '.txt'
                return custom_filename
        
        elif custom_filename_input == 'n':
            return ''
        

def get_yes_or_no(prompt: str) -> bool:

    while True:

        user_input = input(prompt).lower()

        if user_input in ['y', 'n']:

            if user_input == 'y':
                return True
            
            elif user_input == 'n':
                return False

        else:
            print("I'm sorry, your input should be either 'y' or 'n'.")
            continue


def does_user_want_summary() -> bool:
    summary_question = "Would you like this extraction to include a text summary from ChatGPT? (y/n) "
    return get_yes_or_no(summary_question)


def get_url() -> str:
    return input("Please enter the url of the website you wish to extract text from: \n")


def main():
    '''
    This function defines the order in which to use all the functions
    as an example of how one would get the text and write it to a file.
    '''
    custom_filename = user_input_txt_filename()
    txt_file = TextFile(url=get_url(), filename=custom_filename)
    
    user_wants_summary = does_user_want_summary()
    if user_wants_summary:
        txt_file.add_summary_to_header()

    txt_file.write_text_to_file()


if __name__ == "__main__":
    main()
    
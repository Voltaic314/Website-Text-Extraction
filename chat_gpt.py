'''
Author: Logan Maupin

This module utilizes the G4F (GPT 4 Free) library, with the gpt-3.5-turbo LLM
for various purposes. In this specific repo, it will be used to summarize text
from articles where we have extracted the </p> from. 
'''
import g4f
from time import sleep


class ChatGPT:

    def __init__(self, nick_name='') -> None:
        self.model = "gpt-3.5-turbo"

        if nick_name:
            self.nick_name = nick_name
            self.initial_prompt = f"I will call you {self.nick_name} instead. "
        
        else:
            self.initial_prompt = ''

    def ask(self, message: str) -> str:
        '''
        This function uses chat completion with the gpt-3.5-turbo model
        to get a response from ChatGPT based on whatever input prompt 
        (message) that you gave it. 

        Parameters:
        message: str - message prompt you wish to give the GPT model

        Returns: str - response back from the AI.
        '''
        if self.initial_prompt:
            message = self.initial_prompt + message

        response = g4f.ChatCompletion.create(
        model=self.model,
        messages=[{"role": "user", "content": message}],
        )
        return response
    
    @staticmethod
    def text_needs_to_be_broken(text) -> bool:
        '''
        text needs to be split apart if the character length is greater than
        or equal to 20,000 characters. So it will return True if that's the case.
        '''
        return len(text) >= 20_000

    @staticmethod
    def break_up_text(text_to_break_apart: str) -> list[str]:
        '''
        This function will split up the text into sections of 250 words at a time.

        Returns: list[str] - where each element is a string of 250 words.
        '''
        split_text = text_to_break_apart.split()
        
        separated_list = []
        word_list = []
        for index, element in enumerate(split_text):
            if index % 100 or index == len(split_text) - 1:
                joined_string = ' '.join(word_list)
                separated_list.append(joined_string)
                word_list.clear()

            else:
                word_list.append(element)
                    
    
    def summarize_text(self, text_to_summarize, char_limit=0) -> str:
        '''
        This function summarizes website text from a specific prompt to the AI.
        All you need to do is pass in the website url string for it to complete
        the request. Note: this only looks at the website's </p> HTML tags. If
        the text you wish to extract is not in these tags, this won't work.

        Parameters: 
        website_url: str of the website url you wish to have summarized for you.
        
        Returns: str - summary from the AI.
        '''

        prompt = 'Can you please summarize this website\'s text for me?\n'

        if char_limit:
            prompt += f'Also wtihin a limit of {char_limit} characters? '

        prompt = prompt + f"Here is the website's text: \n\n{text_to_summarize}\n\n"

        prompt += """In your response, pretend I didn't ask you a question, 
just give me only the summary text and nothing else. Thank you so much!"""

        return self.ask(prompt)
    
    def summarize_text_separated(self, text_list: list[str], char_limit=0) -> str:
        prompt = 'Can you please summarize this website\'s text for me?\n'

        if char_limit:
            prompt += f'Also wtihin a limit of {char_limit} characters? '

        prompt += "Note: I can't send all the text at once so it will come in sections of 250 words at a time. I'll let you know once I've sent the last section! "

        prompt += "Please only summarize the website in your last response once I have sent the last section. Okay? "
        first_response_without_any_text_sent_yet = self.ask(prompt)
        responses = [first_response_without_any_text_sent_yet]
        for index, string in enumerate(text_list):
            if index == 0:
                prompt = "Okay here is the first section: \n"

            elif index == len(text_list) - 1:
                prompt = 'Okay that was the last section of words. Please summarize what that text said for me. \n'

            else:
                prompt = "Here is the next section: \n"

            response = self.ask(prompt + string)
            sleep(5)
            responses.append(response)

        return responses[-1]

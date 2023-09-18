import tiktoken


def get_token_amount(text: str, model_name: str) -> int:
    '''
    The purpose of this function is to take an input string of text
    and a specified open AI model and extract how many tokens it is
    for pricing purposes.

    Parameters: 
    text: input text you wish to extract token amount from
    model_name: the specified model name you wish to analyze the tokens for

    Return: Token amount integer
    '''

    # FIXME: This currently doesn't actually work because I'm not 
    # smart enough to know what the actual way to do this is lol
    tokenizer = tiktoken.Tokenizer(model_name)
   
    # Tokenize the text and count tokens
    tokens = tokenizer.count_tokens(text)
    print(f"Number of tokens in the text: {tokens}")
    return tokens


def calculate_price(token_amount: int, price_conversion: float) -> float:
    '''
    This function takes 2 arguments. the amount of tokens and the price conversion float.
    It then outputs the rounded (to 2 decimals) output of how many dollars it would roughly
    cost to process by a language model given Open AI's pricing.

    Parameters: 
    token_amount: the amount of tokens you wish to process, this should be an integer.
    price_conversion: Typically a float like 0.002 for the davinci-002 model for example.

    Returns: Float rounded to 2 decimals of how much money it should cost to process.
    '''
    raw_amount = token_amount * price_conversion
    rounded_amount = round(raw_amount, 2)
    print(f'Cost of input text: {rounded_amount}')
    return rounded_amount
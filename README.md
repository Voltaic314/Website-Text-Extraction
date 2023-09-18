# Website-Text-Extraction
This extracts the text from a website. Ideal for passing it into a language model for processing and summarization. 

This repository is a collection of scripts used to help with extracting body text from a website (like an article) and then writing it to a text file.

This text can then be passed into an LLM of your choosing to summarize the text, train it, whatever you want. I intended to use this for finance related purposes.
Like summarizing an article posted for investors or summarizing a new news article to help with trading algorithms. 

Ideally in a perfect world you'd get real world news from a news API of some kind, that would be much faster and more efficient than parsing and summarizing all of the HTML body text of a website.

Unfortunately, I don't know enough about ML AI to actually do the last part, but I at least have the part of extracting text and writing a text file done at least. 

Something that needs to be fixed for LLM purposes though is that the token counter seems to be broken in the price calculator script. Maybe someone else smarter than me can fix that. lol 

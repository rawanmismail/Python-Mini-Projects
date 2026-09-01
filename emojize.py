import emoji

user_input = input("Input: ")


output = emoji.emojize(user_input, language ='alias')
"""
emoji.emojize(...): This is a pre-made function inside the emoji library. 
It scans a piece of text looking for words surrounded by colons (like :money_bag:) 
and swaps them out for the actual emoji character (💰).

user_input: This tells the function which text to scan (the text we just got from the user in Line 2).

language="alias": This is an extra setting. 
By default, the library only understands official names (like :thumbs_up: with an underscore). 
Adding language="alias" tells it: "Also recognize short versions or nicknames (aliases) like :thumbsup: 
without the underscore."

Finally, the converted result (with real emojis) gets saved into the variable output.
"""


print("Output:", output)


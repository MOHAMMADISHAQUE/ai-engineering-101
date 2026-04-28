# Tokenizing input token 

import tiktoken 

enc = tiktoken.encoding_for_model("gpt-4o")


text = "Hey there! My name is Ishaque"


token = enc.encode(text)

print("Tokens" , token)
# Tokens [25216, 1354, 0, 3673, 1308, 382, 357, 20531, 1126]

# De-tokenizing
decoded = enc.decode([25216, 1354, 0, 3673, 1308, 382, 357, 20531, 1126])

print("Decoded Token", decoded)
import requests
url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
response = requests.get(url)

with open("input.txt",'wb') as file:
    file.write(response.content)
    
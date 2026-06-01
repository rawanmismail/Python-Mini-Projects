emoticon = '[^_^]'

def main():
    global emoticon
    say('Hello world')
    say('Goodbye world')

def say(phrase):
    print(phrase + ' ' + emoticon)

main()
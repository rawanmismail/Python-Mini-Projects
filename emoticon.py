emoticon = '[^_^]'

def main():
    global emoticon
    say('Hello world')
    emoticon = '[T_T]'
    say('Goodbye world')

def say(phrase):
    print(phrase + ' ' + emoticon)
main()
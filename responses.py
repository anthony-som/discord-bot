from random import choice, randint

def get_response(user_input:str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Well, you\'re silent. I guess I\'ll be too.'
    elif 'hello' in lowered or 'hi' in lowered:
        return 'Hello there!'
    elif 'bye' in lowered or 'goodbye' in lowered:
        return 'Bye bye!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'bam' in lowered:
        return 'BAM!'
    else:
        return choice(['Wakarimasen', 'I don\'t understand', 'I\'m sorry, I don\'t know what you mean'])
    
    

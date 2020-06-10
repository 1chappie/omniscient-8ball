import sys
import Lib.random as ran

answers = ()
answers_file = None

def get_txt():
    global answers_file
    try:
        answers_file = open("the8ball_answers.txt", "r")
    except IOError:
        with open("the8ball_answers.txt", "w") as answers_file:
            answers_file.write( 
'''Not really.
Yeah, I don't think so.
I don't buy your shenanigans.
Nah.
Fuck no.
Yep.
I guess so.
Sure.
Never heard something more true.
Obviously.'''       )
        answers_file = open("the8ball_answers.txt", "r")

def refresh_answers():
    global answers
    if answers_file is None: get_txt()
    answers_file.seek(0)
    answers = answers_file.readlines()

def random_answer(seed=None):
    refresh_answers()
    if seed is None or seed[-1:]!='?': return 'I expect a question, mortal.'
    ran.seed(seed)
    try:
        return answers[ran.randint(0, len(answers) - 1)]
    except ValueError:
        return "I'm out of answers at the moment. Maybe you could give me some?"
    
if __name__ == '__main__':
    str_argumente = " ".join(sys.argv[1:])
    print(random_answer(str_argumente))
import random

def random_joke():
    options = ["why do programmers prefer dark mode? because light attracts too many bugs", "why do Java developers wear glasses? because they don't see sharp", "what's a programmer's favourite hangout place? foo bar" ,"why did the programmer quit his job? he didn't get arrays"]
    computer_choice = random.choice(options)

    return computer_choice
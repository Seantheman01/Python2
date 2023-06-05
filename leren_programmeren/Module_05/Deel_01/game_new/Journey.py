from game_storyline import storyline
from game_plaatjes import plaatjes
from game_over import game_over

naam = input("""---------- Welcome to Journey! ----------
Before we start, what is your name? """)
intro = input(f"""Hello {naam}! Here are some tips: you start off with 100 coins,
and one of the first paths is harder than the other.
That is all you need to know for now. 
Good luck on your journey! Are you ready? (just type 'yes or no') """)
if intro == 'no':
    print("Then why are you playing this?")
elif intro == 'yes':
    print(plaatjes[0])
    begin = input(storyline[0]) 
    if begin == 'forest':
        print(plaatjes[1])
        pad1 = input(storyline[1])
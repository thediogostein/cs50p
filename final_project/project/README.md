# TOP TRUMPS OLD CARS
#### Video Demo:  <https://youtu.be/rM-8xXZDLt8>
#### Description:
Presenting a Python-based Top Trumps game that is structured across two essential files: "project.py" and "print_helpers.py." In this design, the "project.py" file encapsulates the core logic of the game, while the complementary "print_helpers.py" file is specifically designated for handling print functions. This intentional separation serves a dual purpose—ensuring clarity in the main file and preventing it from succumbing to unnecessary clutter.

Now, let's delve into the mechanics of the game:

1. **CSV Download and Data Loading:**
   - Initiate the game by downloading a CSV file containing card values.
   - Load these card values into memory, creating a list of dictionaries to represent the deck of cards.

2. **Shuffling and Distribution:**
   - The deck of cards, now structured as a list of dictionaries, undergoes a strategic shuffle.
   - Half of the shuffled deck is allocated to the player, while the other half is reserved for the AI opponent.

3. **Rounds and Card Collection:**
   - Engage in competitive rounds, vying for victory to amass a collection of cards.
   - The winner of each round claims the cards involved, gradually accumulating a strategic advantage.

4. **Game Conclusion:**
   - The game unfolds until one player depletes their card reserves, marking the conclusion of the gameplay.

5. **Determining the Ultimate Victor:**
   - The ultimate victor emerges as the player who successfully accumulates all the cards.

Currently, the game abstains from addressing tie scenarios. However, it's noteworthy that the card values are deliberately unique, mitigating the possibility of tied rounds. Subsequent updates may introduce mechanisms to handle tie scenarios, offering an enhanced and nuanced gaming experience. Dive into the world of this uncomplicated yet engaging Top Trumps game, and relish the strategic pursuit of card mastery!

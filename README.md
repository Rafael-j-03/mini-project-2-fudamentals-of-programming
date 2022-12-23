# FP1 - Mini Project 2

### Objective of the Project:

Implement a game called "Comets" in pygame with the detailed rules and also the implementation of a leaderboard at the end of the game.
## Developers

- [@Rafael-j-03](https://github.com/Rafael-j-03)
- [@rodgoe](https://github.com/rodgoe)
## How our project was organized

- The code production was mostly done by Rafael José, Rodrigo Gomes also contributed to it, helping to solve some problems and some logical systems. The README.md was mostly done by Rodrigo Gomes, in which Rafael José helped composed some more information.

- 1st commit - Start screen; - Rafael José - 22202078

- 2nd commit - First Game Screen and player's ship with movements; - Rafael José - 22202078

- 3rd commit - Bullets, asteroids and wrap-around movements implemented; - Rafael José - 22202078

- 4th commit - Collisions between bullets and asteroids as well as asteroids and the player implemented; - Rafael José - 22202078

- 5th commit - Added the correct images for each object; - Rafael José - 22202078

- 6th commit - Implemented the player's score and "Game Over" screen; - Rafael José - 22202078

- 7th commit - Added the leaderboard with scores; - Rafael José - 22202078

- 8th commit - Setting the leaderboard to properly appear on screen for 6 seconds; - Rafael José - 22202078

- 9th commit - Solved a bug in the initials input on the leaderboard. - Rafael José - 22202078

- 10th commit - README.md implemented - Rodrigo Gomes - 22201252

- [Git Repository](https://github.com/Rafael-j-03/mini-project-2-fudamentals-of-programming)
## Development of our work

### How we organized our code

- On the top we have set the screen and some variables, like the middle of the screen, on the x and the y, the path to our game assets, and some colors.

- After we set the player's class which contain the some variables and start position, and functions to turn left and right, propulsion and his deceleration over some time, depending on the speed, a simple 'get score', his position update, which includes a wrap-around, and function to reset it.

- In this game the player can also shoot at the asteroids on the screen and for that we had to set the position from when it leaves the player's tip until it reaches an asteroid, or if it reaches one of the edges of the screen it can wrap around allowing the bullet to remain on the screen;

- Next we determined the class the asteroids consisting on tree types: small, medium and big and with that we had to adjust their sizes. As for their speeds we set a function for it to be random for each asteroid. Also as with any other object if it its one of the limits of the screen wrap around if necessary;

- Then we adjusted the start screen of the game with the description "Comets" and also the option to "start", that leads us to the game, and "exit" that closes the game;

- When the game starts we have 2 big asteroids on the screen, if that asteroids got shoot by a player's bullet it turns to 3 medium asteroids, and if that asteroid is shot it turns to 5 small asteroids;

- Another component we had to include on the game screen is the score count for how many points the player is making for destroying the asteroids, each on of them gives a certain score depending on the asteroid size;

- While the player is alive some component need to be updated such the player himself, which includes the score, the asteroids and the bullets on the screen, all of this to check the position of each on of them, so he can check collisions;

- The keyboard inputs were also needed for when the player is moving and shooting, and also for the menus to select to start the game and or exit, or for putting his initials on the  leaderboard;

- When its game over a "Game Over" screen message appears for 2 seconds, and after that it is the leaderboard where if the player got a better score than the 10 best scores, that are stored in the .txt file, has to input the first 3 initials by choice so that it can appear after on the leaderboard score;

- The leaderboard is displayed for 6 seconds, in order by which player achieved the best score that appears on top in the first position and so on, the initials of each player are also displayed in upper cases;

- After the leaderboard screen we created a loop to return to the beginning menu, and the game can continue if the player wants so, or he can easily go out by choosing the 'exit' option on the start screen, or by or by clicking the 'x' of the window.
  
## References

- We import tow external libraries, random and math.

- The "random" like the article about it says "This module implements pseudo-random number generators for various distributions.
For integers, there is a uniform selection from a range. For sequences, there is a uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.". And we used it to get random numbers mostly for the dices system.

- The "math" like the article about it says "This module provides access to the mathematical functions defined by the C standard.
These functions cannot be used with complex numbers; use the functions of the same name from the cmath module if you require support for complex numbers. The distinction between functions which support complex numbers and those which don’t is made since most users do not want to learn quite as much mathematics as required to understand complex numbers. Receiving an exception instead of a complex result allows earlier detection of the unexpected complex number used as a parameter, so that the programmer can determine how and why it was generated in the first place."

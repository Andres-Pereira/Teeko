# Teeko
 
We created our own teeko version that can be played with 2 real players or the computer as an opponent.
The game will show a 5x5 matrix that will be representing our board, each space will be called a cell.
The number 1 will be representing the black markers, the number 2 the red ones.
The number 0 is defined as a blank space, that means that either 1 or 2 can mark.
A match will have his own board and functions to make sure that the game follows the rules.

The rules of the game are in the link below:

https://bonaludo.com/2016/07/27/teeko-a-game-and-a-masterpiece-of-john-scarne-the-wizard-of-games/

### Usage Guide

To run the game to play between 2 real players you must run the file: Main.py 

To run the game with an AI with MinMax with depth algorithm you must run the file: PlayerVsla2.py

To run the game with an AI with MinMax with depth and alpha-beta prunning algorithm 
you must run the file: PlayerVsla.py

### AI Solution

##### Heuristic function

For our heuristic function we take 2 principal ideas:

- How many markers of the same color are arranged together in order they can win(vertical, horizontal, square and diagonal arrangements).

We evaluate if there are 2 or 3 consecutive markers of the same color in a winning direction. 
When we have 2 consecutive markers in a winning direction we will recompense the player with 5 points in the utility function.
When we have 3 consecutive markers in a winning direction we will recompense the player with 10 points in the utility function.

Let's see some examples: 

                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]

In this state we can see that we have two black markers in a vertical position. If this happens we give max +5.
This also would happen if the markers are in a diagonal or horizontal direction.

                [0, 2, 0, 0, 0],
                [0, 0, 2, 0, 0],
                [0, 0, 0, 2, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]

In this case the min player will be recompensed with -10.

                [0, 2, 0, 0, 0],
                [0, 2, 2, 0, 0],
                [0, 0, 0, 2, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]

If we have more than one winning direction, in this case we have a vertical, horizontal and diagonal consecutive arrangement, 
we will recompense min with the sumatory of the consecutive directions. -5(horizontal) -5(vertical) -5(diag) = -15 extra points for this state.


- Assignation of values on our board.

We defined the board with the following values:

                [0, 1, 0, 1, 0],
                [1, 2, 2, 2, 1],
                [0, 2, 3, 2, 0],
                [1, 2, 2, 2, 1],
                [0, 1, 0, 1, 0]
            
That means that if min locates at position B2 he will have -2, and if max locates on C3 he will get +3. This because we multiply the
player value(-1 for min +1 for max) with the position value. When all markers are placed we evaluate their position values and get them
together in order to get the utility function for the state.

Let's imagine we have this board:

                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]

For this board the utility value is 5.

A real example, adding the opponent:

                [0, 1, 0, 2, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 2, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 2, 0, 2, 0]

The value of max is 5, the value for min is 6 which means that the utility value for this state is -1.
This means that this state gives min a slight advantage over max.

Now, how do we assign this values to the board?

 Our logic is that the positions with the highest value are the ones that can move to more directions and also the ones that can
 escape easily of an enemy blocking. If we see, some positions like the edges have the worst values, this because they can move
 in less directions and the directions they can place another marker is only at the front of this position. With that explained we can 
 also deduce that the center position has the highest value.

- A terminal value if there is a winner.

When a winner is found on a determinate state, we automatically assign the highest utility value which is 100. 
In that case if the AI sees that his opponent can have the max value, it will interfere.

    winner = state.match.checkWinner() // Returns +1 or -1 depending of the winner, returns None if no one won still.
            if winner != None: 
                return 100 * state.match.checkWinner()


All this parts that we explained are considered to get an improved heuristic function that will analyze the marker's position,
the consecutive markers on a winning direction and if there is a match winner. All this parts can add or subtract an amount to
the utility function of a state. The utility state will define if the state favors min or max.

##### Experiments

First we implemented the MinMax algorithm, this crashed multiple times because the recursive calls where exceeded, the problem
with the original algorithm is that this expands the states until they reach a leave, for this game it gets inefficient and even
impossible to compute so many states. We also tried to use alpha-beta prunning with this algorithm and the results where the same.
This algorithm maybe can work out with an application that has less possible states. We couldn't make the game perform completely without
some errors, even having our heuristic returning logical values and our functions tested individually we found ourselves with some bugs
that make the AI disobey the rules of the game, somehow the AI responds making random and unestablished actions, we expect it's about a 
little bug we need to correct in our possible actions. With this said, we can't realize the experiments we expected, but still we want
to share that testing our AI to perform an individual action in response to a state we saw that without alphabeta prunning
takes almost the double amount of time in responding than with alpha beta.
We want to make clear that the programs are actually working and without crashing but the rules aren't been respected and the moves
the AI makes are illogical, still, is a runnable program and can take smart decisions in a decent response time.


##### Conclusion

We did at least experienced in our experiments testing the program and performing individual actions
how the depth will define the speed of the AI answer, we know that the more levels we expand, the more 
intelligent and predictable our program is. But also this can make the program take too long to return an answer,
or it can also crash the program itself. For a 1v1 game a long response time is not optimal, we can't be waiting that long
for the computer to perform. That doesn't mean that we will have to conform with an unintelligent program, we can see that 
our heuristic function and how it works will also define how optimal are the decisions that the program perform. We can tell
this by the experiments we made to check the utility and how this affected the decisions the algorithm made.


##### Authors: 
##### Andres Pereira - Harold Muyba
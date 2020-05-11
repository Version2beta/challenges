# Some practice coding problems

## N Queens problem

GIVEN:

* a size `(r, f)` where
    * `r` represents the number of ranks
    * `f` represents the number of files on a chess board
* `n` number of Queens

RETURN:

* a matrix `r` x `f` with a `1` at each location representing the valid placement of a Queen and `0` at each remaining location where the valid placement of a Queen indicates that no Queens is in check from another Queen.
* If no valid arrangement exists, return an empty matrix [].

## Darts - [Euler problem 109](https://projecteuler.net/problem=109)

In the game of darts a player throws three darts at a target board which is split into twenty equal sized sections numbered one to twenty.

The score of a dart is determined by the number of the region that the dart lands in. A dart landing outside the red/green outer ring scores zero. The black and cream regions inside this ring represent single scores. However, the red/green outer ring and middle ring score double and treble scores respectively.

At the centre of the board are two concentric circles called the bull region, or bulls-eye. The outer bull is worth 25 points and the inner bull is a double, worth 50 points.

There are many variations of rules but in the most popular game the players will begin with a score 301 or 501 and the first player to reduce their running total to zero is a winner. However, it is normal to play a "doubles out" system, which means that the player must land a double (including the double bulls-eye at the centre of the board) on their final dart to win; any other dart that would reduce their running total to one or lower means the score for that set of three darts is "bust".

When a player is able to finish on their current score it is called a "checkout" and the highest checkout is 170: T20 T20 D25 (two treble 20s and double bull).

There are exactly eleven distinct ways to checkout on a score of 6:

```
D3 	  	 
D1 	D2 	 
S2 	D2 	 
D2 	D1 	 
S4 	D1 	 
S1 	S1 	D2
S1 	T1 	D1
S1 	S3 	D1
D1 	D1 	D1
D1 	S2 	D1
S2 	S2 	D1
```

Note that D1 D2 is considered different to D2 D1 as they finish on different doubles. However, the combination S1 T1 D1 is considered the same as T1 S1 D1.

In addition we shall not include misses in considering combinations; for example, D3 is the same as 0 D3 and 0 0 D3.

Incredibly there are 42336 distinct ways of checking out in total.

How many distinct ways can a player checkout with a score less than 100?

## Shortest path for a Knight

Given
* a standard chessboard
* an origin
* and a destination

Return the shortest path a Knight can take from the origin to the destination

## Wandering Robot [Euler problem 575](https://projecteuler.net/problem=575)

*Solved with Anthony Elle, who had also recently shared [Infinite Series' Markov Chains video](https://www.youtube.com/watch?v=63HHmjlh794) with me.*

It was quite an ordinary day when a mysterious alien vessel appeared as if from nowhere. After waiting several hours and receiving no response it is decided to send a team to investigate, of which you are included. Upon entering the vessel you are met by a friendly holographic figure, Katharina, who explains the purpose of the vessel, Eulertopia.

She claims that Eulertopia is almost older than time itself. Its mission was to take advantage of a combination of incredible computational power and vast periods of time to discover the answer to life, the universe, and everything. Hence the resident cleaning robot, Leonhard, along with his housekeeping responsibilities, was built with a powerful computational matrix to ponder the meaning of life as he wanders through a massive 1000 by 1000 square grid of rooms. She goes on to explain that the rooms are numbered sequentially from left to right, row by row. So, for example, if Leonhard was wandering around a 5 by 5 grid then the rooms would be numbered in the following way.
p575_wandering_robot_1_5x5.png

Many millenia ago Leonhard reported to Katharina to have found the answer and he is willing to share it with any life form who proves to be worthy of such knowledge.

Katharina further explains that the designers of Leonhard were given instructions to program him with equal probability of remaining in the same room or travelling to an adjacent room. However, it was not clear to them if this meant (i) an equal probability being split equally between remaining in the room and the number of available routes, or, (ii) an equal probability (50%) of remaining in the same room and then the other 50% was to be split equally between the number of available routes.
p575_wandering_robot_2_fixed.png
(i) Probability of remaining related to number of exits

p575_wandering_robot_3_dynamic.png
(ii) Fixed 50% probability of remaining

The records indicate that they decided to flip a coin. Heads would mean that the probability of remaining was dynamically related to the number of exits whereas tails would mean that they program Leonhard with a fixed 50% probability of remaining in a particular room. Unfortunately there is no record of the outcome of the coin, so without further information we would need to assume that there is equal probability of either of the choices being implemented.

Katharina suggests it should not be too challenging to determine that the probability of finding him in a square numbered room in a 5 by 5 grid after unfathomable periods of time would be approximately 0.177976190476 [12 d.p.].

In order to prove yourself worthy of visiting the great oracle you must calculate the probability of finding him in a square numbered room in the 1000 by 1000 lair in which he has been wandering.
(Give your answer rounded to 12 decimal places)

# Counting Sundays [Project Euler problem 19](https://projecteuler.net/problem=19)

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

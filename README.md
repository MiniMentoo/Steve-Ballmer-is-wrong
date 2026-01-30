
# The Game

I was laying in bed, and saw [this video](https://www.youtube.com/watch?v=svCYbkS0Sjk). Where Steve Ballmer is talking about his favourite interview question.

In this question he presents his candidates with a game. Steve will choose a number between 1 and 100. The candidate can make a guess on the number Steve is thinking, and will recieve one of three responses, HIGHER, LOWER or CORRECT.

If the candidate guesses the number immediately, they recieve a payout of $5, on the second game $4 and so on, on the 6th guess the candidate recieves no payout and on the 7th guess the candidate pays Steve $1.

Steve then declares that the candidate should NOT play this game. For 2 reasons, "there are a lot more numbers where you lose than where you win" and "I can pick a number that's harder for you to guess".

This video rubbed me the wrong way, but I didn't know how, and Steve seemed so confident, maybe my gut feeling was wrong? So I wrote up a quick implementation of Steve Ballmer's game, and made a binary searcher to solve it.

## The theory
Intuitively, using a binary search algorithm will give us the optimal number of guesses to find the number Steve is thinking off. We start at 50, and depending on if the response is higher or lower, we guess 25 or 75 respectively, halfing every time until we get the number.

The marker for a good strategy is one where the game is solved in less than 6 guesses on average. On the 6th guess the payout is 0, so if our average is below, then in theory you should play this game as much as possible, since you'll be winning in the long run.

So how many of the 100 numbers can binary search guess within 6 guesses?
1. On the first guess the midpoint is always 50, so 1. 
2. On the second guess you will guess 25 on a lower, and 75 on a higher. So you cover 2 here.
3. On the 3rd your guesses double again to 4.
4. 8
5. 16
6. 32

By the 5th guess you've coevered 16+8+4+2+1 = 31 possible numbers. And on the 6th you've covered 63. Meaning there are 37 numbers where you lose. 

Case closed then? You get nothing 32% of the time, win 31% of the time and lose 37%? 

...except your payout for winning is much higher than for losing. Because of how binary search works, on your 7th guess, you'd cover the remaining 100 numbers (127 actually). This means you could only ever lose $1 with binary search, but your payout can be up to $5 if you're lucky. 

This EV is easy to calculate aswell $5 * 0.01 (the 1% of getting it right first try) + 4 * 0.02 + 3 * 0.04 + 2 * 0.08 + 1 * 0.16 - 1 * 0.37 (the chance of losing) = 0.2.
Meaning you expect a payout of $0.20 every time you play this game.


## The results
So I made an implementation of this game. A random number generator decides the number for each round of the game. A Binary search algorithm runs through until it finds the secret number, then returns the number of guesses it took to find the number.

Running this experiment enough times and taking the average, our average number of guesses is **5.8**. Lower than 6 by a good amount of leeway.

## The catch
However, steve implies in this interview that the numbers he thinks of are not generated randomly. Instead he can choose between numbers that are "harder" for binary search to guess. 

Unfortunately Steve has assumed that an Optimal binary search is the only strategy that beats his game, and has assumed that the contestant will use this strategy when they play this game.

If I am to assume that Steve is playing adversarily, I can simply perform binary search on the 37 numbers that beat an optimal binary search. If I am correct my payout is even higher, since I'm far more likely to guess it within 5 attempts.

It is also possible to vary the initial guess, or to weight your second/3rd guesses more towards the "edges" with harder to reach numbers. These strategies are even harder to plan around since they also have the advantage of being strategies that aren't that much more suboptimal than optimal binary search.

![Plot showing average turns to guess vs variety of initial guesses](https://github.com/MiniMentoo/Steve-Ballmer-is-wrong/blob/main/Initial%20Guess%20vs%20Average%20Number%20of%20Guesses.png "Plot showing average turns to guess vs variety of initial guesses")

This above plot shows the average number of guesses to find a random number if we vary the initial first guess. This was the simplest varience in guess strategy to test. By altering your initial guess slightly, you can travel down a different
"path" of guesses. This makes your chosen guesses less predictable and has the upside of still performing almost equally as well for initial guesses within the 40-60 range, and keeping it's edge against Steve for the 25-75 range.

I'm sure there are plenty of other smart strategies to beat this game, even against an adversarial number picker, but I am now satisfied, and my curiousity has been sated.

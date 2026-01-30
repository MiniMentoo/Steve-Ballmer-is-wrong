import matplotlib.pyplot as plt

from binarytest import BinarySearcher, NUM_OF_TRIALS


def average_guesses_for_initial_guess(initial_guess: int) -> float:
    total_guesses = 0
    bs = BinarySearcher(initial_guess)

    for _ in range(NUM_OF_TRIALS):
        total_guesses += bs.playGame()
        bs.reset()

    return total_guesses / NUM_OF_TRIALS


def main():
    initial_guesses = list(range(1, 101))
    averages = []

    for guess in initial_guesses:
        avg = average_guesses_for_initial_guess(guess)
        averages.append(avg)
        print(f"Initial guess {guess}: average guesses = {avg:.4f}")

    # Plot
    plt.figure()
    plt.plot(initial_guesses, averages, label="Average guesses")
    plt.axhline(y=6, linestyle="--", label="y = 6")

    plt.xlabel("Initial Guess")
    plt.ylabel("Average Number of Guesses")
    plt.title("Initial Guess vs Average Number of Guesses")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()

from binarytest import (
    NumberGame,
    BinarySearcher,
    result,
    LOWERBOUND,
    UPPERBOUND,
)

# ------------------------
# result enum tests
# ------------------------

def test_result_enum_values():
    assert result.HIGHER.value == 1
    assert result.LOWER.value == -1
    assert result.CORRECT.value == 0


# ------------------------
# NumberGame tests
# ------------------------

def test_numbergame_correct_guess(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 42)
    game = NumberGame()

    assert game.guess(42) == result.CORRECT


def test_numbergame_guess_higher(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 50)
    game = NumberGame()

    assert game.guess(25) == result.HIGHER


def test_numbergame_guess_lower(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 50)
    game = NumberGame()

    assert game.guess(75) == result.LOWER


def test_numbergame_reset_changes_number(monkeypatch):
    values = iter([10, 90])
    monkeypatch.setattr("random.randint", lambda a, b: next(values))

    game = NumberGame()
    first = game.number

    game.reset()
    second = game.number

    assert first != second
    assert LOWERBOUND <= second <= UPPERBOUND


# ------------------------
# BinarySearcher tests
# ------------------------

def test_set_guess_midpoint():
    bs = BinarySearcher()
    bs.lower = 1
    bs.upper = 100

    assert bs.setGuess() == 50


def test_binarysearcher_finds_number(monkeypatch):
    """
    Force the environment number so the game is deterministic.
    """
    monkeypatch.setattr("random.randint", lambda a, b: 73)

    bs = BinarySearcher()
    guesses = bs.playGame()

    assert bs.previousGuessResult == result.CORRECT
    assert bs.env.number == 73
    assert guesses > 0


def test_binarysearcher_guess_count_reasonable(monkeypatch):
    """
    Binary search over 1–100 should take at most 7 guesses.
    """
    monkeypatch.setattr("random.randint", lambda a, b: 1)

    bs = BinarySearcher()
    guesses = bs.playGame()

    assert guesses <= 7


def test_binarysearcher_reset_restores_state(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 42)

    bs = BinarySearcher()
    bs.playGame()
    bs.reset()

    assert bs.guessCount == 0
    assert bs.lower == LOWERBOUND
    assert bs.upper == UPPERBOUND
    assert bs.previousGuessResult is None

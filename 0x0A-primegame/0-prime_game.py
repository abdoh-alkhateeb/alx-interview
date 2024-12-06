#!/usr/bin/python3
"""
Defines `isWinner`.
"""


def isWinner(x, nums):
    """
    Returns name of the player that won the most rounds.
    """

    ben_wins = 0
    maria_wins = 0

    nums = nums[:x]

    if nums:
        max_n = max(nums)

    primes = []

    for i in range(2, max_n + 1):
        for prime in primes:
            if i % prime != 0:
                break
        else:
            primes.append(i)

    for n in nums:
        marias_turn = True

        round_primes = filter(lambda x: x <= n, primes)

        while True:
            try:
                next(round_primes)

                marias_turn ^= True
            except StopIteration:
                if marias_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1

                break

    if ben_wins > maria_wins:
        return "Ben"

    if maria_wins > ben_wins:
        return "Maria"

    return None

def sieve(n):
    # Sieve of Eratosthenes.
    prime_list = [True]*n # Initialize primality list. Better than initializing on the fly.
    prime_list[0] = False
    prime_list[1] = False

    for (i, is_prime) in enumerate(prime_list):
        if is_prime:
            yield i
            for j in range(i**2, n, i): # Mark factors which are non-prime.
                prime_list[j] = False

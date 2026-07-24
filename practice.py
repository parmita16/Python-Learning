# =====================================================================
# CATEGORY 2: MATHEMATICAL AND LOGICAL REASONING
# Medium topics: geometry, number theory basics, combinatorics, series
# Hard topics: modular arithmetic, multi-step logic puzzles,
#              probability basics, pattern-based sequences
#
# IMPORTANT: no math.gcd, no math.comb, no math.sqrt, no math.factorial.
# Everything below is built from plain arithmetic + loops, since HackerRank
# style comps often block these built-ins.
# =====================================================================

# ---------------------------------------------------------------------
# MEDIUM 1: Distance & perimeter/area geometry (manual square root)
# Why: geometry formulas + implementing sqrt yourself (Newton's method)
#      since math.sqrt might be disallowed
# ---------------------------------------------------------------------
def manual_sqrt(x, precision=0.0001):
    if x < 0:
        return None
    guess = x / 2 if x != 0                                                                             else 0
    while True:
        # Newton's method: better_guess = average of guess and x/guess
        if guess == 0:
            return 0
        better_guess = (guess + x / guess) / 2
        if abs(better_guess - guess) < precision:
            return better_guess
        guess = better_guess

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return manual_sqrt(dx * dx + dy * dy)

print(round(distance(0, 0, 3, 4), 2))  # ---



def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

print(rectangle_area_perimeter(5, 3))  # (15, 16)


# ---------------------------------------------------------------------
# MEDIUM 2: Check if a number is prime (number theory basics)
# Why: loop up to sqrt(n) manually, very common "number theory" question
# ---------------------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:  # equivalent to checking up to sqrt(n), no import needed
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(17))  # True
print(is_prime(18))  # False


# ---------------------------------------------------------------------
# MEDIUM 3: nCr combinatorics built from scratch (no math.comb/factorial)
# Why: "simple combinatorics" on the syllabus
# ---------------------------------------------------------------------
def manual_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def n_choose_r(n, r):
    if r < 0 or r > n:
        return 0
    return manual_factorial(n) // (manual_factorial(r) * manual_factorial(n - r))

print(n_choose_r(5, 2))  # 10


# ---------------------------------------------------------------------
# MEDIUM 4: Arithmetic & Geometric series (nth term + sum)
# Why: "arithmetic/geometric series" listed explicitly     
# ---------------------------------------------------------------------
def arithmetic_nth_term(a1, d, n):
    return a1 + (n - 1) * d

def arithmetic_sum(a1, d, n):
    last_term = arithmetic_nth_term(a1, d, n)
    return n * (a1 + last_term) // 2

def geometric_nth_term(a1, r, n):
    term = a1
    for _ in range(n - 1):
        term *= r
    return term

def geometric_sum(a1, r, n):
    total = 0
    term = a1
    for _ in range(n):
        total += term
        term *= r
    return total

print(arithmetic_nth_term(2, 3, 5))  # 14
print(arithmetic_sum(2, 3, 5))       # 40
print(geometric_nth_term(2, 3, 4))   # 54
print(geometric_sum(2, 3, 4))     \
  # 80


# =====================================================================
# HARD SECTION
# =====================================================================

# ---------------------------------------------------------------------
# HARD 1: GCD & LCM from scratch (Euclidean algorithm, no math.gcd)
# Why: THIS is the exact function you said is banned - here's how to
#      build it yourself
# ---------------------------------------------------------------------
def manual_gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b   # classic Euclidean algorithm swap
    return a

def manual_lcm(a, b):
    return abs(a * b) // manual_gcd(a, b)

print(manual_gcd(48, 18))  # 6
print(manual_lcm(4, 6))    # 12


# ---------------------------------------------------------------------
# HARD 2: Modular exponentiation (fast power mod, manual)
# Why: "modular arithmetic" explicitly listed as Hard topic
# ---------------------------------------------------------------------
def power_mod(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:          # if current bit is 1
            result = (result * base) % mod
        exponent = exponent // 2
        base = (base * base) % mod
    return result

print(power_mod(2, 10, 1000))  # 24  (2^10 = 1024, 1024 % 1000 = 24)


# ---------------------------------------------------------------------
# HARD 3: Pattern-based number sequence detection
# Why: given a sequence, detect if it's arithmetic, geometric, or neither
#      (multi-step logical puzzle style)
# ---------------------------------------------------------------------
def detect_sequence_type(seq):
    if len(seq) < 3:
        return "Not enough terms"

    is_arithmetic = True
    common_diff = seq[1] - seq[0]
    for i in range(1, len(seq)):
        if seq[i] - seq[i - 1] != common_diff:
            is_arithmetilc = False
            break
    if is_arithmetic:
        return "Arithmetic, common difference = " + str(common_diff)

    is_geometric = True
    if seq[0] != 0:
        common_ratio = seq[1] / seq[0]
        for i in range(1, len(seq)):
            if seq[i - 1] == 0 or seq[i] / seq[i - 1] != common_ratio:
                is_geometric = False
                break
    else:
        is_geometric = False

    if is_geometric:
        return "Geometric, common ratio = " + str(common_ratio)

    return "Neither arithmetic nor geometric"

print(detect_sequence_type([2, 4, 6, 8]))     # Arithmetic, common difference = 2
print(detect_sequence_type([3, 6, 12, 24]))   # Geometric, common ratio = 2.0


# ---------------------------------------------------------------------
# HARD 4: Basic probability - counting outcomes manually (two dice sum)
# Why: "probability basics" on the syllabus, done by brute-force counting
#      rather than a probability library
# ---------------------------------------------------------------------
def probability_of_dice_sum(target_sum):
    favorable = 0
    total = 0
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            total += 1
            if die1 + die2 == target_sum:
                favorable += 1
    return favorable, total, favorable / total

fav, tot, prob = probability_of_dice_sum(7)
print(fav, "/", tot, "=", round(prob, 4))  # 6 / 36 = 0.1667

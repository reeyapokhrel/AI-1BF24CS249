
from itertools import product

def implies(a, b):
    return (not a) or b

def show(x):
    return "T" if x else "F"

# Knowledge Base
# 1. Q -> P
# 2. P -> NOT Q
# 3. Q OR R

def evaluate(p, q, r):
    s1 = implies(q, p)
    s2 = implies(p, not q)
    s3 = q or r

    kb = s1 and s2 and s3
    return s1, s2, s3, kb

print("TRUTH TABLE")
print("-----------------------------------------")
print("P  Q  R | Q->P | P->!Q | QvR | KB")
print("-----------------------------------------")

models = []

for p, q, r in product([True, False], repeat=3):
    s1, s2, s3, kb = evaluate(p, q, r)

    print(show(p), show(q), show(r), " | ",
          show(s1), "  |  ", show(s2), "  | ",
          show(s3), " | ", show(kb))

    if kb:
        models.append((p, q, r))

print("\nMODELS OF KB:")
for model in models:
    print(tuple(show(x) for x in model))

def entails(test):
    return all(test(p, q, r) for p, q, r in models)

print("\nENTAILMENT RESULTS:")
print("ii) KB entails R:",
      entails(lambda p, q, r: r))

print("iii) KB entails R -> P:",
      entails(lambda p, q, r: implies(r, p)))

print("iv) KB entails Q -> R:",
      entails(lambda p, q, r: implies(q, r)))

#Output
# TRUTH TABLE
# -----------------------------------------
# P  Q  R | Q->P | P->!Q | QvR | KB
# -----------------------------------------
# T T T  |  T   |   F   |  T  |  F
# T T F  |  T   |   F   |  T  |  F
# T F T  |  T   |   T   |  T  |  T
# T F F  |  T   |   T   |  F  |  F
# F T T  |  F   |   T   |  T  |  F
# F T F  |  F   |   T   |  T  |  F
# F F T  |  T   |   T   |  T  |  T
# F F F  |  T   |   T   |  F  |  F

# MODELS OF KB:
# ('T', 'F', 'T')
# ('F', 'F', 'T')

# ENTAILMENT RESULTS:
# ii) KB entails R: True
# iii) KB entails R -> P: False
# iv) KB entails Q -> R: True

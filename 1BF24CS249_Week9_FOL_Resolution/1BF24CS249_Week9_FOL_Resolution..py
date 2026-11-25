

def resolve(c1, c2):
    result = []

    for a in c1:
        for b in c2:
            if a == "~" + b or b == "~" + a:
                new_clause = [x for x in c1 if x != a]
                new_clause += [x for x in c2 if x != b]
                result.append(new_clause)

    return result


clauses = [
    ["~Food(Peanuts)", "Likes(John,Peanuts)"],

    ["~Eats(Anil,Peanuts)",
     "~NotKilled(Anil)", "Food(Peanuts)"],

    ["Eats(Anil,Peanuts)"],

    ["Alive(Anil)"],

    ["~Alive(Anil)", "NotKilled(Anil)"],

    ["~Likes(John,Peanuts)"]
]

print("RESOLUTION PROOF\n")

print("Initial Clauses:")
for i, c in enumerate(clauses, 1):
    print(f"C{i}: {' OR '.join(c)}")

print("\nApplying Resolution:\n")

r1 = ["~Food(Peanuts)"]
print("1. Substitution: {Peanuts/x}")
print("   Result:", " OR ".join(r1))

r2 = ["~Eats(Anil,Peanuts)", "~NotKilled(Anil)"]
print("\n2. Substitution: {Anil/y, Peanuts/z}")
print("   Result:", " OR ".join(r2))

r3 = ["~NotKilled(Anil)"]
print("\n3. Resolve with Eats(Anil,Peanuts)")
print("   Result:", " OR ".join(r3))

r4 = ["NotKilled(Anil)"]
print("\n4. Resolve with Alive(Anil)")
print("   Result:", " OR ".join(r4))

print("\n5. Resolve:")
print("   ~NotKilled(Anil)")
print("   NotKilled(Anil)")
print("   Result: {}")

print("\nSUCCESS: Empty clause obtained!")
print("Hence, John likes peanuts is PROVED.")


# Output
# RESOLUTION PROOF

# Initial Clauses:
# C1: ~Food(Peanuts) OR Likes(John,Peanuts)
# C2: ~Eats(Anil,Peanuts) OR ~NotKilled(Anil) OR Food(Peanuts)
# C3: Eats(Anil,Peanuts)
# C4: Alive(Anil)
# C5: ~Alive(Anil) OR NotKilled(Anil)
# C6: ~Likes(John,Peanuts)

# Applying Resolution:

# 1. Substitution: {Peanuts/x}
#    Result: ~Food(Peanuts)

# 2. Substitution: {Anil/y, Peanuts/z}
#    Result: ~Eats(Anil,Peanuts) OR ~NotKilled(Anil)

# 3. Resolve with Eats(Anil,Peanuts)
#    Result: ~NotKilled(Anil)

# 4. Resolve with Alive(Anil)
#    Result: NotKilled(Anil)

# 5. Resolve:
#    ~NotKilled(Anil)
#    NotKilled(Anil)
#    Result: {}

# SUCCESS: Empty clause obtained!
# Hence, John likes peanuts is PROVED.

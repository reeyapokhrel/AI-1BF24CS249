

facts = {
    ("Owns", "A", "T1"),
    ("Missile", "T1"),
    ("American", "Robert"),
    ("Enemy", "A", "America")
}



def forward_chaining(facts):

    print("INITIAL FACTS:")
    for fact in sorted(facts):
        print(fact)

    print("\nFORWARD CHAINING PROCESS:")
    
    new_fact_added = True

    while new_fact_added:
        new_fact_added = False
        new_facts = set()

        for fact in facts:
            if fact[0] == "Missile":
                x = fact[1]
                if ("Owns", "A", x) in facts:
                    result = ("Sells", "Robert", x, "A")
                    if result not in facts:
                        new_facts.add(result)

        for fact in facts:
            if fact[0] == "Missile":
                x = fact[1]
                result = ("Weapon", x)
                if result not in facts:
                    new_facts.add(result)
)
        for fact in facts:
            if fact[0] == "Enemy" and fact[2] == "America":
                x = fact[1]
                result = ("Hostile", x)
                if result not in facts:
                    new_facts.add(result)


        for american in facts:
            if american[0] == "American":
                p = american[1]

                for weapon in facts:
                    if weapon[0] == "Weapon":
                        q = weapon[1]

                        for sale in facts:
                            if sale[0] == "Sells":
                                seller, item, country = sale[1:]

                                if seller == p and item == q:
                                    if ("Hostile", country) in facts:
                                        result = ("Criminal", p)

                                        if result not in facts:
                                            new_facts.add(result)

        if new_facts:
            print("\nNew facts derived:")
            for fact in sorted(new_facts):
                print(fact)

            facts.update(new_facts)
            new_fact_added = True

    return facts


final_facts = forward_chaining(facts)

print("\n================================")
print("GOAL: Criminal(Robert)")
print("================================")

if ("Criminal", "Robert") in final_facts:
    print("SUCCESS: Robert is Criminal.")
else:
    print("FAILURE: Cannot prove Robert is Criminal.")


# Output
# INITIAL FACTS:
# ('American', 'Robert')
# ('Enemy', 'A', 'America')
# ('Missile', 'T1')
# ('Owns', 'A', 'T1')

# FORWARD CHAINING PROCESS:

# New facts derived:
# ('Hostile', 'A')
# ('Sells', 'Robert', 'T1', 'A')
# ('Weapon', 'T1')

# New facts derived:
# ('Criminal', 'Robert')

# ================================
# GOAL: Criminal(Robert)
# ================================
# SUCCESS: Robert is Criminal.

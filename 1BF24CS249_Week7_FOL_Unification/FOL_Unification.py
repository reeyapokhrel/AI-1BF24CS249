

def is_variable(term):
    return term.islower()

def unify(term1, term2, substitutions):
    while term1 in substitutions:
        term1 = substitutions[term1]

    while term2 in substitutions:
        term2 = substitutions[term2]

    if term1 == term2:
        return True

    if is_variable(term1):
        substitutions[term1] = term2
        print(f"Substitution: {term1} = {term2}")
        return True

    if is_variable(term2):
        substitutions[term2] = term1
        print(f"Substitution: {term2} = {term1}")
        return True

    return False


def apply_substitution(expression, substitutions):
    result = []

    for term in expression:
        while term in substitutions:
            term = substitutions[term]
        result.append(term)

    return result


def main():
    print("========================================")
    print(" UNIFICATION IN FIRST ORDER LOGIC")
    print("========================================")

    # Given expressions
    expr1 = ["Eats", "x", "Apple"]
    expr2 = ["Eats", "Riya", "y"]

    print("\nExpression A:", f"{expr1[0]}({expr1[1]}, {expr1[2]})")
    print("Expression B:", f"{expr2[0]}({expr2[1]}, {expr2[2]})")

    substitutions = {}

    print("\n--- Unification Process ---")

    if expr1[0] != expr2[0]:
        print("Unification Failed: Predicate names differ.")
        return

    print("\nStep 1: Comparing predicate names")
    print("Both predicates are Eats")

    print("\nStep 2: Unifying first arguments")
    if not unify(expr1[1], expr2[1], substitutions):
        print("Unification Failed!")
        return

    print("\nStep 3: Unifying second arguments")
    if not unify(expr1[2], expr2[2], substitutions):
        print("Unification Failed!")
        return

    print("\n--- Substitution Set ---")
    for key, value in substitutions.items():
        print(f"{key} = {value}")

    result1 = apply_substitution(expr1, substitutions)
    result2 = apply_substitution(expr2, substitutions)

    print("\n--- Applying Substitutions ---")
    print(f"Expression A: {result1[0]}({result1[1]}, {result1[2]})")
    print(f"Expression B: {result2[0]}({result2[1]}, {result2[2]})")

    print("\n--- Final Result ---")

    if result1 == result2:
        print("Unified Expression:",
              f"{result1[0]}({result1[1]}, {result1[2]})")
        print("Unification Successful!")
    else:
        print("Unification Failed!")


if __name__ == "__main__":
    main()

# Output
# ========================================
#  UNIFICATION IN FIRST ORDER LOGIC
# ========================================

# Expression A: Eats(x, Apple)
# Expression B: Eats(Riya, y)

# --- Unification Process ---

# Step 1: Comparing predicate names
# Both predicates are Eats

# Step 2: Unifying first arguments
# Substitution: x = Riya

# Step 3: Unifying second arguments
# Substitution: y = Apple

# --- Substitution Set ---
# x = Riya
# y = Apple

# --- Applying Substitutions ---
# Expression A: Eats(Riya, Apple)
# Expression B: Eats(Riya, Apple)

# --- Final Result ---
# Unified Expression: Eats(Riya, Apple)
# Unification Successful!

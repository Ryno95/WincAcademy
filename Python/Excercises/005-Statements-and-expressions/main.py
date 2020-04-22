# A "statement" is something your computer can execute
# An "expression" is something that your computer can evaluate and is a small part of a statement
# ex. 5*3 (expr) a=5*3 (statem)

3  # Expr
3 + 3  # Expr
prijs = 5  # Statem
aantal = 3  # Statem
prijs * aantal  # Expr
totaalPrijs = prijs * aantal  # Statem
totaalPrijs  # Expr
print(totaalPrijs)  # Statem
frank = "Frank Rijkaard"  # Statem
print(f"Hallo {frank}")  # Statem
f"Hoi {frank}"  # Expr
f"Zeg {frank}, jouw voornaam heeft {len(frank[:5])} karakters."  # Expr

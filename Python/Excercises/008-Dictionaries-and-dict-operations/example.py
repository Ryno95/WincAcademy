# You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}).
# A colon (:) separates each key from its associated value:
# dict = {key: value}

# Classic syntax
MLB_team = {
    "Colorado": "Rockies",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}

# Alt syntax #1
MLB_team1 = dict(
    [
        ("Colorado", "Rockies"),
        ("Boston", "Red Sox"),
        ("Minnesota", "Twins"),
        ("Milwaukee", "Brewers"),
        ("Seattle", "Mariners"),
    ]
)

# Alt syntax #2 (Only if values are strings)
MLB_team3 = dict(
    Colorado="Rockies",
    Boston="Red Sox",
    Minnesota="Twins",
    Milwaukee="Brewers",
    Seattle="Mariners",
)

# Accessing Dictionary values:
MLB_team["Minnesota"]  # Prints 'Twins'

MLB_team["Colorado"]  # Prints 'Rockies'

# To add an entry simply assign a new value and key pair
MLB_team["Pretoria"] = "Blou Bulle"

# To update and existing entry, assign a new value to existing key
MLB_team["Seattle"] = "Seahawks"

# To delete an entry, use del statement and specify key
del MLB_team["Pretoria"]

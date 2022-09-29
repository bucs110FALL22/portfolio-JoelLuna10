article = """
Slow but durable, only attacks buildings. When destroyed, explosively splits into two Golemites and deals area damage! 
"""

substitutions = {
    "Slow":"fast",
    "durable":"weak",
    "attacks":"defends",
    "buildings":"troops",
    "destroyed":"healed",
    "explosively":"",
    "splits":"grows",
    "two": "one",
    "Golemites": "Huge Golem",
    "area damage!":"explosive damage!",
}

for key, value in substitutions.items():
    article = article.replace(key, value)

print(article)
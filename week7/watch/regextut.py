import re

# Check if the string starts with "Python"
"""
result = re.match("Python", "Python Regex Match")
print(result)
"""

# Search for the pattern "Regex" in the string
"""
result = re.search("Regex", "Python Regex Match")
print(result)
"""

######

pattern = r"https?://[^\s]+"
text = "Visit our website at https://www.example.com or follow us on https://twitter.com/example."

urls = re.findall(pattern, text)
print(urls)



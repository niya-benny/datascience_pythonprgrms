import re

pattern = re.compile(r'\bhello\b', re.IGNORECASE)

text = "Hello world! Do you want to say hello?"

matches = pattern.findall(text)
print(matches)  # ['Hello', 'hello']

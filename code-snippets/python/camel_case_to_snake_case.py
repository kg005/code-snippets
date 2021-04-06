# one time

import re
name = 'CamelCaseName'
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name)  # camel_case_name

# multiple times

pattern = re.compile(r'(?<!^)(?=[A-Z])')
name = pattern.sub('_', name).lower()


# snake to camel

name = 'snake_case_name'
name = ''.join(word.title() for word in name.split('_'))
print(name)  # SnakeCaseName


# advanced to handle abbreviations (not reversible though)

def camel_to_snake(name):
  name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


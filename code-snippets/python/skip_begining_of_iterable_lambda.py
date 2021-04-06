
string_from_file = """
// Author: ...
// License: ...
//
// Date: ...

Actual content...
"""

import itertools

for line in itertools.dropwhile(lambda line: line.startswith("//"), string_from_file.split("\n")):
    print(line)

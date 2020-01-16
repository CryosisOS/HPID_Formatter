import sys
import json

def recurse(d, allStrings, currentString=list()):
    for k, v in d.items():
        if isinstance(v, dict):
            currentString.append(k)
            recurse(v, allStrings, currentString=currentString)
            currentString.pop()
        elif isinstance(v, list):
            currentString.append(k+" - "+str(v))
            allStrings.append(currentString.copy())
            currentString.pop()
        else:   
            currentString.append(k+" - "+v)
            allStrings.append(currentString.copy())
            currentString.pop()
    return allStrings.copy()


with open(sys.argv[1]) as json_file:
    data = json.load(json_file)
    strings = list()
    strings = recurse(data, strings)
formatted_strings = list()
for string in strings:
    formatted_strings.append(" - ".join(string))
output = open(sys.argv[2], "w")
for string in formatted_strings:
    output.write("=>"+string+"\n")
output.close()
print("Format finished.")
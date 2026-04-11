original = ['a', 'b', 'c']

copy = original[:]      # if copy = original, copy just points out to original which means both the lists will be connected

copy.append('d')

print(f"Original : {original}\nCopy : {copy}")
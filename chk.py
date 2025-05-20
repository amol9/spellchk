import re

fn = "one.txt"
text = ""
with open(fn, 'r') as f:
    text = f.read()

words = ""
text2 = ""

fn2 = "/usr/share/dict/words"
with open(fn2, 'r') as f:
    text2 = f.read()

words = text2.split()

#print(words[0:20])
#print(len(words))

words_in_file = text.split()

print(words_in_file[0:10])
print(len(words_in_file))

for w in words_in_file:
    print(w)
    w2 = ""
    m = re.match("[a-z]+", w)
    if m is not None:
        w2 = m[0]
        
    print(w2)

    
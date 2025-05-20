
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

print(words[0:20])
print(len(words))
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

#print(words_in_file[0:10])
#print(len(words_in_file))

for w in words_in_file:
    #print(w)
    w2 = ""
    m = re.match("[a-z]+", w)
    if m is not None:
        w2 = m[0].strip()
        
    #print(w2)

    if w2 == "":
        continue

    if w2 not in words:
        w3 = ""
        if w2[-1] == 's':
            w3 = w2[:-1]
            #print(w3)
            if w3 not in words:
                print(w3)
        elif w2[-2:] == "ed":
            w3 = w2[:-2]
            if w3 not in words:
                #print(w3)
                w3 += 'e'
                #w3 = w2[:-2]
                if w3 not in words:
                    print(w3)
        elif w2[-3:] == "ing":
            w3 = w2[:-3]
            if w3 not in words:
                #print(w3)
                w3 += 'e'
                #w3 = w2[:-2]
                if w3 not in words:
                    print(w3)
        elif w2[-3:] == "ive":
            w3 = w2[:-3]
            if w3 not in words:
                print(w3)
        else:
            print(w2)
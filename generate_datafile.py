import random
import string

"""it's working for the most cases , but there is problem with del op . note : its work fine without del op

This basically lazy code that generate n_word randomly then chooses random number
of operation add,replace,del . every operation have unique special char that refilled in the string
and after all ops finish , process special char that had been added and calc the total number of ops .
then save the original word , the edited one and the num of ops.


["+","$","-","!"]
+ plus 
$ alter
- del
! never exist
"""
word_count = 100
max_ops = 5
max_char = 100
with open("data.txt", "w") as f:
    for _ in range(word_count):
        n_char = random.randint(1, max_char)
        a = b = ''.join([random.choice(string.ascii_letters).lower() for _ in range(n_char)])
        add_op = random.randint(0, max_ops)
        replace_op = random.randint(0, max_ops)
        del_op = random.randint(0, max_ops)
        total_ops = 0
        for _ in range(add_op):
            idx = random.randint(0, len(b) - 1)
            b = b[:idx] + "+" + b[idx:]

        for _ in range(replace_op):
            idx = random.randint(0, len(b) - 1)
            if b[idx] != "+":
                b = b[:idx] + "$" + b[idx + 1:]

        for _ in range(del_op):
            idx = random.randint(0, len(b) - 1)
            if b[idx] == "$" or b[idx] == "+":
                b = b[:idx] + "!" + b[idx + 1:]
            else:
                b = b[:idx] + "-" + b[idx + 1:]

        for i in range(len(b)):
            if b[i] == "-":
                total_ops += 1
            elif b[i] == "+":
                b = b[:i] + random.choice(string.ascii_letters).upper() + b[i + 1:]
                total_ops += 1
            elif b[i] == "$":
                total_ops += 1
                b = b[:i] + random.choice(string.ascii_letters).upper() + b[i + 1:]
            else:
                pass
        b = b.replace("-", " ")
        b = b.replace("!", "")

        f.write(f"{a}_{b}_{total_ops}\n")

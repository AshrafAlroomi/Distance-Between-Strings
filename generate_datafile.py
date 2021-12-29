import random
import string
import re

n_word = 100
"""This basically lazy code that generate n_word randomly then chooses random number
of operation add,replace,del . every operation have unique special char that refilled in the string
and after all ops finish , process special char that had been added and calc the total number of ops .
then save the original word , the edited one and the num of ops.


+ plus
# plus/replace
! plus/replace/del
@ plus/del
$ replace
- del
"""
with open("data.txt", "w") as f:
    for _ in range(n_word):
        n_char = random.randint(1, 100)
        a = b = ''.join([random.choice(string.ascii_letters).upper() for _ in range(n_char)])
        add_op = random.randint(0, 10)
        replace_op = random.randint(0, 10)
        # del_op = random.randint(0, 10)

        for _ in range(add_op):
            idx = random.randint(0, len(b) - 1)
            b = b[:idx] + "+" + b[idx:]

        for _ in range(replace_op):
            idx = random.randint(0, len(b) - 1)
            if b[idx] == "+":
                b = b[:idx] + "#" + b[idx:]
            else:
                b = b[:idx] + "$" + b[idx:]

        """Unfortunately del not working :( """
        # for _ in range(del_op):
        #     idx = random.randint(0, len(b) - 1)
        #     if b[idx] == "#":
        #         b = b[:idx] + "!" + b[idx + 1:]
        #     elif b[idx] == "+":
        #         b = b[:idx] + "@" + b[idx + 1:]
        #     else:
        #         b = b[:idx] + "-" + b[idx + 1:]

        total_ops = 0
        for i in range(len(b)):
            if b[i] == "-":
                total_ops += 1
            elif b[i] == "+":
                b = b[:i] + random.choice(string.ascii_letters).lower() + b[i + 1:]
                total_ops += 1
            elif b[i] == "$":
                total_ops += 1
                b = b[:i] + random.choice(string.ascii_letters).lower() + b[i + 1:]
            elif b[i] == "#":
                total_ops += 1
                b = b[:i] + random.choice(string.ascii_letters).lower() + b[i + 1:]

        b = b.replace("-", "")
        b = b.replace("@", "")
        b = b.replace("!", "")

        f.write(f"{a} {b} {total_ops}\n")

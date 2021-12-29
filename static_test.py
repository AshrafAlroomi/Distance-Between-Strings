from distance import Levenshtein, Hamming

# example from wiki
a = "flaw"
b = "lawn"

print(f"Hamming= {Hamming(a, b).distance()}")
print(f"Levenshtein= {Levenshtein(a, b).distance()}")


from distance import Levenshtein, Hamming

# this code need user instruction to run

algo_list = ["Levenshtein", "Hamming"]  # add all algo that you have, make sure you import them first
algo_dict = {i: v for i, v in enumerate(algo_list)}  # give the algo id , make user choose id
text1 = input("input the first string: ")  # a
text2 = input("input the second string: ")  # b
algo = input(f"choose the distance algo id {algo_dict} :")  # id of  the algo
distance = eval(
    algo_dict[int(algo)] + f"('{text1}','{text2}').distance()")  # this use eval to ref the algo by chosen id
print("-" * 20)
print(f"this distance = {distance}")

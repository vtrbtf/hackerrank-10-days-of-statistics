dice = [1,2,3,4,5,6]
all_probs_set = [(str(d1) + "," + str(d2)) for d1 in dice for d2 in dice]
at_most_9_set = ([(str(d1) + "," + str(d2)) for d1 in dice for d2 in dice if (d1 + d2) <= 9])

print(f"All kind of toss set: {all_probs_set}")
print(f"At most 9 toss set: {at_most_9_set}")
print("--------------------------")
print("A = sum will be at most 9 ")
print(f"P(A) = {len(at_most_9_set)} / {len(all_probs_set)}")
print(f"P(A) = {len(at_most_9_set) / len(all_probs_set)}")

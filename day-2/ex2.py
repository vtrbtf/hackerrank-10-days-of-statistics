dice = [1,2,3,4,5,6]
all_probs_set = [(str(d1) + "," + str(d2)) for d1 in dice for d2 in dice]
distinct_and_equal_to_six_set = ([(str(d1) + "," + str(d2)) for d1 in dice for d2 in dice if (d1 != d2) and ((d1 + d2) == 6)])

print(f"All kind of toss set: {all_probs_set}")
print(f"Distinct and equal to 6 toss set: {distinct_and_equal_to_six_set}")
print("--------------------------")
print("A = Distinct and equal to 6 ")
print(f"P(A) = {len(distinct_and_equal_to_six_set)} / {len(all_probs_set)}")
print(f"P(A) = {len(distinct_and_equal_to_six_set) / len(all_probs_set)}")

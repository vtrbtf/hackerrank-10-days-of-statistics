P_RED_X = 4/7
P_RED_Y = 5/9
P_RED_Z = 4/8

P_BLK_X = 3/7
P_BLK_Y = 4/9
P_BLK_Z = 4/8

print("P(2 Reds and 1 Black) = P(Red, Red. Black) + P(Red, Black, Red) + P(Black, Red, Red)")
print("For P(X,Y,Z)")
print(f"(P_RED_X * P_RED_Y * P_BLK_Z) + (P_RED_X * P_BLK_Y * P_RED_Z) + (P_BLK_X + P_RED_Y + P_RED_Z)")
print(f"({P_RED_X} * {P_RED_Y} * {P_BLK_Z}) + ({P_RED_X} * {P_BLK_Y} * {P_RED_Z}) + ({P_BLK_X} * {P_RED_Y} * {P_RED_Z})")
print((P_RED_X * P_RED_Y * P_BLK_Z) + (P_RED_X * P_BLK_Y * P_RED_Z) + (P_BLK_X * P_RED_Y * P_RED_Z))

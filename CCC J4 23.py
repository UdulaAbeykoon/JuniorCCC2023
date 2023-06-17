C = int(input())
Tape = 0
rowInput_1 = str(input())
rowInput_2 = str(input())
rowInput_1 = rowInput_1.split()
rowInput_2 = rowInput_2.split()
Tape += rowInput_1.count("1") * 3
Tape += rowInput_2.count("1") * 3
for x in range(C):
  if x != 0:
    if rowInput_1[x] == "1" and rowInput_1[x - 1] == "1":
      Tape -= 2
  if x != 0:
    if rowInput_2[x] == "1" and rowInput_2[x - 1] == "1":
      Tape -= 2
  if rowInput_1[x] == "1" and rowInput_2[x] == "1" and x % 2 != 1:
    Tape -= 2
print(Tape)
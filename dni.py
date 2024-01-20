 1 with open("wordlist.txt", "w") as f:
 2         for a in range(0, 999):
 3                 for b in range(30000000, 39999999):
 4                         f.write(str(a).zfill(3) + str(b).zfill(8) + "\n")

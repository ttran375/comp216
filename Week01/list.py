## List

lst1 = []
lst2 = ["programming", "mathematics", 2018, 3.14]
lst3 = [1, 2, 3, 4, 5, 3, 2, 1]
lst4 = ["narendra", "pershad"]
lst2[1]  # 'mathematics'
lst3[8]  # indexError
lst2[-1]  # 3.14
lst3[-3]  # 3
for item in lst3:
    for i in range(len(lst3)):
        print(lst3[i])

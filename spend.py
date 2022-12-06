import csv
import matplotlib.pyplot as plt


Years = []
Spent = []


with open('/Users/grant/Desktop/spenddata.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    linecount = 0
    for row in lines:
        linecount += 1

        if linecount != 1:
            year = row[0]
            money = float(row[20][1:])

            if year in Years:
                Spent[Years.index(year)] += money
            else:
                Years.append(year)
                Spent.append(money)

plt.bar(Years, Spent, color = 'g', width = 0.72,)
plt.xlabel('Years')
plt.ylabel('Spent')
plt.title('Money Spent on Amazon')
plt.legend()
plt.show()




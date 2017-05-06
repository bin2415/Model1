import re
import matplotlib.pyplot as plt
fileName = "best_bob_eve_110.log"
f = open(fileName,'r')
data = list()
data2 = list()
for line in f.readlines():
    line = line.strip()
    if line != "":
        regex = re.compile(r'(\w|\W)*bob bit error (.+?),(\w|\W)*')
        result = regex.findall(line)
        data.append(float(result[0][1]))
        regex1 = re.compile(r'(\w|\W)*eve bit error (.+?),(\w|\W)*')
        result1 = regex1.findall(line)
        data2.append(float(result[0][1]))

f.close()
xlabel = range(0, 50000, 100)
plt.figure()
plot1 = plt.plot(xlabel, data, 'r')
plot2 = plt.plot(xlabel, data2, 'g')
plt.xlabel('training iteration', fontsize = 16)
plt.ylabel('bit error', fontsize = 16)
plt.legend([plot1, plot2],('bob bit error', 'alice bit error'), numpoints = 1)
plt.savefig("./training_bob_eve.png")



    
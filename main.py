import numpy as np
import matplotlib.pyplot as plt
import os

os.system('cls')

#! first of all we declare an array of risks, and we start our trades with 1% per trade as usual
risks = [0.005, 0.0075, 0.01, 0.0125, 0.015, 0.0175, 0.02]

#! most of people think that the worst state in trading is that all trades hit stop loss in a row
#! but it is proved that if all your trades hits stop loss and you decrease your risk per trade to half after 4 loss in a row,
#! then if number of trades that hits stop loss goes to infinite, your overal loss goes to under 10%
#! here is the simulation:

test_risk = 0.01
init_deposit = 100
deposit = init_deposit

counter = 0
for i in range(100000):
    counter += 1
    if counter == 4:
        counter = 0
        test_risk /= 2
    init_deposit -= init_deposit * test_risk
print(f'initial deposit after 10000 loss trades : {init_deposit}')
print(f'overall loss after 10000 loss trades : {(deposit-init_deposit) / deposit}')

action = []
for i in range(600):
    action.append(1)

for i in range(400):
    action.append(0)


init_array = []
arr = []
action = np.array(action)
for H in range(100000):
    print(H)
    np.random.shuffle(action)
    init = 100
    risk = 0.01
    risk_ind = 2
    pos_count = 0
    neg_count = 0
    to_save = []
    for i in action:
        if i == 1:
            pos_count += 1
        if i == 0:
            neg_count += 1

        if neg_count == 4:
            neg_count = 0
            pos_count = 0
            risk_ind -= 1
            if risk_ind < 0:
                risk_ind = 0
            risk = risks[risk_ind] 

        if pos_count == 16:
            neg_count = 0
            pos_count = 0
            risk_ind += 1
            if risk_ind > len(risks)-1:            
                risk_ind = len(risks)-1
            risk = risks[risk_ind]

        if i == 1:
            init += init * risk
        if i == 0:
            init -= init * risk
        to_save.append(init)
    init_array.append(to_save)
    arr.append(init)

min_ = [min(x) for x in init_array]
y = [i for i in range(len(min_))]
plt.scatter(y, min_)
plt.show()

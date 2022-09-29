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

#! but now, we are going to test another state, what happens if you gain some profit and increase
#! your risk per trade? for example, gain 4 rewards and then loss 4 trades?
#! we create a search space for trades using R/R = 1 ratio and 60% accuracy
#! to cover almost all conditions, we shuffle our search space array '1000' times
#! actualy i tried 1000 000 but my RAM was not enough to store all the data so i changed it to 100 000 for my self.
#! you can change it easily


#! threshold for reward counter : 4
#! threshold for loss counter : 4
action = []
for i in range(600):
    action.append(1)

for i in range(400):
    action.append(0)

init_array = []
arr = []
action = np.array(action)
for H in range(1000):
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

        if pos_count == 4:
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

print('lowest level of balance after 1000 trades for 1000 times shuffled search space : ')
print(min_)
plt.scatter(y, min_)
plt.show()

#! and here is another state, that we increase risk per trade after 16 rewards instead of 4 :
#! threshold for reward counter : 16
#! threshold for loss counter : 4
init_array = []
arr = []
action = np.array(action)
for H in range(1000):
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
print('')
print('lowest level of balance after 1000 trades for 1000 times shuffled search space : ')
print(min_)
plt.scatter(y, min_)
plt.show()

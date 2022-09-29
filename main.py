import numpy as np
import matplotlib.pyplot as plt
risks = [0.005, 0.0075, 0.01, 0.0125, 0.015, 0.0175, 0.02]
action = []
# ind = 1
# count = 0


# for i in range(1000):
#     count += 1
#     action.append(ind)
    
#     if count == 4:        
#         count = 0
        # ind = 0 if ind == 1 else 1

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



print(arr)
print(min(arr))
# y = [i for i in range(len(arr))]

print('')
print('')
print('')
print('')
print('')

min_ = [min(x) for x in init_array]
y = [i for i in range(len(min_))]
print(min(min_))
plt.scatter(y, min_)
plt.show()

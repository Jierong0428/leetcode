from gurobi import *
import numpy as np
from datetime import datetime

M = 10000

def optimization(delta_S, X, N, T):
    m = Model("4500_HW4")
    y = [m.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, name=f"day{i}") for i in range(T)]
    m.setObjective(np.dot(delta_S, y), GRB.MAXIMIZE)
    m.addConstr(np.sum(y) == 0, "C0")
    for i in range(T):
        m.addConstr(X[i] + y[i] >= 0, f"C{i + 1}")
    m.optimize()
    return [v.x for v in m.getVars()]

def solve(T, N, alpha, pi):
    X = np.array([N] + [0] * (T - 1))
    last_obj = 0
    for t in range(10000):
        delta_S = np.zeros(T)
        for i in range(T):
            part_1 = 1
            for j in range(i + 1):
                part_1 *= (1 - alpha * X[j] ** pi)
            part_2 = -X[i] * alpha * pi * X[i] ** (pi - 1) if X[i] > 0 else 0
            for j in range(i):
                part_2 *= (1 - alpha * X[j] ** pi)
            part_3 = 0
            for k in range(i + 1, T):
                if X[i] > 0:
                    tmp = X[k] * (-alpha * pi * X[i] ** (pi - 1))
                    for j in range(i):
                        tmp *= (1 - alpha * X[j] ** pi)
                    for j in range(i + 1, k + 1):
                        tmp *= (1 - alpha * X[j] ** pi)
                    part_3 += tmp
            delta_S[i] = part_1 + part_2 + part_3
        pre_prod = np.cumprod(1 - alpha * np.power(X, pi))
        all_term = X * pre_prod
        last_obj = np.sum(all_term)
        y = np.array(optimization(delta_S, X, N, T))
        best_X = X
        pred_prod = np.cumprod(1 - alpha * np.power(X, pi))
        best_obj = np.sum(X * pre_prod)
        for i in range(1, M + 1):
            cur_X = X + y * (i * 1. / M)
            pre_prod = np.cumprod(1 - alpha * np.power(cur_X, pi))
            obj = np.sum(cur_X * pre_prod)
            if obj > best_obj:
                best_X = cur_X
                best_obj = obj
        X = best_X
        if best_obj == last_obj:
            break
        else:
            last_obj = best_obj
    return best_obj

st = datetime.now()
setParam("LogToConsole", 0)        
ans = solve(T=20, N=1000, alpha=0.001, pi=0.5)
print(ans)
print("Time elapsed:", datetime.now() - st)

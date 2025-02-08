import numpy as np

timp_tramvai = 4
timp_autobuz = 8

lambda_tramvai = 1 / timp_tramvai
lambda_autobuz = 1 / timp_autobuz

prob_tramvai_peste_5 = np.exp(-lambda_tramvai * 5)
print(prob_tramvai_peste_5)

prob_autobuz_peste_5 = np.exp(-lambda_autobuz * 5)
prob_tramvai_si_autobuz_peste_5 = prob_tramvai_peste_5 * prob_autobuz_peste_5
prob_tramvai_sau_autobuz_peste_5 = prob_tramvai_peste_5 + prob_autobuz_peste_5 - prob_tramvai_si_autobuz_peste_5

print(prob_tramvai_sau_autobuz_peste_5)

N = 100000

simul_tramvai = np.random.exponential(scale=timp_tramvai, size=N)
simul_autobuz = np.random.exponential(scale=timp_autobuz, size=N)

prob_tramvai_peste_5 = np.mean(simul_tramvai > 5)

prob_tramvai_sau_autobuz_peste_5 = np.mean((simul_tramvai > 5) | (simul_autobuz > 5))

print(prob_tramvai_peste_5)
print(prob_tramvai_sau_autobuz_peste_5)

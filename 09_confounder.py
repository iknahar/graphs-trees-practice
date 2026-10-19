import numpy as np
#
# simulated days: heat drives ice cream and sunburn, nothing else links them
rng = np.random.default_rng(46)
temp = rng.uniform(12, 34, 240)
ice = 20 + 6.0 * temp + rng.normal(0, 18, 240)
burn = 2 + 0.9 * temp + rng.normal(0, 3.2, 240)
#
print("r, all days:", np.corrcoef(ice, burn)[0, 1].round(2))   # ~0.80
#
# hold the common cause roughly fixed: compare days of similar heat
rs = []
for lo in range(12, 34, 4):
    m = (temp >= lo) & (temp < lo + 4)
    rs.append(np.corrcoef(ice[m], burn[m])[0, 1])
print("r, similar heat:", np.round(rs, 2))
print("average:", np.mean(rs).round(2))                        # ~0.16

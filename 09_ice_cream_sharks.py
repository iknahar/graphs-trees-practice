import numpy as np
#
# simulated weeks: heat sells ice cream and fills the sea with swimmers;
# nothing links ice cream to sharks directly
rng = np.random.default_rng(46)
temp = rng.uniform(8, 32, 104)
ice = 200 + 40 * temp + rng.normal(0, 120, 104)
sharks = 0.5 + 0.35 * temp + rng.normal(0, 1.6, 104)
#
print("r, all weeks:", np.corrcoef(ice, sharks)[0, 1].round(2))   # ~0.74
#
# hold the hidden cause roughly fixed: compare weeks of similar heat
rs = []
for lo in range(8, 32, 6):
    m = (temp >= lo) & (temp < lo + 6)
    rs.append(np.corrcoef(ice[m], sharks[m])[0, 1])
print("r, similar heat:", np.round(rs, 2))
print("average:", np.mean(rs).round(2))                           # ~0.13

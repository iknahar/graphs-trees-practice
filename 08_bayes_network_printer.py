from itertools import product
#
# two causes point at one symptom: paper -> fail <- driver
p_paper, p_driver = 0.10, 0.05
p_fail = {(0, 0): 0.01, (1, 0): 0.95, (0, 1): 0.90, (1, 1): 0.99}
#
# the DAG lets the joint probability factor into small pieces
joint = {}
for a, b in product([0, 1], [0, 1]):
    pa = p_paper if a else 1 - p_paper
    pb = p_driver if b else 1 - p_driver
    joint[a, b] = pa * pb * p_fail[a, b]      # the printer failed
#
z = sum(joint.values())
print("P(paper | fail) =", round((joint[1, 0] + joint[1, 1]) / z, 3))
print("P(driver | fail) =", round((joint[0, 1] + joint[1, 1]) / z, 3))
#
# explaining away: learning the tray is empty clears the driver
z2 = joint[1, 0] + joint[1, 1]
print("P(driver | fail, paper) =", round(joint[1, 1] / z2, 3))

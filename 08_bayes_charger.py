from itertools import product
#
# two causes point at one symptom: cable -> won't charge <- socket
p_cable, p_socket = 0.20, 0.05
p_dead = {(0, 0): 0.01, (1, 0): 0.95, (0, 1): 0.99, (1, 1): 0.999}
#
# the DAG lets the joint chance split into small, easy pieces
joint = {}
for c, s in product([0, 1], [0, 1]):
    pc = p_cable if c else 1 - p_cable
    ps = p_socket if s else 1 - p_socket
    joint[c, s] = pc * ps * p_dead[c, s]      # the phone stayed dead
#
z = sum(joint.values())
print("P(bad cable | dead) =", round((joint[1, 0] + joint[1, 1]) / z, 3))
print("P(dead socket | dead) =", round((joint[0, 1] + joint[1, 1]) / z, 3))
#
# explaining away: proving the socket is dead clears the cable
z2 = joint[0, 1] + joint[1, 1]
print("P(bad cable | dead, socket dead) =", round(joint[1, 1] / z2, 3))

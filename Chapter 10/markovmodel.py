import numpy as np

SUNNY = 0
CLOUDY = 1

start_probs = [0.1, 0.9] # it is almost always cloudy
transitions_from_SUNNY = [0.3, 0.7]
transitions_from_CLOUDY = [0.4, 0.6]
transition_probs = np.array([transitions_from_SUNNY,
                             transitions_from_CLOUDY])
print(transition_probs)

def joint_prob(X):
    result = start_probs[X[0]]
    for i in range(1, len(X)):
        from_state = X[i - 1]
        to_state = X[i]
        result *= transition_probs[from_state, to_state]
    return result

X = [SUNNY, SUNNY, CLOUDY, SUNNY]
print(joint_prob(X))

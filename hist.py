# Randomizing Data, generating summmary statistics, and histogram

import numpy as np
import matplotlib.pyplot as plt


#fake data, thats normal (bell)

mu= 80
sigma = 4.5

x = np.random.normal(mu, sigma, 150)

print ("Random Normal Array:", x[:30])

print ("Mean:", np.mean(x))
print ("Stand Dev", np.std(x))

plt.hist(x)
plt.show()

#there's only enough space for one cowboy in this town


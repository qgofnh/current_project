# Proj2 a)
from sklearn.datasets import fetch_20newsgroups
import matplotlib.pyplot as plt
import numpy as np
categories = [ 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware',
              'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey']
for i in categories:
    a = [len(fetch_20newsgroups(subset='train', categories=[i], shuffle=True, random_state=42).data) for i in categories]

# print a
plt.bar(np.arange(len(a)), a, 0.5, align='center', alpha=0.5)
plt.xticks(np.arange(len(a)),categories)
plt.show()

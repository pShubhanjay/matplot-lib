import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame([[0.2419, 0.3091], [0.2888, 0.3156], [0.3037, 0.3515], [0.3312, 0.4025], [0.3703, 0.3399], [0.4051, 0.4952], [0.4659, 0.5892], [0.4854, 0.5627], [0.5004, 0.6055], [0.5177, 0.6474],
                   ]
                  , columns=['train', 'test'], index=[i for i in range(1,11)])
plt.figure(figsize=(25,20))
plt.rc('xtick', labelsize=35)
plt.rc('ytick', labelsize=35)
plt.plot(df)
plt.suptitle('Accuracy Graph', fontsize=50)
plt.ylabel('Accuracy', fontsize=40)
plt.xlabel('Epoch', fontsize=40)
plt.legend(['train', 'test'], loc='upper left',prop={'size':35})
# plt.show()
plt.savefig('accuracy.png', dpi=500)

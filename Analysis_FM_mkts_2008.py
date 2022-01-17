
import pandas as pd
import numpy as np 
import seaborn as sb
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

Data_pre = pd.read_excel('/Users/fergie/Documents/Pre.xlsx')
Data_post = pd.read_excel('/Users/fergie/Documents/Post.xlsx')


Data1 = Data_pre.set_index("Date")
Data2 = Data_post.set_index("Date")

"""
#Print 2005-09 to 2007-04 (inclusive) heatmap
Data_early = Data1.drop(Data1.index[394:775])
CorMatrix_early = Data_early.corr()
sb.set(font_scale=1)   # set the font scale at 0.7
sb.heatmap(CorMatrix_early, annot=True, cmap="YlGnBu", cbar=True)
plt.show()
"""

"""
#Print 2007-05 to 2008-10 (inclusive) heatmap
Data_latter_pre = Data1.drop(Data1.index[0:394])
CorMatrix_latter_pre = Data_latter_pre.corr()
sb.set(font_scale=1)   # set the font scale at 0.7
sb.heatmap(CorMatrix_latter_pre, annot=True, cmap="YlGnBu", cbar=True)
plt.show()
"""

"""
#Print 2008-11 to 2010-01 (inclusive) heatmap
Data_early_post = Data2.drop(Data2.index[311:796])
CorMatrix_early_post = Data_early_post.corr()
sb.set(font_scale=1)   # set the font scale at 0.7
sb.heatmap(CorMatrix_early_post, annot=True, cmap="YlGnBu", cbar=True)
plt.show()
"""

#Print 2010-02 to 2011-12 (inclusive) heatmap
Data_latter_post = Data2.drop(Data2.index[0:311])
CorMatrix_latter_post = Data_latter_post.corr()
sb.set(font_scale=1)   # set the font scale at 0.7
sb.heatmap(CorMatrix_latter_post, annot=True, cmap="YlGnBu", cbar=True)
plt.show()


"""
#print overall preL heatmap
CorMatrix1 = Data1.corr()
CorMatrix1
"""

"""
#Print overall postL heatmap
sb.set(font_scale=1)   # set the font scale at 0.7
sb.heatmap(CorMatrix1, annot=True, cmap="YlGnBu", cbar=True)
plt.show()
"""



"""
#post Lehman brothers heatmap

Data_post = pd.read_excel('/Users/fergie/Documents/Post.xlsx')

Data2 = Data_post.set_index("Date")
CorMatrix2 = Data2.corr()
CorMatrix2

sb.set(font_scale=1)   # set the font scale at 0.7
sb.heatmap(CorMatrix2, annot=True, cmap="YlGnBu", cbar=True)
plt.show()

"""




"""
#plot for pre Lehmans 
returns = np.log(Data1 / Data1.shift(1))
co_var = returns.cov()*250
co_var * 100 #as a per cent 
(Data1 / Data1.iloc[0]*100).plot(figsize=(15,6));
plt.show()
"""


"""
#plot for post Lehmans 
returns = np.log(Data2 / Data2.shift(1))
co_var = returns.cov()*250
co_var * 100 #as a per cent 

(Data2 / Data2.iloc[0]*100).plot(figsize=(15,6));
plt.show()
"""




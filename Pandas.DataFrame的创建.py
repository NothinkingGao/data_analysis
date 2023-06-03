import pandas as pd
import numpy as np

# 创建dataframe的方法
# 1. 通过字典创建
df = pd.DataFrame({'id': [1, 2, 3, 4, 5]})

# 2. 通过列表创建
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])

# 3. 通过numpy数组创建
df = pd.DataFrame(np.arange(12).reshape(3, 4))

# 4. 通过series创建
df = pd.DataFrame(pd.Series([1, 2, 3, 4, 5]))

# 5. 通过字典列表创建
df = pd.DataFrame([{'id': 1, 'name': 'zs'}, {'id': 2, 'name': 'ls'}])

# 6. 通过字典列表创建
df = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'name': ['zs', 'ls', 'ww', 'zl', 'tq']})

# Series是一维数组,DataFrame是二维数组
# Series的创建
s = pd.Series([1, 2, 3, 4, 5])

# Series的创建2
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Series的创建3
s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

# Series的创建4
s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, index=['a', 'b', 'c', 'd', 'e'])

# Series的创建5
s = pd.Series(np.arange(5))

# Series的创建6
s = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])



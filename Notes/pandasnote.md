1.导入包
```python
import pandas as pd
import numpy as np
```
2.读取文件
```python
df = pd.read_csv('D:/your/file/path/filename.csv',encoding='latin1')
#可以先执行encoding前面的内容，如果出现uft8不符合的问题，加上encoding。
```
3.将时间列改为时间格式
```python
from datetime import datetime
df['time'] = pd.to_datetime(df['time'])
```
4.筛选
```python
df= df[(df['column'] >= situation) & (df['column']<= situation)]
```
5.画折线图
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
plt.plot(df['column1'],df['column2'],maker='o')
plt.xlabel('time')
plt.ylabel('value')
plt.title('figure')
plt.grid(True)#网格
plt.show()
```
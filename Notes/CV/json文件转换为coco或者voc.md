从github中下载对应文件
在文件夹中创建label.txt
> 内容为
> __ignore__
> _background_
> label

```python
#打开windows powershell
#首次运行anaconda虚拟环境运行
conda init powershell
#激活虚拟环境
#导航到又labelme2coco.py的文件夹
cd D:\img
#选择输入文件夹，输出文件夹自己命名，不用创建
python lableme2coco.py D:/img/imgjson D:/img/shuchu --labels label.txt
```

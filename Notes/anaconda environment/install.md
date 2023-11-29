调出实时窗口 ctrl K, V
## anaconda 环境配置和安装

#### 1.安装anaconda
选择清华大学开源软件镜像站。
https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
安装合适版本的anaconda
双击打开安装文件exe
> Install for: All USers
    Destination Folder: 最好是C盘
    Advanced Options: Register Anaconda3 as system Python 

配置环境
>    此电脑——属性——高级系统设置——环境变量——系统变量——path——新建
    C:\Anaconda
    C:\Anaconda\Scripts
    C:\Anaconda\Library\mingw-w64\bin
    C:\Anaconda\Libray\usr\bin
    C:\Anaconda\Library\bin
    确定——确定
    
检查配置是否成功
    cmd——python——conda --version

#### 2.使用anaconda navigator 安装虚拟环境

版本

python ==3.6 √

pandas == 0.23.4 √
numpy == 1.15.1 √

scikit-learn== 0.24.2 √ (出现no module named'sklearn.ensemble._forest,更新版本20之后)
(备注：之前模型用的0.24.2的版本保存)
scipy== 1.1.0 √ （和sk组合安装）
sklearn== 0.0
tensorflow == 1.9.0 √
keras == 2.1.6 √
Flask == 2.0.2 （和keras 组合安装）√
matplotlib == 2.2.3 √

unidecoed== 1.0.22
joblib == 0.13.0 √

ipython == 6.5.0 √
tornado== 6.1 (和ipython组合安装) √
ipykernel == 4.8.2 √ （为jupyter notebook 提供内核）
jupyter == 1.0.0 √
##### 选择 Not installed ,搜索library名称，右键选择 mark of version installation

##### 安装完成，点击开始激活虚拟环境

#### 3.修改jupyter notebook路径
打开Anaconda Prompt（base）
```python
jupyter notebook --generate-config
#创建配置文件，输入后会显示一个路径
#打开路径找到Jupyter_notebook_config,用记事本打开
#使用ctrl F 找到 c.NotebookApp.notebook_dir=''
#删除最前面的#号，然后输入路径
c.NotebookApp.notebook_dir=r'D:\\文件名'
```
找到jupyter notebook 快捷方式，右键属性。将目标最后的"%USERPROFILE%/"删除（包括引号）。点击确定。

修改完成。

### VScode 使用虚拟环境
vscode管理员身份打开
vscode下载python扩展包
ctrl shift p 打开命令交互面板
输入
```python
Python: Select Interpreter
```
选择虚拟环境解释器
完成
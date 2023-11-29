## notes:
一张图，把目标用一个框标出来，就是目标检测算法。把属于猫的像素点标出来，语义分割算法。目标检测可以区分个体但不够精确。语义分割可以划分像素点但不可以区分个体。
实例分割达到两者的优势和解决劣势。拿到一张图片，为了防止失真和保证语义分割效果的精确，在图像的边缘加上灰度，同时还要保证图像的边长可以整除二的六次方。
Mask R-CNN 第一步利用先验框获得建议框，第二步利用建议框获得预测框，第三步利用预测框获得语义分割结果。相对于faster RCNN利用特征金字塔增加了一些公用特征层，并在最后获得预测结果后，增加了一个语义分割模型用于进行语义分割。

配置：
    配置tensorflow1.13.2 keras2.1.5
    安装CUDA前需要安装Visual Studio, 2017版本
    30系显卡不适合，30系需要安装CUDA 11.0,及对应的cudnn和高版本的tensorflow2
    安装完tensorflow后利用命令装h5py=2.10.0
    如果报typeError:_array_()takes 1 positional argument but 2 were given.修改pillow==8.2.0
    其他依赖库，tqdm，opencv等在激活环境后用pip装。

环境内容：tensorflow-gpu:1.13.2 keras:2.1.5 numpy:1.17.4
anaconda 2019
安装时勾选自动配置
下载cuda10.0,cudnn 7.4.1.5

安装cuda
>    双击ext文件
> 选择自定义

解压cudnn,打开文件夹，复制子文件到cuda根目录

配置tensorflow环境
>启动cmd
```python
#创建虚拟环境
conda create -n tensorflow-gpu python=3.6
#激活环境
activate tensorflow-gpu
#安装tensorflow-gpu和keras
pip install tensorflow-gpu==1.13.2
pip install keras==2.1.5
```
如果安装慢，在用户文件夹下，创建一个pip文件夹，在pip文件夹下创建一个pip.ini文件，写入
```python
[global]
index-url = http://pypi.mirrors.ustc.edu.cn/simple
[install]
use-mirrors = true
mirrors = http://pypi.mirrors.ustc.edu.cn/simple
trusted-host = pypi.mirrors.ustc.edu.cn
```
全部安装完成后重启电脑

使用anaconda navigator ,选择环境，安装vscode,
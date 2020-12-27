# wind python API

   设置 wind 的python 量化接口，wind推荐的方法是用 app 内置的修复按钮（网上很多人推荐的也是这个办法）
   但是事实上，按了之后，根本不清楚，wind 到底对电脑做了什么手脚
   是不是背地里安装、设置了什么东西
   
   因此，我们不通过这个途径，自己设置 python 接口
   
   1.找到 C:\Wind\Wind.NET.Client\WindNET\x64 这个目录
   
   2.确认该目录下有 WindPy.py ,WindPy.dll 这两个文件
   
   3.打开一个文件编辑器，输入 C:\Wind\Wind.NET.Client\WindNET\x64，保存为 pe.pth，注意去掉.txt，后缀为 .pth
   
   4.在D 盘新建 wind的 虚拟环境 python -m venv wind_venv
   
   5.把 pe.pth 放入 D:\Python\wind_venv\Lib\site-packages
   
   6.打开cmd，进入 wind_venv目录下的 python
   
   7.测试 import WindPy，以及 WindPy.w.start()，成功运行，说明wind 的python 接口安装好了
   
   8.再回到 pycharm 与 wind_venv 关联，指定解释器，再测试 import WindPy，WindPy.w.start() ，均成功
   
    

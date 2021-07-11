# pip install of no deps and install with txt on Windows

    在 windows下安装一个package，例如 web3 ，但是web3 依赖的包 bitarray，需要c编译器，导致安装失败时
    仍然想要安装 web3 ，同时也不想在windows上安装c编译器，怎么解决这个问题
    
    1.在 linux里，先安装c编译器
      >> sudo xbps-install gcc      
      
    2.在linux里，创建 web3 ，虚拟环境
      >> python -m venv web3      
      
    3.在linux 里安装 web3
      >> web3/bin/pip install web3   
    
    4.pip freeze 检查web3 虚拟环境里面已安装的包
      >> web3/bin/pip freeze
      aiohttp==3.7.4.post0
      async-timeout==3.0.1
      attrs==21.2.0
      bitarray==1.2.2
      certifi==2021.5.30
      chardet==4.0.0
      cytoolz==0.11.0
      eth-abi==2.1.1
      eth-account==0.5.4
      eth-hash==0.3.1
      eth-keyfile==0.5.1
      eth-keys==0.3.3
      eth-rlp==0.2.1
      eth-typing==2.2.2
      eth-utils==1.10.0
      jsonschema==3.2.0
      lru-dict==1.1.7
      multiaddr==0.0.9
      
    5.我们将 freeze 查到的结果，copy到一个web3.txt文件中
      并删除掉其中的 bitarray==1.2.2， cytoolz==0.11.0 ，因为这两个需要 c编译器
    
    6.打开windows 的 cmd，cd到 d://python目录下，创建web3 的虚拟环境
      >> python -m venv web3_venv
      
    7.在windows的 web3虚拟环境下，安装 web3
      >> D:\Python\web3_venv\Scripts\pip install -r C:\Users\april\Desktop\web3.txt -i https://pypi.douban.com/simple --no-deps
      -r requirement，根据txt的要求来安装
      --no-deps，是安装时不依赖其他包，只安装 txt里指定的包，必须要加上这项，否则pip又会自动安装 cytoolz等
      
    8.安装发现报错，lru-dict依然需要 c编译器，于是回到 web3.txt,继续删除 lru-dict==1.1.7,再次安装
      >> D:\Python\web3_venv\Scripts\pip install -r C:\Users\april\Desktop\web3.txt -i https://pypi.douban.com/simple --no-deps
      安装成功
      
    9.在pycharm里，为新web3虚拟环境配置新的project，让 project 可以被导入刚安装的 web3相关的安装包
      >> import web3
      发现报错，提示没有安装web3依赖的 cytoolz等，但是pycharm的 py文件里，可以对 web3模块的相关命令，进行补全
      因此，我们可以在 pycharm里面编辑，然后在 linux里面运行py文件
      
    10.我们可以在 linux里，检验 --no-deps的功能，创建一个 no-deps 的虚拟环境
      >> python -m venv no-deps
      >> no-deps/bin/pip install eth-abi --no-deps -i https://pypi.douban.com/simple
      >> no-deps/bin/pip list
      Package    Version
      ---------- -------
      eth-abi    2.1.1
      pip        21.1.1
      setuptools 56.0.0
      可以看到这里，只安装了 eth-abi ，eth-abi依赖的cytoolz，没有被安装
      pip，setuptools 是创建虚拟环境时，自动生成的 
      
    9.我们可以在linux 里创建一个 init 虚拟环境，来检验 pip，setuptools 
      >> python -m venv init
      >> init/bin/pip list
      Package    Version
      ---------- -------
      pip        21.1.1
      setuptools 56.0.0
      
    11.删除刚刚创建的2个测试虚拟环境
      >> rm -rf init      # -r 递归删除  -f 删除不用询问      
      >> rm -rf no-deps
      
    12.安装 eth-abi，因为eth-abi依赖 toolz库，toolz库有2个版本，一个是 cytoolz（c编辑器得版本），另一个是纯python得版本
       选择其中一个就可以，pip会默认先安装 cytoolz ，在windows上就会报错，因此也用上面类似得办法通过 .txt 文件来安装
       linux：
       >> python -m venv eth
       >> eth/bin/pip install eth-abi -i https://pypi.douban.com/simple
       >> eth/bin/pip freeze
       
       拷贝结果至 eth.txt，并删除 cytoolz==0.11.0
       windows cmd：
       >> python -m venv eth
       >> eth\script\pip install -r eth.txt -i https://pypi.douban.com/simple --no-deps
       安装成功，测试一下
       
       >> py
       >> import eth_abi   # 注意：这里不是 import eth-abi，这个名字中间有“-”在windows里是无法import的
                                   pip安装的那个名字，跟import的不一定对应的
     
       
       

    
      
      
    
      
    
      

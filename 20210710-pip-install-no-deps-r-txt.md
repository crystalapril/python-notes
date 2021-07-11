# pip install of no deps and install with txt on Windows

    在 windows下安装一个package，例如 web3 ，但是web3 依赖的包 bitarray，需要c编译器，导致安装失败时
    仍然想要安装 web3 ，同时也不想在windows上安装c编译器，怎么解决这个问题
    
    1.在 linux里，先安装c编译器
      >> sudo xbps-install gcc      
      
    2.在linux里，创建 web3 ，虚拟环境
      >> python -m venv web3      
      
    3.在linux 里安装 web3
      >> web3/bin/pip install web3   
    
    4.检查web3 虚拟环境里面已安装的包
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
      
    8.我们可以在 linux里，检验 --no-deps的功能，创建一个 no-deps 的虚拟环境
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
      
    9.我们可以创建一个 init 虚拟环境，来检验 pip，setuptools 
      >> python -m venv init
      >> init/bin/pip list
      Package    Version
      ---------- -------
      pip        21.1.1
      setuptools 56.0.0
      
      
    
      
    
      

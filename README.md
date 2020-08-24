# sdu_green_code

> 仅供研究学习使用。

# 服务搭建

1. 安装 mitmproxy 与  beautifulsoup4 ：[https://docs.mitmproxy.org/stable/overview-installation/#installation-from-the-python-package-index-pypi](https://docs.mitmproxy.org/stable/overview-installation/#installation-from-the-python-package-index-pypi)
2. git clone [https://github.com/suxb201/sdu_green_code.git](https://github.com/suxb201/sdu_green_code.git)
3. cd sdu_green_code
4. mitmdump -p 10009 --set block_global=false -q -s main.py

# 使用教程 IOS

假设你已经部署服务在 100.100.100.100 的 10007 端口上。

1. 在 wifi 设置添加代理
    1. 服务器：100.100.100.100
    2. 端口：10007
2. 使用 Safari 浏览器访问 [mitm.it](http://mitm.it) ，点击 Apple 图标。弹出窗口 “此网站正尝试下载一个配置描述文件。您要允许吗？”，点击 “允许”。
3. 设置 → 通用 → 描述文件 → mitmproxy → 安装 （期间会要求输入密码）
4. 设置→ 通用 → 关于本机 → 证书信任设置 → mimproxy 打勾
5. 打开 “山大校园通”，扫码即可

![](./doc/demo.png)
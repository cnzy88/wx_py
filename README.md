# 介绍

最近在搞python微信公众号开发，写着感觉虽然不难但是东西很多，索性就写了一个小的方便处理的框架。
能方便处理，具有扩展性。

暂时实现了微信登录，微信支付，发送模板消息，微信菜单，回复消息等服务。
如果需要新的，可以基于框架去扩展。

wechat目录:  封装了微信公众号处理的相关类，以及微信主动推送消息时的相关事件处理.

web目录：  用flask简单实现接收微信消息的相关接口。

config.py  配置文件
    
## Install

支持Python2和Python3。测试版本:Python2.7和Python3.7,可以正常运行。

pip install -r requirements.txt

## Usage

python server.py

```
```


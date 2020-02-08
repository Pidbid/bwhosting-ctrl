# Bwhosting-Ctrl
> 一个简单的基于Python语言的搬瓦工VPS控制“模块”
## 如何使用？
- 登录搬瓦工官网，国内可以选择登录[国内特殊搬瓦工](htp://www.bwh88.net)
- 点击 “My Services”
- 点击需要管理的服务，如下
![点击进入管理的图片](https://github.com/Pidbid/bwhosting-ctrl/blob/master/img/bwh001.png)
- 进入管理页面后点击“API”
- 记录您的VEID后点击“Show API Key”记录您的APIKEY
![点击进入管理的图片](https://github.com/Pidbid/bwhosting-ctrl/blob/master/img/bwh002.png)
- 获取APIKEY以及VEID后即可使用
## 示例
将bwh.py文件储存在您编辑的文件同一路径下
> import bwh  
veid = '123456'  
apikey = 'my_api_key'  
vps = bwh.Bwh(veid,apikey)  
vpsInfo = vps.start() #to start your vps  

## 其他功能
- start() #启动您的VPS，返回一个JSON实体
- stop() #关闭您的VPS，返回一个JSON实体
- restart() #重启您的VPS，返回一个JSON实体
- getServiceInfo() #获取您的VPS信息，返回一个JSON实体
- creatSnapshots(str:descripthin) #创建一个快照，返回一个JSON实体 
>description:该快照的描述，类型为字符串

## 了解更多
可以在作者博客了解更多介绍[歪克士](https://www.wicos.me)

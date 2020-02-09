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
### 基础功能
- start() #启动您的VPS，返回一个JSON实体
- stop() #关闭您的VPS，返回一个JSON实体
- restart() #重启您的VPS，返回一个JSON实体
- getServiceInfo() #获取您的VPS信息，返回一个JSON实体
- creatSnapshots(str:descripthin) #创建一个快照，返回一个JSON实体   
>description:该快照的描述，类型为字符串  
- setPtrRecord(ip,ptr) #
- kill() #强制停止此VPS，但有可能数据会丢失。
- getAvailableOS() #获取可用的系统，用于重装
- reinstallOS(osName) #重装系统
> osName:系统的名称，可以先运行getAvailableOS()获取
- resetRootPassword() #重置ROOT用户密码，新密码会再JSON实体内返回
- getUsageGraphs() #
- getRawUsageStats() #
- getAuditLog() #获取log
- setHostname(newHostname) #设置一个新的Hostname
### 数据备份，数据迁移
- getSnapshotList() #获取快照列表
- snapshotDelete(snapshot) #删除快照
> snapshot:快照名称
- snapshotRestore(snapshot) #将创建的快照覆盖现有系统
> snapshot:快照名称
- snapshotToggleSticky(snapshot,sticky) #将现有创建的快照设置为不自动删除快照
> snapshot:快照名称  
sticky: 为0时删除一个“不自动删除快照”，为1时创建一个“不自动删除快照”
- snapshotExport(snapshot) #生成一个快照的令牌，可以将这个令牌传输到另外的VPS实例内安装，返回一个导出快照的JSON实体
> snapshot:快照名称
- snapshotImport(sourceVeid,sourceToken) #导入一个快照
> sourceVeid:快照的VEID
sourceToken:快照的令牌
- getBackupList() #获取自动备份的系统列表
- backupCopyToSnapshot(backup_token) #将备份的系统复制到可恢复的快照中
> backup_token:备份的令牌
- ipv6Add(ip) #分配一个新的IPV6地址
> ip:首次分配时ip为空，再次申请时要再同一个64子网内
- ipv6Delete(ip) #删除指定的IPv6地址
> ip:指定的IP，类型为：str
- migrateGetLocations() #返回可用的“可迁移数据中心”
- migrateStart(location) #开始迁移VPS向一个新的数据中心
> location:必须是migrateGetLocations()返回的可用的数据中心地址，类型为：str
### 违规信息，安全类功能
- getSuspensionDetails() 
- getPolicyViolations() #
- unsuspend(record_id) #
- resolvePolicyViolation(record_id) #
- getRateLimitStatus() #
- privateIpGetAvailableIps() #
- privateIpAsign(ip) #
- privateIpDelete(ip) #
## 了解更多
可以在作者博客了解更多介绍[歪克士](https://www.wicos.me)  
# Orderseat
来选座:湘潭大学


本程序的原作者为罗申申 "TECH申申" WeiBo：https://weibo.com/u/5585212629

https://github.com/luoenen/HUELibraryAutoBook

因为我一个同学哥们要考湘潭大学研究生，所以将原作者河南财经政法大学选座改为湘潭大学选座


在2019.9 发现来选座系统验证码逻辑对应变动，所以花了一段时间解决了这个问题


现在本程序可以根据js计算出验证码，不再是原作者写死在配置文件中的对应了。


如需传播请征求原作者同意


需修改execjs包中的_external_runtime.py，找到Popen(有两处)，在参数列表中添加encoding='utf-8'，如

p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=self._cwd, universal_newlines=True,encoding='utf-8')

自行配置execjs node.js



2019.09.19


请自行安装python3，execjs，调整文件编码问题


使用需修改system_config中的SessionId，具体教程https://www.bilibili.com/video/av39398182

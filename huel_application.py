# 本程序的原作者为罗申申 "TECH申申" WeiBo：https://weibo.com/u/5585212629
# 他的B站地址为https://space.bilibili.com/85750427?spm_id_from=333.788.b_765f7570696e666f.2，内有教程
# https://github.com/luoenen/HUELibraryAutoBook
# 因为我一个同学哥们要考湘潭大学研究生，所以将原作者河南财经政法大学选座改为湘潭大学选座
# 在2019.9 发现来选座系统验证码逻辑对应变动，所以花了一段时间解决了这个问题
# 现在本程序可以根据js计算出验证码，不再是原作者写死在配置文件中的对应了。
# 如需传播请征求原作者同意
# 需修改execjs包中的_external_runtime.py，找到Popen(有两处)，在参数列表中添加encoding='utf-8'，如
# p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=self._cwd, universal_newlines=True,encoding='utf-8')
# 自行配置execjs node.js
# 二次开发作者:天志 Q1244517363 
# GitHub: https://github.com/tian0zhi/Orderseat
# 2019.09.19
import re
import time
import system_book_timer
import system_config
import system_function
import huel_library_urls
import lxzVcodeget


if __name__ == "__main__":

	print("准备进入系统......")
	verify_code = None

	response = system_function.into_index(huel_library_urls.index_url)
	if "来选座" in response:
			print("成功进入系统......")
	else :
		print("未成功进入系统，建议更新SessionId再试!!\n")
		exit(0)
	result = system_function.obtain_js(response)
	request_js = result[1]
	need_js = re.findall(r"layout/(.+?).js",request_js)
	print("js已获取："+need_js[0])
	verify_code = lxzVcodeget.verify_code_get(need_js[0])
	print("验证码为:"+verify_code)

	url = huel_library_urls.booked_url+verify_code+'=11,18&yzm='
	print("选座已就绪......")
	while system_book_timer.timer_setting():
		while True:
			result = system_function.booking(url)
			print(result)
			if '成功' in result:
				print("选座成功")
				break
			print("重试...")
			# 如需丧心病狂的抢座请将time.sleep 中的值尽量调小，或把代码注释，但有可能被封ip(不确定)。
			time.sleep(0.05)


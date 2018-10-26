#case_dir:保存的是用例的路径
#pattern匹配规则为“test*.py”也就是通过正则表达式找到test开头，py结尾文件
import unittest
#从工程下面的第一次开始导入，可以导入文件的内容作为库
from common.HtmlRunner import HTMLTestRunner

#用例存储路径
sdir = r"F:\untitled\shizhan\case"
rule = "test*.py"

#执行所有用例
discover = unittest.defaultTestLoader.discover(sdir,rule)
print(discover)

#执行后生成高级报告
fp = open("result.html","wb")
runner = HTMLTestRunner(fp,
                          title="这里是报告的标题，比如xx项目接口自动化报告",
                          description="报告如下：")
runner.run(discover)
fp.close()#这里报告最终必须关闭，不关闭无内容

"""
#这里是低级报告，也就是unittest自带报告，不推荐，如果使用，上面的生成报告可以不写
runner = unittest.TextTestRunner()
runner = run(discover)
"""

















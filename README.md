# 代码逻辑

首先是利用downloadHtml下载网页。但是要注意对中文字符的处理，这里我们用chardet库来检测网页编码。
然后把里面的通知列表，用正则表达式过滤下来，保存在txt文件中。
程序运行两次以后，比较originalFile和presentFile区别，将区别写入differFile中。
最后，利用smtplib自动发送邮件。

# 代码文件结构
* downloadHtml 下载web页面，并过滤列表信息保存成txt文件
* getEncoding 获取web编码
* differText 对比文件内容的不同
* sendMail 发送邮件
* monitorWeb 文件主模块，监控web页面是是否有更新

# 依赖性
  chardet

# 注意
  sendMail中需要添加邮件账户，才能运行主模块monitorWeb。

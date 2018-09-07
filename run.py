#coding=utf-8

import unittest
import HTMLTestRunner
import time
from config import globalparam
from public.common import sendmail
from public.common import publicfunction

def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test_basic_data.py')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)

    #截图
    # publicfunction.get_img(dr=? ,'test.png')

    # time.sleep(3)
    # # 发送邮件
    # mail = sendmail.SendMail()
    # mail.send()

if __name__=='__main__':
    run()
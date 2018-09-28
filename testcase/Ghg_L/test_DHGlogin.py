#coding=utf-8

from public.common import mytest
from public.pages import login_page
import time
from public.common import datainfo
from public.common.publicfunction import get_img


class Dhg_Test(mytest.MyTest):

    def test_login_test(self):
        page = login_page.IndexPage(self.dr)
        page.into_page('http://192.168.0.135:9090/')
        page.input_username_key('jjqlyj')  # 账户
        page.input_password_key('123456')  # 密码
        page.input_code_key('0')  # 验证码
        page.click_button()  # 登录
        time.sleep(7)

        self.assertEqual(u'重庆旅游行业管理平台V3',page.return_title())





#coding=utf-8

from time import sleep
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img


class TestBaiduIndex(mytest.MyTest):
    """测试"""

    def _search(self,data_values):
        """封装的函数"""
        page = login_page.IndexPage(self.dr)
        page.into_page('http://192.168.0.65:8010/')
        page.input_username_key(data_values[0])
        page.input_password_key(data_values[1])
        page.input_code_key(data_values[2])
        page.click_button()
        sleep(2)
        # self.assertIn(title, page.return_title())

    # def test_search(self):
    #     """直接"""
    #     page = login_page.IndexPage(self.dr)
    #     page.into_page()
    #     page.input_username_key('admin')
    #     page.input_password_key('123456')
    #     page.click_button()
    #     sleep(2)
    #     self.assertIn('旅游公共信息服务平台',page.return_title())


    def test_search_excel(self):
        """使用数据驱动,进行测试"""
        datas = datainfo.get_excel_data('searKey_1.xlsx','Sheet1',1)
        # for data in datas:
        #     self._search(data)
        self._search(datas)





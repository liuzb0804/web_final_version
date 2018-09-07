#coding=utf-8
import time,os
from public.common import basepage
import login_page

class MainPage(basepage.Page):

    def project_number(self,project):
        """选择（一级目录）"""
        # project = u'资源管理'
        for i in range(7):
            xpath = '//*[@id="itemUl"]/li[' + str(i) + ']'
            xpath_text = '//*[@id="itemUl"]/li[' + str(i) + ']/a/p'
            try:
                text = self.dr.find_element_by_xpath(xpath_text).text
                if text == project:
                    return self.dr.find_element_by_xpath(xpath).click()
            except:
                pass


    def type_number(self,TLC):
        """选择（二级目录）"""
        for i in range(10):
            xpath = '//*[@id="js_nav"]/ul/li[' + str(i) + ']'
            xpath_text = '//*[@id="js_nav"]/ul/li[' + str(i) + ']/a/span'
            try:
                name = self.dr.find_element_by_xpath(xpath_text).text
                # print name
                if name == TLC:
                    return self.dr.find_element_by_xpath(xpath).click()
            except:
                pass

    # 若存在第三级，则路径为：
    # xpath = '//*[@id="js_nav"]/ul/li[' + str(i) + ']/ul/li[' + str(j) + ']/a/span'
    # 若还有下一级目录，则路径继续加 /ul/li
    # xpath = '//*[@id="js_nav"]/ul/li[' + str(i) + ']/ul/li[' + str(j) + ']/ul/li[' + str(k) + ']/a/span'

    # type_name(TLC=u'景区')







    def select_click(self,values):
        """选择"""
        self.dr.click('id->id',values)

    def switch_frame(self,values):
        """切frame"""
        self.dr.switch_to_frame('id->id',values)

    def select_action(self,values):
        """选择操作"""
        self.dr.click('id->id',values)

    def input_data(self,values):
        """键入数据"""
        self.dr.clear_type('name->name',values)








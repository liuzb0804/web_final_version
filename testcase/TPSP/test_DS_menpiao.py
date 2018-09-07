# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_menpiao(mytest.MyTest):
    '''
    用例编号：
    模块：
    功能点：
    测试点描述：
    测试步骤：

    预期结果：

    '''

    def test_login_page(self):
        """ login """
        #************************** login ************************
        page = login_page.IndexPage(self.dr)
        page.into_page('http://192.168.0.65:8010/')
        page.input_username_key('admin')
        page.input_password_key('123456')
        page.click_button()
        time.sleep(7)
        self.assertEqual(u'旅游公共信息服务平台', page.return_title())

        #************************** porject ***********************
        self.dr.click('id->systemName')
        time.sleep(1)

        self.dr.click('xpath->/html/body/div[1]/ul/li[2]/ul/li[7]')
        time.sleep(3)

        self.dr.click('id->790')#产品管理
        time.sleep(2)

        self.dr.click('id->792')#门票
        time.sleep(3)

        #************************ 切换frame **********************
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)

        #************************* before check ********************
        text_before = self.dr.get_text('xpath->//*[@id="listForm"]/div[4]') #获取当前页面条数显示信息
        print text_before

        #************************** actions ************************
        self.dr.click('xpath->//*[@id="listForm"]/div[2]/a[1]') #点击添加
        self.dr.sleep(3)





        #选择景区 *
        self.dr.click('id->companyName')    #打开景区列表
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div[5]/div[2]/table/tbody/tr[1]')  #景区列表第一个
        #2： 输入景区名
        self.dr.type('xpath->/html/body/div[5]/div[1]/input','******')  # * 搜索条件
        self.dr.click('xpath->/html/body/div[5]/div[1]/a')  #搜索键
        self.dr.click('xpath->/html/body/div[5]/div[1]/button') #清空

        #选择票型 *     此受限于选择景区的选择
        self.dr.click('id->companyType')    #打开票型列表
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="companyType"]/option[2]')    #列表第二个
        #新增票型
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/a')

        #产品名称 * （2-60字）
        self.dr.type('name->name','*******')    # * 为输入数据

        #服务特色 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/span/label') #随时退
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/span/span')#秒发码

        #对接接口
        self.dr.click('id->appkeyType') #选择对接接口，点击
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="appkeyType"]/option[2]') #列表第二个
        #输入
        self.dr.type('name->outSn','****')  #* 为输入数据

        #商户
        self.dr.click('id->supplierName')   #打开列表
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div[6]/div[2]/table/tbody/tr[1]')  #第二个
        #2：
        self.dr.type('xpath->/html/body/div[6]/div[1]/input','*****')   #输入搜索条件
        self.dr.type('xpath->/html/body/div[6]/div[1]/a')   #点击搜索
        self.dr.click('xpath->/html/body/div[6]/div[1]/button') #清空

        #验票人
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label')  #用户可验票
        self.dr.click('id->selectCheckTicketMember')    #其他验票人
        #切iframe
        self.dr.switch_to_frame('id->browserFrame1535075562203244887')
        self.dr.sleep(3)
        #选择验票人：
        self.dr.click('id->selectAll')  #全选
        self.dr.click('xpath->//*[@id="listTable"]/tbody/tr[2]')    #选择第一个
        self.dr.click('xpath->/html/body/div[9]/div[4]/input[1]')   #确定
        self.dr.click('xpath->/html/body/div[9]/div[4]/input[2]')   #关闭
        self.dr.type('id->searchValue') #输入条件
        self.dr.click('xpath->//*[@id="listForm"]/div[1]/button')   #点击查询
        #回到main frame
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #商品头图   (单次)
        self.dr.click('xpath->/html/body/div[8]')   #点击上传新图片
        self.dr.sleep(3)
        os.system('D:\WinClick3.exe')   #路径
        self.dr.sleep(3)









        #************************ check after ************************
        pass

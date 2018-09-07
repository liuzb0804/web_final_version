# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import ramdon
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_px_htgl_007(mytest.MyTest):
    '''
    用例编号：px_htgl_007
    模块：门票
    功能点：添加
    测试点描述：必填项分别分空
    测试步骤：
        1、进入门票添加页
        2、必填项逐一为空
        3、点击“保存”
    预期结果：
        1、提示XXX为必填项，不能为空或者其他提示信息
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

        #1：
        # self.dr.click('xpath->/html/body/div[1]/ul/li[2]/ul/li[7]')
        # time.sleep(3)
        #2：
        a = '电商运营子系统'
        for i in range(10):
            path = 'xpath->/html/body/div[1]/ul/li[2]/ul/li[' + str(i) + ']'
            try:
                text = self.dr.get_text(path)
                text_1 = text[2:]
                text_code = text_1.encode('utf-8')
                if text_code == a:
                    self.dr.click(path)
                    break
            except:pass


        self.dr.click('id->790')#产品管理
        time.sleep(2)

        self.dr.click('id->792')#门票
        time.sleep(3)

        #************************ 切换frame **********************
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)

        #************************* before check ********************
        #必填项:选择景区，选择票型，产品名称，服务特色，验票人，出售时间，兑换凭证，入园方式
        #入园地址，短信模板，价格库存模式，验证消费日期，价格库存，退款说明，费用包含，使用说明
        fake = Factory.create("zh_CN")

        #************************** actions ************************
        self.dr.click('xpath->//*[@id="listForm"]/div[2]/a[1]')
        time.sleep(2)

        # 选择景区
        self.dr.click('id->companyName')
        time.sleep(1)
        self.dr.click('xpath->/html/body/div[5]/div[2]/table/tbody/tr[1]')#选择景区
        time.sleep(1)
        #验证点击后框体是否消失
        try:
            element = self.dr.get_element('xpath->/html/body/div[5]/div[2]/table/tbody/tr[1]')
            if element is None:
                pass
            else:raise IOError
        except:pass



        # 选择票型
        self.dr.click('id->companyType')
        time.sleep(2)
        self.dr.click('xpath->//*[@id="companyType"]/option[2]')#选择票型
        time.sleep(1)


        # 产品名称（2-60字）
        # name = ramdon.ramdondata(61)
        self.dr.type('name->name', '1')     #最短-1
        # self.dr.type('name->name', name)    #最长+1
        #验证1：当前验证
        #验证2：需保存后，验证


        # 服务特色（可多选）（单次点击是选中，二次点击是取消）
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/span/label') #随时退
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/span/span')  #秒发码

        # 验票人
        self.dr.click('id->selectCheckTicketMember')#其他验票人
        time.sleep(2)
        self.dr.click('xpath->//*[@id="listTable"]/tbody/tr[2]')#选择验票人（1）  单次为选中，二次为取消
        time.sleep(1)
        self.dr.click('xpath->//*[@id="listTable"]/tbody/tr[3]')#选择验票人（2）
        time.sleep(1)
        # 出售时间 3个选项
        #1：默认
        #2： click-input
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[18]/td/label[2]')
        time.sleep(1)
        self.dr.click('id->saleStartTime')
        time.sleep(1)
        self.dr.click('id->dpTodayInput')#今天
        time.sleep(2)
        self.dr.click('name->saleEndTime')
        time.sleep(1)
        self.dr.click('id->dpTodayInput')  # 今天
        time.sleep(2)

        # 兑换凭证  4个选项
        #1:默认       确认短信
        #2：
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/label[2]')#身份证
        #3:
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/label[3]')#短信和身份证
        #4：
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/label[4]')#电子邮件确认单

        # 入园方式  2个选项
        #1：默认
        #2：
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[2]')
        time.sleep(1)
        self.dr.type('name->pickupAddress',fake.address())#地址
        time.sleep(1)
        self.dr.type('name->pickupTime',fake.date(pattern="%Y-%m-%d"))#时间

        # 入园地址
        self.dr.type('name->passAddress',fake.address())

        # 短信模板
        self.dr.click('id->smsThemeId')
        time.sleep(1)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[23]/td/div/ul/li')
        time.sleep(2)

        #价格库存
        # 价格库存模式  2个选项  选项不同，要求所填内容不同。 先为默认模式
        #1：默认       日历价格库存模式
        # 验证消费日期
        #1：默认
        #2：
        self.dr.click('xpath->//*[@id="consumeAuthen"]/td/label[2]')
        time.sleep(1)
        self.dr.click('name->beforeDay')
        time.sleep(1)
        self.dr.click('xpath->//*[@id="consumeAuthen"]/td/label[2]/select[1]/option[3]')
        time.sleep(1)
        self.dr.click('name->afterDay')
        time.sleep(1)
        self.dr.click('xpath->//*[@id="consumeAuthen"]/td/label[2]/select[2]/option[3]')
        time.sleep(1)

        # 价格库存
        self.dr.click('id->batchset')#批量上架
        time.sleep(2)
        self.dr.click('id->startDate_1')#时间段：开始时间
        time.sleep(2)
        self.dr.click('id->dpTodayInput')#今天
        time.sleep(2)
        self.dr.click('id->endDate_1')#时间段：结束时间
        time.sleep(2)
        self.dr.click('id->dpTodayInput')#今天
        time.sleep(2)
        self.dr.type('id->marketPrice_1','100')#票面价
        time.sleep(1)
        self.dr.type('id->stockNum_1','100')#每日库存
        time.sleep(1)
        self.dr.type('id->sellPrice_1','100')#售卖价
        time.sleep(1)
        self.dr.type('id->minimum_1','100')#最少购买
        time.sleep(1)
        self.dr.type('id->maximum_1','100')#最多购买
        time.sleep(1)
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[4]/input[1]')

        #批量下架：
        self.dr.click('id->batchunset')
        time.sleep(2)
        self.dr.click('id->startDate_3')#时间段：开始时间
        time.sleep(2)
        self.dr.click('id->dpTodayInput')#今天
        time.sleep(2)
        self.dr.click('id->endDate_3')#时间段：结束时间
        time.sleep(2)
        self.dr.click('id->dpTodayInput')#今天
        time.sleep(2)
        #星期：默认全选，选中即取消
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[1]')
        #确定
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[4]/input[1]')
        #全部下架：
        self.dr.click('id->clearall')

        # 退款说明
        self.dr.type('id->refundInfo',fake.text(max_nb_chars=200, ext_word_list=None))

        # 费用包含
        self.dr.type('id->feeInfo',fake.text(max_nb_chars=200, ext_word_list=None))

        # 使用说明
        self.dr.switch_to_frame('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[43]/td/div/div[2]/iframe')#iframe
        time.sleep(3)
        self.dr.type('xpath->/html/body',fake.text(max_nb_chars=200, ext_word_list=None))
        #回到原frame
        self.dr.switch_to_frame_out()
        time.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)


        #价格库存：第二种：总库存模式


        #验证消费日期： 3个选项


        #价格库存
        self.dr.click('id->modifyprice')#编辑价格
        time.sleep(2)


        #商品调价




        #************************ check after ************************
        #TODO

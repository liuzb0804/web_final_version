# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_zuche(mytest.MyTest):
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

        self.dr.click('id->892')#租车
        time.sleep(3)

        #************************ 切换frame **********************
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)

        #************************* before check ********************
        # text_before = self.dr.get_text('xpath->//*[@id="listForm"]/div[4]') #获取当前页面条数显示信息
        # print text_before

        #************************** actions ************************
        self.dr.click('xpath->//*[@id="listForm"]/div[2]/a[1]') #点击添加
        self.dr.sleep(3)

        #产品名称 *
        self.dr.type('name->name','***')

        #产品卖点 *
        self.dr.type('name->sellingPoint','***')

        #出发地 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[4]/td/select[1]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[4]/td/select[1]/option[4]')#省
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[4]/td/select[2]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[4]/td/select[2]/option[2]')#市
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[4]/td/select[3]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[4]/td/select[3]/option[2]')#区/县
        self.dr.sleep(2)

        #目的地 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/select[1]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/select[1]/option[4]')#省
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/select[2]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/select[2]/option[2]')#市
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/select[3]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/select[3]/option[2]')#区/县
        self.dr.sleep(2)

        #所在地 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[6]/td/select[1]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[6]/td/select[1]/option[4]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[6]/td/select[2]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[6]/td/select[2]/option[2]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[6]/td/select[3]')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[6]/td/select[3]/option[2]')
        self.dr.sleep(2)

        #商户
        self.dr.click('id->supplierName')
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div[2]/div[2]/table/tbody/tr[1]')
        self.dr.sleep(2)

        #验票人
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label')

        self.dr.click('id->selectCheckTicketMember')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->/html/body/div[4]/div[3]/div/iframe')
        self.dr.sleep(3)
        self.dr.click('id->selectAll')#全选
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('xpath->/html/body/div[4]/div[4]/input[1]')#确定
        # self.dr.click('xpath->/html/body/div[4]/div[4]/input[2]')#关闭
        self.dr.sleep(2)


        #销售渠道
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[1]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[2]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[3]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[4]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]/label[5]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[2]')

        #车辆图片 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[10]/td/div/div[2]/ul/li/div/a')
        self.dr.sleep(2)
        os.system('D:\WinClick2.exe')
        self.dr.sleep(3)

        #商品封面图
        self.dr.click('id->logoUploadBox_1_1')
        self.dr.sleep(3)
        os.system('D:\WinClick2.exe')
        self.dr.sleep(3)

        #取消设置
        self.dr.type('name->autoCancelTime','***')

        #联系人信息
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label[3]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label[4]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label[5]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label[6]')

        #预订限制
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/td/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/td/label[2]/input[1]')
        self.dr.type('name->enterSightAdvanceDay','***')
        self.dr.click('name->enterSightAdvanceHour')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="ADVANCE_BOOK_TIME"]/option[1]')
        self.dr.sleep(2)
        self.dr.click('name->enterSightAdvanceMinute')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="ADVANCE_BOOK_TIME"]/option[1]')
        self.dr.sleep(2)

        #短信模板 *
        self.dr.click('id->smsThemeId')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/div/ul/li[1]')
        self.dr.sleep(2)

        #车型等级 *
        self.dr.click('xpath->//*[@id="carGrade"]/tbody/tr/td[1]/button')#选择车型
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="carGrade"]/tbody/tr/td[1]/dl/dd[1]/input[1]')#4座及以下
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="carGrade"]/tbody/tr/td[1]/dl/dd[2]/button[1]')#确定
        self.dr.sleep(2)
        self.dr.type('xpath->//*[@id="carGrade"]/tbody/tr/td[2]/input','***')#备注

        # self.dr.click('xpath->//*[@id="carGrade"]/tbody/tr/td[3]/button')#删除
        self.dr.sleep(2)

        #套餐设置 *
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/div[1]/button')#添加新套餐
        self.dr.type('name->meal_name','***')#套餐名称
        self.dr.type('name->sale_price','***')#租赁量
        self.dr.type('name->market_price','***')#市场价
        self.dr.type('name->min_order','***')#最小租赁量
        self.dr.type('name->max_order','***')#最多租赁量
        self.dr.type('name->repertory','***')#库存

        #有效期 *
        self.dr.click('id->skuStartDate')#起始
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('name->skuEndDate')#截止
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #费用包含
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[1]')#车辆使用费
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[2]')#司导
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[3]')#拥堵
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[4]')#邮费
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[5]')#空驶
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[6]')#司导餐补
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[7]')#路桥费
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[8]')#停车费

        #出售时间 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[22]/td/label[1]')#默认
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[22]/td/label[2]/input[1]')#设定
        self.dr.sleep(1)
        self.dr.click('id->saleStartTime')#起始
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('name->saleEndTime')#截止
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        # 放入仓库
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[22]/td/label[3]')

        #退款设置
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[24]/td/label[1]')#默认
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[24]/td/label[2]')

        #退款审核
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[1]')
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[2]')#默认

        #退款说明 *
        self.dr.type('name->refundInfo','***')

        #使用说明
        self.dr.type('name->remind','***')

        #温馨提示
        self.dr.type('name->memo','***')

        #保存
        # self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[1]')

        #返回
        # self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[2]')

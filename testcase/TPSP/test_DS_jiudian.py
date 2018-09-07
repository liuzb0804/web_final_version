# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_jiudian(mytest.MyTest):
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
        self.fake = Factory.create("zh_CN")
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

        self.dr.click('id->836')#酒店
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

        #选择酒店 *
        self.dr.click('id->companyName')
        time.sleep(2)
        self.dr.click('xpath->/html/body/div[5]/div[2]/table/tbody/tr[1]')

        #商户（默认）
        #选择房型 *
        #新增
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[4]/td/a')
        # time.sleep(3)
        # self.dr.type('name->name','***')    #房型
        # self.dr.type('name->storey','***')  #楼层
        # self.dr.type('name->bedType','***') #床型
        # self.dr.type('name->num','***')      #可住人数
        # self.dr.type('name->acreage','***') #面积
        # self.dr.type('name->window','***')  #窗户
        # self.dr.type('name->wifi','***')   #wifi
        # self.dr.type('name->panorama','***')    #720全景
        # self.dr.click('xpath->//*[@id="num2"]/td[10]/button[1]')    #房型设施
        # self.dr.click('xpath->//*[@id="num2"]/td[11]/button[1]')    #房型图片
        # self.dr.click('xpath->//*[@id="num2"]/td[12]/button')   #删除
        # self.dr.click('id->butsubmit')  #保存
        # self.dr.click('xpath->//*[@id="inputForm"]/input[2]')   #返回
        # #选择
        # self.dr.click('id->companyTypeId')

        #产品名称 *
        self.dr.type('name->name','123')

        #服务特色 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[6]/td/span/label') #随时退
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[6]/td/span/span')  #秒发码

        #是否含早
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[7]/td/label[1]')   #无
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[7]/td/label[2]')   #含早
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[7]/td/label[3]')   #含双早
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[7]/td/label[4]')   #含三早
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[7]/td/label[5]')   #有（收费）

        #验票人 *
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/label')
        #其他验票人
        self.dr.click('id->selectCheckTicketMember')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->/html/body/div[8]/div[3]/div/iframe')
        self.dr.sleep(3)
        self.dr.click('id->selectAll')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('xpath->/html/body/div[8]/div[4]/input[1]')
        self.dr.sleep(2)

        #商品头图
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/div/div[2]/ul/li/div/a')
        self.dr.sleep(3)
        os.system('D:\WinClick3.exe') #AUTO
        self.dr.sleep(3)

        #商品封面图
        self.dr.click('id->logoUploadBox_1_1')
        self.dr.sleep(3)
        os.system('D:\WinClick4.exe') #AUTO
        self.dr.sleep(3)

        #销售渠道
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[11]/td/label[1]/label[1]') #C端
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[11]/td/label[2]')  #PC商场
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[11]/td/label[3]')  #购票机

        #取消设置
        self.dr.type('name->autoCancelTime','***')

        #联系人信息
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/label[3]')

        #出售时间
        #1(默认)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/td/label[1]')
        #2
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/td/label[2]/input[1]')
        self.dr.sleep(1)
        self.dr.click('id->saleStartTime')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('xpath->/html/body/div/div[6]/input[2]')
        self.dr.sleep(3)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        self.dr.click('name->saleEndTime')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(2)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #3
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[15]/td/label[3]')

        #短信模板 *
        self.dr.click('id->smsThemeId')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/div/ul/li[1]')

        #价格库存 *
        self.dr.click('id->batchset')    #批量上架

        self.dr.sleep(2)
        self.dr.click('id->startDate_1')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(2)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(3)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('id->endDate_1')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(3)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[1]')#星期1
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[2]')#星期2
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[3]')#星期3
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[4]')#星期4
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[5]')#星期5
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[6]')#星期6
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[7]')#星期7
        self.dr.sleep(1)
        self.dr.type('id->marketPrice_1', '100')#票面价
        # self.dr.type('id->stockNum_1', '100')#每日库存
        self.dr.type('id->sellPrice_1', '100')#售卖价
        # self.dr.type('id->minimum_1', '100')#最少购买
        # self.dr.type('id->maximum_1', '100')#最多购买

        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[4]/input[1]')#保存
        # self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[4]/input[2]')#取消
        self.dr.sleep(2)

        # 批量下架
        self.dr.click('id->batchunset')
        self.dr.sleep(3)
        self.dr.click('id->startDate_3')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(2)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[2]/div/label[2]')
        self.dr.sleep(2)
        self.dr.switch_to_frame('xpath->//*[@id="_my97DP"]/iframe')
        self.dr.sleep(3)
        self.dr.click('id->dpTodayInput')
        self.dr.sleep(2)
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[1]')#1
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[2]')#2
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[3]')#3
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[4]')#4
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[5]')#5
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[6]')#6
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[7]')#7

        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[4]/input[1]')#确定
        # self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[4]/input[2]')#取消
        self.dr.sleep(2)

        #全部下架
        self.dr.click('id->clearall')

        #商品调价
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/label[1]')  #是
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/label[2]')  #否

        #退款设置
        #可以退款(默认)
        self.dr.click('name->canRefund')
        #列表1：
        self.dr.click('name->partRefund')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[1]/select[1]/option[1]')
        #列表2：
        self.dr.click('id->refundChargeType')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="refundChargeType"]/option[1]')
        #输入：
        self.dr.clear_type('id->refundCharge','***')
        #不可退款
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[2]')

        #退款审核(退款设置为不可退款时，不存在此项)
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[1]')  #需要审核
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[2]')  #不需要审核

        #退款说明 *
        self.dr.type('name->refundInfo','***')

        #费用包含 *
        self.dr.type('name->feeInfo','***')

        #费用不含
        self.dr.type('name->feeExclude','***')

        #使用说明 *
        self.dr.type('name->remind','***')

        #保存
        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[1]')

        #返回
        # self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[2]')
# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_jiudian1(mytest.MyTest):
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

        self.dr.click('id->794')#酒店1.0
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
        self.dr.click('id->companyName')    #打开列表
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div[5]/div[2]/table/tbody/tr[1]')  #第一个

        #选择房型 *
        self.dr.click('id->companyType')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="companyType"]/option')    #选择第一个 ，有效数据
        # 新增
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/a')  #点击 新增

        #产品名称 * （2/60字）
        self.dr.type('name->name','*****')  # * ：输入数据

        #是否含早
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/label[1]')  # 无
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/label[2]')  # 含早
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/label[3]')  # 含双早
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/label[4]')  # 含三早
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/label[5]')  # 有（收费）

        #商户
        self.dr.click('id->supplierName')   #打开列表
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div[6]/div[2]/table/tbody/tr[1]')  #选择 第一个
        self.dr.type('xpath->/html/body/div[6]/div[1]/input','*******') #"请输入商户账号" * ：账号
        self.dr.click('xpath->/html/body/div[6]/div[1]/a')  #搜索键
        self.dr.click('xpath->/html/body/div[6]/div[1]/button') #清空键

        #验票人 *
        self.dr.click('name->isSupplierCheck')  #商户可验票
        #其他验票人
        self.dr.click('id->selectCheckTicketMember')
        #切frame
        self.dr.switch_to_frame('id->browserFrame15350796781108236')
        self.dr.sleep(3)
        self.dr.click('id->selectAll')  #全选
        self.dr.click('xpath->//*[@id="listTable"]/tbody/tr[2]')    #第一个
        self.dr.click('xpath->/html/body/div[9]/div[4]/input[1]')   #确定
        self.dr.click('xpath->/html/body/div[9]/div[4]/input[2]')   #关闭
        self.dr.type('id->searchValue','****')  #搜索条件
        self.dr.click('xpath->//*[@id="listForm"]/div[1]/button')   #查询
        #切回frame
        self.dr.switch_to_frame_out()
        self.dr.sleep(3)
        self.dr.switch_to_frame('id->indIframe')
        self.dr.sleep(3)

        #商品头图
        self.dr.click('xpath->/html/body/div[8]')
        self.dr.sleep(3)
        os.system('')   #AUTO执行程序
        self.dr.sleep(3)

        #销售渠道
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[1]')   #供销平台
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[2]/label[1]')  #C端 （全选）
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[2]/label[2]')  #产品码
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[2]/label[3]')  #商品码
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[2]/label[4]')  #专题码
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[2]/label[5]')  #店铺码
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[9]/td/label[3]')   #PC商场

        #取消设置
        self.dr.type('name->autoCancelTime','*****')

        #联系人信息（默认勾选：手机号，姓名）
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[12]/td/label[3]')

        #出售时间
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/label[1]')  #立刻上架出售，过期自动下架  (默认勾选)

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/label[2]')  #点击设定出售时间
        self.dr.click('id->saleStartTime')  #起始
        self.dr.click('name->saleEndTime')  #截止
        #时间操作
        self.dr.click('id->dpQS')            #切换显示方式
        #常规显示，为6 排 数据，操作按排数来
        self.dr.click('xpath->/html/body/div/div[3]/table/tbody/tr[6]/td[6]')   #有效时间：第五排，第六个，星期五
        self.dr.click('id->dpClearInput')   #清空
        self.dr.click('id->dpTodayInput')   #今天
        self.dr.click('id->dpOkInput')      #确定

        #短信模板 *
        self.dr.click('id->smsThemeId') #打开列表
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/div/ul/li[1]')  #第一个选项
        #新增模板
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[14]/td/a')

        #价格库存
        #批量操作
        self.dr.click('id->batchset')   #批量上架
        #弹窗
        self.dr.click('id->startDate_1')    #起始
        #时间操作同上：140-144
        self.dr.click('id->endDate_1')  #截止
        # 时间操作同上：140-144
        self.dr.click('xpath->//*[@id="dateStock"]/div[2]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/div/input[1]')  #星期一  input[2]:星期二 依次类推

        self.dr.type('id->marketPrice_1','***') #票面价 *
        self.dr.type('id->stockNum_1','***')#每日库存 *
        self.dr.type('id->sellPrice_1','***')#售卖价 *
        self.dr.type('id->minimum_1','***')#最少购买 *
        self.dr.type('id->maximum_1','***')#最多购买 * (不可小于最少购买)

        self.dr.click('id->batchunset') #批量下架
        #弹窗
        self.dr.click('id->startDate_3')    #起始
        #见140-144
        self.dr.click('id->endDate_3')  #截止
        # 见140-144
        #星期 ：见161
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[4]/input[1]')
        self.dr.click('xpath->//*[@id="unstock"]/div[2]/div[4]/input[2]')

        self.dr.click('id->clearall')   #全部下架

        #商品调价
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[17]/td/label[1]')  #是（默认）
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[17]/td/label[2]')  #否

        #退款设置
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/label[1]')  #可以退款（默认）
        self.dr.click('name->partRefund')   #打开第一个列表
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/label[1]/select[1]/option[1]')  #第一个选项：可以部分退.  option[2]:

        self.dr.click('id->refundChargeType')   #第二个列表
        self.dr.click('xpath->//*[@id="refundChargeType"]/option[1]')   #第一个选项

        self.dr.type('id->refundCharge','***')  #输入

        #不可退款
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/label[2]')  #选择不可退款，退款审核将会消失

        #退款审核（条件：退款设置为可以退款）
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[1]')  #需要审核
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[2]')  #不需要审核（默认）

        #退款说明 *
        self.dr.type('name->refundInfo','***')

        #费用说明 *
        self.dr.type('name->feeInfo','****')

        #费用不含
        self.dr.type('name->feeExclude','***')

        #使用说明 *
        self.dr.type('name->remind','***')


        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[1]')  #保存
        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[2]')  #返回



        #************************ check after ************************
        pass

# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_xianlu(mytest.MyTest):
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

        self.dr.click('id->799')#线路
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

        #产品名称 *
        self.dr.type('name->name','***')

        #服务特色
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/div[1]/label')#100%成团
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/div[2]/label')#无购物
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[3]/td/div[3]/label')#无自费

        #线路类型 *
        self.dr.click('id->lineType')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="lineType"]/option[2]')

        #出发城市 *
        self.dr.click('name->areaId_select')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[5]/td/span/select/option[2]')

        #商户
        self.dr.click('id->supplierName')
        self.dr.sleep(2)
        self.dr.click('xpath->/html/body/div[6]/div[2]/table/tbody/tr[1]')

        #验票人 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[7]/td/label')#用户可验票
        #其他验票人
        self.dr.click('id->selectCheckTicketMember')

        #线路图片 *
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[8]/td/div/div[2]/ul/li/div/a')
        self.dr.sleep(3)
        os.system('D:\WinClick3.exe')
        self.dr.sleep(3)

        #商品封面图
        self.dr.click('id->logoUploadBox_1_1')
        self.dr.sleep(3)
        os.system('D:\WinClick4.exe')
        self.dr.sleep(3)

        #销售渠道
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[10]/td/label[1]/label[1]')#1
        # self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[10]/td/label[2]')#2

        #集合信息 *
        self.dr.click('name->gather_hour')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="gatherTable"]/tbody/tr[2]/td[1]/select[1]/option[1]')#0
        self.dr.sleep(2)
        self.dr.click('name->gather_minute')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="gatherTable"]/tbody/tr[2]/td[1]/select[2]/option[1]')#0
        self.dr.sleep(2)
        self.dr.type('name->gather_addr','***')#集合地点
        # self.dr.click('id->gatherButton')#操作：添加


        #交通安排 *
        self.dr.click('xpath->inbound')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/label[1]/select/option[2]')
        self.dr.click('name->outbound')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[13]/td/label[2]/select/option[2]')

        #行程特色
        self.dr.click('name->lineFeature')

        #行程天数 * ()
        #行程安排
        #游玩景点 *
        #餐食安排
        #详细安排
        #住宿安排
        #购物安排
        self.dr.type('id->sceneryId','***')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="eat_box"]/tbody/tr[1]/td/label[1]')#早餐
        # self.dr.click('xpath->//*[@id="eat_box"]/tbody/tr[1]/td/label[2]')#酒店提供
        # self.dr.click('xpath->//*[@id="eat_box"]/tbody/tr[1]/td/label[3]')#自理  （默认）
        # self.dr.click('xpath->//*[@id="eat_box"]/tbody/tr[1]/td/label[4]')#自定义
        # self.dr.type('name->breakfast_input','***')
        self.dr.click('xpath->//*[@id="eat_box"]/tbody/tr[2]/td/label[1]')#中餐
        #同早餐
        self.dr.click('xpath->//*[@id="eat_box"]/tbody/tr[3]/td/label[1]')#晚餐
        #同早餐
        self.dr.type('name->travel_title','***')#行程时间段     范例：9：00-10:00，成都-都江堰

        #切frame
        self.dr.type('xpath->/html/body','***')
        #退出frame
        #切回主干

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/table/tbody/tr[5]/td/input')#添加行程时间段

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/table/tbody/tr[6]/th/label')
        self.dr.sleep(1)
        self.dr.type('name->stay','***')#住宿安排

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[16]/td/table/tbody/tr[7]/th/label')
        self.dr.sleep(1)
        self.dr.type('name->shop','***')#购物安排






        #取消设置
        self.dr.type('name->autoCancelTime','***')

        #联系人信息
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[19]/td/label[3]')

        #客人信息
        self.dr.click('name->needPassengerInfoCheck')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/span/label[1]')#默认
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/span/label[2]')#需要每个

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/div/label[1]')# 姓名
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/div/label[2]')# 拼音
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/div/label[3]')# 手机

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/div/label[4]')# 身份证
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/div/label[5]')# 护照
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/div/label[6]')# 台胞证
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/div/label[7]')# 港澳通行证

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/div/label[8]/input[1]')
        self.dr.sleep(1)
        self.dr.type('name->needPassengerInfoOther1','***')#其他1

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[20]/td/div/label[9]/input[1]')
        self.dr.sleep(1)
        self.dr.type('name->needPassengerInfoOther2','***')#其他2


        #时间限制
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[1]')#默认
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[21]/td/label[2]/input[1]')#提前
        self.dr.type('name->enterSightAdvanceDay')
        self.dr.sleep(1)
        self.dr.click('name->enterSightAdvanceHour')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="ADVANCE_BOOK_TIME"]/option[1]')
        self.dr.sleep(2)
        self.dr.click('name->enterSightAdvanceMinute')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="ADVANCE_BOOK_TIME"]/option[1]')
        self.dr.sleep(2)


        #出售时间 *
        #1(默认)
        #2
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[22]/td/label[2]/input[1]')
        #3
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[22]/td/label[3]')

        #短信模板 *
        self.dr.click('id->smsThemeId')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[23]/td/div/ul/li[1]')


        #验证消费日期
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[25]/td/label[1]/label')#默认
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[25]/td/label[2]/label')#有效期
        self.dr.click('id->consumeStartDate')#起始
        self.dr.sleep(2)
        #TODO
        self.dr.click('id->consumeEndDate')#截止
        self.dr.sleep(2)
        #TODO
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[25]/td/label[3]/label')#游客
        self.dr.sleep(1)
        self.dr.click('name->beforeDay')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[25]/td/label[3]/select[1]/option[2]')
        self.dr.sleep(2)
        self.dr.click('name->afterDay')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[25]/td/label[3]/select[2]/option[2]')
        self.dr.sleep(2)


        #价格库存 *
        #TODO

        #商品调价
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[27]/td/label[1]')#是（默认）
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[27]/td/label[2]')#否

        #退款设置
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[29]/td/label[1]/input[1]')#可以退款 （默认）
        self.dr.click('name->partRefund')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[29]/td/label[1]/select[1]/option[1]')#默认
        self.dr.click('name->refundChargeType')
        self.dr.sleep(2)
        self.dr.click('xpath->//*[@id="refundChargeType"]/option[1]')#默认
        self.dr.type('id->refundCharge')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[29]/td/label[2]')#不可退款

        #退款审核
        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[1]')#需要

        self.dr.click('xpath->//*[@id="refundAudit"]/td/label[2]')#不需要（默认）

        #退款说明 *
        self.dr.type('name->refundInfo','***')

        #费用包含
        #交通
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[1]/td[2]/label[1]')#默认 景区内用车免费

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[1]/td[2]/label[2]/label')#自定义
        self.dr.sleep(1)
        self.dr.type('name->feeInclude_traffic_text','***')

        #住宿
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[2]/td[2]/label[1]')#默认 无信息

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[2]/td[2]/label[2]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[2]/td[2]/label[3]/label')
        self.dr.sleep(1)
        self.dr.type('name->feeInclude_room_text','***')

        #用餐
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[3]/td[2]/label[1]')#默认

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[3]/td[2]/label[2]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[3]/td[2]/label[3]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[3]/td[2]/label[4]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[3]/td[2]/label[5]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[3]/td[2]/label[6]/label')
        self.dr.sleep(1)
        self.dr.type('name->feeInclude_dining_text','***')

        #门票
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[4]/td[2]/label[1]')#默认
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[4]/td[2]/label[2]')
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[4]/td[2]/label[3]/label')
        self.dr.sleep(1)
        self.dr.type('name->feeInclude_ticket_text','***')

        #导游服务
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[5]/td[2]/label[1]')#默认

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[5]/td[2]/label[2]/label')
        self.dr.sleep(1)
        self.dr.type('name->feeInclude_guide_text1','***')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[5]/td[2]/label[3]/label')
        self.dr.sleep(1)
        self.dr.type('name->feeInclude_guide_text2','***')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[5]/td[2]/label[4]/label')
        self.dr.sleep(1)
        self.dr.type('name->feeInclude_guide_text3','***')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[5]/td[2]/label[5]/label')
        self.dr.sleep(1)
        self.dr.type('name->feeInclude_guide_text','***')

        #保险
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[6]/td[2]/label[1]')#默认

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[6]/td[2]/label[2]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[6]/td[2]/label[3]/label')
        self.dr.sleep(2)
        self.dr.type('xpath->feeInclude_safest_text','***')

        #儿童价说明
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/label[2]/label')
        self.dr.click('name->childage_pro0')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/select[1]/option[1]')
        self.dr.sleep(1)
        self.dr.click('name->childage_pro1')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/select[2]/option[1]')
        self.dr.sleep(1)
        self.dr.click('name->childage_pro2')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/select[3]/option[1]')
        self.dr.sleep(1)
        self.dr.click('name->childage_pro3')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/select[4]/option[1]')
        self.dr.sleep(1)
        self.dr.click('name->childage_pro4')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/select[5]/option[1]')
        self.dr.sleep(1)
        self.dr.click('name->childage_pro5')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/select[6]/option[1]')
        self.dr.sleep(1)
        self.dr.click('name->childage_pro6')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/select[7]/option[1]')
        self.dr.sleep(1)
        self.dr.click('name->childage_pro7')
        self.dr.sleep(1)
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/select[8]/option[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/label[3]/label')
        #TODO

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[33]/td/table/tbody/tr[7]/td[2]/label[4]/label')
        self.dr.type('name->feeInclude_child_text','***')


        #其他
        self.dr.type('name->feeInclude_other','***')

        #费用不含
        #不可抗力
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[1]/td[2]/label[1]/label')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[1]/td[2]/label[2]/label')
        self.dr.type('name->feeExclude_majeure_text')

        #单房差
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[2]/td[2]/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[2]/td[2]/label[2]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[2]/td[2]/label[3]/label')
        self.dr.type('name->feeExclude_differ_text','***')

        #交通
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[3]/td[2]/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[3]/td[2]/label[2]/label')
        self.dr.type('name->feeExclude_traffic_text','***')

        #门票
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[4]/td[2]/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[4]/td[2]/label[2]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[4]/td[2]/label[3]/label')
        self.dr.type('name->feeExclude_ticket_text','***')

        #补充
        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[5]/td[2]/label[1]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[5]/td[2]/label[2]')

        self.dr.click('xpath->//*[@id="inputForm"]/table[1]/tbody/tr[34]/td/table/tbody/tr[5]/td[2]/label[3]/label')
        self.dr.type('name->feeExclude_additional_text','***')

        #活动项目
        self.dr.type('name->feeExclude_activity','***')

        #其他
        self.dr.type('name->feeExclude_other','***')

        #使用说明 *
        self.dr.type('name->reminde','***')

        #保存
        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[1]')

        #返回
        self.dr.click('xpath->//*[@id="inputForm"]/table[2]/tbody/tr/td/input[2]')



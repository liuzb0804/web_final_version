#coding=utf-8
from public.common import pyselenium
from public.common import basepage
from public.common import data_test
import time,os


class IndexPage(basepage.Page):

    def into_page(self,url):
        """打开首页"""
        self.dr.open(url)

    def input_username_key(self,values):
        """输入关键词"""
        self.dr.clear_type('id->username',values)

    def input_password_key(self,values):
        """输入关键词"""
        self.dr.clear_type('id->password',values)

    def input_code_key(self,values):
        self.dr.clear_type('id->captcha',values)

    def click_button(self):
        """点击按钮"""
        self.dr.click('id->submit')

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()


    def project_number(self,project):
        """选择（一级目录）"""
        # project = u'资源管理'
        for i in range(7):
            xpath = 'xpath->//*[@id="itemUl"]/li[' + str(i) + ']'
            xpath_text = 'xpath->//*[@id="itemUl"]/li[' + str(i) + ']/a/p'
            try:
                text = self.dr.get_text(xpath_text)
                # pyselenium.PySelenium.my_print(text)
                if text == project:
                    self.dr.click(xpath)
                    break
            except:
                pass


    def type_number(self,type):
        """选择（二级目录）"""
        # type = u'景区'
        for i in range(10):
            xpath = 'xpath->//*[@id="js_nav"]/ul/li[' + str(i) + ']'
            xpath_text = 'xpath->//*[@id="js_nav"]/ul/li[' + str(i) + ']/a/span'
            try:
                name = self.dr.get_text(xpath_text)
                # print name
                if name == type:
                    self.dr.click(xpath)
            except:
                pass


    def actions_type_add_all(self,id,number):
        """actions:添加"""
        re_data = data_test.data[id][number]
        for key,value in re_data.items():
            if key in data_test.list_data:
                # print "list:", key
                # xpath_value = re_data['景区']['one_page'][key]
                xpath_key = 'id->' + key
                xpath = 'xpath->//*[@id ="' + key + '"]/ul/li[' + value + ']'
                self.dr.click(xpath_key)
                time.sleep(3)
                self.dr.click(xpath)
                time.sleep(3)

            elif key in data_test.list_data_span:
                xpath_key = 'id->' + key
                xpath = 'xpath->//*[@id ="' + key + '"]/span/div/ul/li[' + value + ']'
                self.dr.click(xpath_key)
                time.sleep(3)
                self.dr.click(xpath)
                time.sleep(3)

            elif key in data_test.sep_list:
                # print "sep_list:",key
                # xpath = '//*[@id=' + key + ']/select[' + value[0] + ']'
                self.dr.click('xpath->//*[@id="regionErrorPopups"]/select[2]')
                time.sleep(3)
                self.dr.click('xpath->//*[@id="regionErrorPopups"]/select[2]/option[2]')
                time.sleep(3)
                self.dr.click('xpath->//*[@id="regionErrorPopups"]/select[3]')
                time.sleep(3)
                self.dr.click('xpath->//*[@id="regionErrorPopups"]/select[3]/option[2]')
                time.sleep(3)

            elif key in data_test.shangchuan_data:
                # print 'shangchuan:',key
                xpath_key = 'id->' + key
                time.sleep(2)
                self.dr.click(xpath_key)
                time.sleep(2)
                os.system(value)
                time.sleep(3)

            elif key in data_test.riqi:
                # print "riqi:",key
                xpath_key = 'id->' + key
                self.dr.type(xpath_key,value)  # '%Y-%M-%D'
                # riqi = self.dr.get_element(xpath_key)
                # riqi.send_keys(value)
                time.sleep(2)

            elif key in data_test.sele_data:
                # print "sele:",key
                xpath = 'xpath->//*[@id ="' + key + '"]/p[' + value + ']'
                self.dr.click(xpath)
                time.sleep(2)

            elif key in data_test.dingwei_data:
                # print "dingwei：",key
                xpath_key= 'id->'+key
                self.dr.click(xpath_key)
                time.sleep(3)
                self.dr.click('xpath->/html/body/div[3]/div[2]/div[1]/a')
                time.sleep(3)

            else:
                # print "input:",key
                xpath_key='name->'+key
                # self.dr.type(xpath_key,value)
                name = self.dr.get_element(xpath_key)
                name.send_keys(value)
                time.sleep(1)

        if id =='daoyou':
            xpath = 'id->'+data_test.daoyou[int(number)-1]
            self.dr.click(xpath)
        else:
            xpath = 'id->'+data_test.button[int(number)-1]
            self.dr.click(xpath)


    #TODO
    def actions_type_add_required(self,id):
        """操作：只添加必填项"""
        re_data = data_test.data[id]['Required']
        for key,value in re_data.items():
            pass

    # TODO error  long time
    def actions_type(self,select,action):
        """"""
        # select = 1      #第一个选项
        # action = 1      #第一个动作  看当前选项存在几个动作。默认顺序：查看，编辑，审核，删除

        actions = ['查看','编辑','审核','删除']
        for i in range(1,11):
            xpath = 'xpath->//*[@id="listTable"]/tbody/tr[' + str(select) + ']/td[' + str(i) + ']/div/a[' + str(action) + ']'
            try:
                # text = driver.find_element_by_xpath(xpath).text
                # print i,text
                text = self.dr.get_text(xpath)
                if text in actions:
                    self.dr.click(xpath)
                    time.sleep(2)
            except:print ('NO ACTION ` PLZ CHECK')

        # for i in range(1,11):
        #     xpath = 'xpath->//*[@id="listTable"]/tbody/tr[' + str(select) + ']/td[' + str(i) + ']/div/a[' + str(action) + ']'
        #     try:
        #         text = self.dr.get_text(xpath)
        #         #TODO
        #         #
        #     except:'no action'


    # def actions_type_dele(self,number):#删除
    #     pass
    # def actions_type_edi(self,number):#编辑
    #     pass
    # def actions_type_look(self,numebr):#查看
    #     pass
    # def actions_type_examine(self,number):#审核
    #     pass


    def data_number(self):
        """ 页面条数显示"""
        text = self.dr.get_text('xpath->//*[@id="listForm"]/div/div/div[2]/span')
        text_encode = text.encode('utf-8')
        A = text_encode.split('，')[2]
        B = '合计'
        C = A.replace(B,'')
        D = '条'
        E = C.replace(D,'')
        # total = int(E)/10 + int(E)%10
        total = int(E)
        return total


    #TODO
    def display_number(self,select):
        """切换页面显示数"""
        xpath = 'xpath->//*[@id="page-select"]/ul/li[' + str(select) + ']'
        self.dr.click('id->page-select')
        time.sleep(2)
        self.dr.click(xpath)


    #TODO
    def jump_page(self,number):
        """跳页"""
        # text = self.dr.get_element('xpath->//*[@id="listForm"]/div/div/div[2]/div/div[1]/input')
        # text.send_key(number)
        self.dr.type('xpath->//*[@id="listForm"]/div/div/div[2]/div/div[1]/input',number)
        time.sleep(1)
        self.dr.click('xpath->//*[@id="listForm"]/div/div/div[2]/div/div[1]/input')
        time.sleep(3)
        text = self.dr.get_text('xpath->//*[@id="showPage"]')
        return text

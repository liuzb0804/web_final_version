#coding=utf-8

import codecs
import os
import xlrd
from config import globalparam

data_path = globalparam.data_path
def get_xls_to_dict(xlsname, sheetname):
	"""
	读取excel表结果为dict
	第一行为字典的key，下面的为值
	return [{'title':'1','user':'root'},{'title':'2','user':'xiaoshitou'}]
	"""
	# dataresult = []
	# result = []
	datapath = os.path.join(data_path,xlsname)
	xls1 = xlrd.open_workbook(datapath)
	table = xls1.sheet_by_name(sheetname)
	# for i in range(0,table.nrows):
	# 	dataresult.append(table.row_values(i))
	dataresult = [table.row_values(i) for i in range(0, table.nrows)]
	#将list转化成dict
	# for i in range(1,len(dataresult)):
	# 	temp = dict(zip(dataresult[0],dataresult[i]))
	# 	result.append(temp)

	result = [ dict(zip(dataresult[0], dataresult[i])) for i in range(1, len(dataresult))]
	return result

def get_url_data(title):
	"""
	读取txt文件，转化成dict;读取url和导航栏的对应关系
	将txt转化成一个字典:
	"""
	name = 'urlsource.txt'
	txtpath = os.path.join(data_path,name)
	with codecs.open(txtpath,'r',encoding='utf-8') as f:
		txtcontent = f.readlines()
	txtdict = dict([txt.strip().replace('\ufeff','').split('=>') for txt in txtcontent])
	return txtdict[title]

def get_xls_to_list(excelname, sheetname):
	"""
	读取excel表，返回一个list,只是返回第一列的值
	return [1,2,3,4,5]
	"""
	datapath = os.path.join(data_path, excelname)
	excel = xlrd.open_workbook(datapath)
	table = excel.sheet_by_name(sheetname)
	result = [table.row_values(i)[0].strip() for i in range(1,table.nrows)]
	return result

def get_excel_data(excelname,sheetname,col):
	"""
	选择某一列提取
	:param excelname:
	:param sheetname:
	:param col:
	:return: datalist
	"""
	datapath = os.path.join(data_path,excelname)
	xls1 = xlrd.open_workbook(datapath)
	table = xls1.sheet_by_name(sheetname)
	cols = table.col_values(col)  # 第col列
	datalist = []
	for data in cols:
		# datavalue = data.encode('utf-8')
		if type(data) ==float:
			datavalue = int(data)
			datalist.append(datavalue)
		else:
			datalist.append(data)
	return datalist

def get_excel_for_id_to_case(excelname,sheetname,id):
	"""
	根据用例ID找到用例所有信息,某一行数据
	:param excelname:
	:param sheetname:
	:param id:
	:return: row
	"""
	datapath = os.path.join(data_path,excelname)
	xls1 = xlrd.open_workbook(datapath)
	table = xls1.sheet_by_name(sheetname)
	rows = table.nrows  #行数
	# datalist = []
	for i in range(0,rows):
		row = table.row_values(i)
		# datalist.append(row)
		if id in row:
			return row

# if __name__=='__main__':
# 	res = get_xls_to_list('addressParse.xlsx','Sheet1')
# 	res = get_xls_to_dict('admin_single_order.xlsx','ordermsg')
# 	print(res)



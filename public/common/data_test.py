#coding=utf-8
import time,os
from faker import Factory
fake = Factory.create("zh_CN")

data = {
    u'景区':{
        "Required":{
            "name":"",
            "parentDict":"2",
            "regionErrorPopups":['2','3']
        },
        "1":{
            "name":u'景区',        #景区名称                            *
            "parentDict": "2",      #景区等级（列表）                      *
            "regionErrorPopups": ['2', '3'],        #所属地区（列表）       *
            "shortName":"",     #中文简称
            "pinyinName":"JQMC",        #拼音名称
            "englishName": "EnglishName",       #英文名称
            "serviceTypeDict":"2",      #服务类型（列表）
            "address": fake.address(),      #景区地址
            "locate": "经纬度（定位）",        #经纬度（定位）
            "creditCode":"123456789",       #统一社会信用代码
            "permitNumber": "987654321",        #许可证号
            "registrationTypeDict": "2",        #企业等级注册类型（列表）
            "industryCode": "123123",       #行业代码
            "contacts": fake.name(),        #联系人
            "phone":fake.phone_number(),        #联系电话
            "organizationCode":"123456",        #组织机构代码
            "status":"2"        #状态（选择）
        },
        "2":{
            "areas": "8898",        #景区面积
            "price": "198",     #门票价格
            "openTime": fake.am_pm(),       #开放时间
            "capacity": "",     #景区最大承载量
            "managementAgency": "",     #管理机构
            "assessmentTime": fake.date(pattern="%Y-%m-%d"),        #评定年月（日期）
            "honoraryTitle": "",        #荣誉称号
            "recommendedTime": fake.month(),        #建议游玩时间
            "fitCrowd": "",     #适合人群
            "parkingSpaces": "198",     #车位
            "consumptionAvg":"198",     #人均消费
            "keywords":"key",       #关键字
            "logFlow":"",       #日志流程
            "tourTime":fake.am_pm(),        #游览时间
            "manager":fake.name(),      #景区管理人员
            "openningHours":fake.date(pattern="%Y-%m-%d"),      #开业时间（日期）
            "holdingSituation":"2",     #控股情况（列表）
            "investmentEntity":"",      #投资主体
            "accountCategoryDict":"2",      #执行会计制度类别（列表）
            "altitude": "889",      #海拔高度
            "setPoint": "2",        #是否设定（选择）
            "travelAgency": "yes",      #上报旅行社
            "introduction": "",     #景区简介
            "recommendedRoute": "",     #推荐旅游路线
            "surroundingInfo": "",      #周边信息
            "serviceFacilities": "",        #服务设施
            "infrastructure": "",       #基础设施
            "travelInfo": "",       #交通信息
            "tourismProject": "",       #旅游项目
            "attractoins": "",      #景点
            "squarePicker": "D:\\WinClick1.exe" ,       #景区图片（上传）
            "logoPicker": "D:\\WinClick1.exe"       #LOGO（上传）
        },
        "3":{
            "principle": fake.name(),       #负责人姓名
            "principleNumber": fake.phone_number(),     #负责人电话
            "email": fake.email(),      #电子邮箱
            "postalCode": "youzhenbianma",      #有争辩
            "fax": "chuanzhen",     #传真
            "rescuePhone": fake.phone_number(),     #救援电话
            "complaintPhone": fake.phone_number(),      #投诉电话
            "emergencyContact": "",     #紧急联系人
            "emergencyPhone": "",       #紧急联系电话
            "supportHotLine": "",       #游客咨询电话
        },
        "4":{
            "url": "",      #网址
            "microUrl": "",     #微网址
            "downloadUrlApple": "",     #苹果版APP地址
            "downloadUrlAndroid": "",       #安卓版APP地址
            "tencentWeibo": "",     #腾讯微博
            "financialNetwork": "",     #金融网点
            "sinaWeibo": "",        #新浪微博
            "wechatPublic": "",     #微信公众号
            "qcCodeApplePicker": "D:\\WinClick1.exe",       #苹果APP二维码
            "qrCodeAndroidPicker": "D:\\WinClick2.exe",     #安卓APP二维码
            "wechatQrCodePicker": "D:\\WinClick3.exe" ,      #微信二维码
        }
    },#景区：627
    u'酒店':{
        "Required":{
            "name":"酒店名称",
            "levelDict":"酒店等级（列表）",
            "regionErrorPopups":"所属地区（列表）"
        },
        "1":{
            "name": "酒店名称",#*
            "levelDict": "酒店等级（列表）",#*
            "regionErrorPopups": "所属地区（列表）",#*
            "shortName":"中文简称",
            "pinyinName": "拼音名称",
            "englishName": "英文名称",
            "address": "酒店地址",
            "locate": "经纬度（定位）",
            "creditCode": "统一社会信用代码",
            "permitNumber": "许可证号",
            "legalRepresent": "法人代表",
            "registrationTypeDict": "企业等级注册类型（列表）",
            "contacts": "联系人",
            "phone": "联系电话",
            "organizationCode": "组织机构代码",
            "status": "状态（选择）",
        },
        "2":{
            "regDate": "工商等级注册时间（日期）",
            "startRateTime": "星级评定时间（日期）",
            "totalBeds": "总床位数",
            "totalRooms": "总客房数",
            "roomType": "房间类型",
            "dishesDict": "主要菜系（列表）",
            "smBanNumber": "小宴会包间数",
            "manageModel": "饭店管理模式",
            "arcStyle": "建筑风格",
            "slogan": "宣传语",
            "lastDecorateTime": "最后一次装修时间（日期）",
            "totalStaff": "员工总数",
            "parkingSpaces": "车位",
            "seatsNumber": "餐厅座位数",
            "totalInvestment": "投资总额",
            "keywords": "关键字",
            "signageNumber": "标牌编号",
            "checkInTime": "最早入住时间",
            "departureTime": "最晚离店时间",
            "openningHours": "开业时间（日期）",
            "travelAgency": "上报旅行社",
            "setPoint": "是否设点（选择）",
            "introduction": "酒店简介",
            "confFacilities": "会议设施",
            "surroundingInfo": "周边信息",
            "foodFacilities": "餐饮设施",
            "recrFacilities": "娱乐设施",
            "travelInfo": "交通信息",
            "busiFacilities": "商务设施",
            "squarePicker": "酒店图片（上传）",
        },
        "3":{
            "bookPhone": "预订电话",
            "fixedPhone": "固定电话",
            "email": "电子邮箱",
            "postalCode": "邮政编码",
            "emergencyContact": "紧急联系人",
            "emergencyPhone": "紧急联系电话",
            "fax": "传真",
        },
        "4":{
            "officialWebsite": "官方网站",
            "wechatPublic": "微信公众号",
            "tencentWeibo": "腾讯微博",
            "sinaWeibo": "新浪微博",
            "downloadUrlApple": "苹果版APP地址",
            "downloadUrlAndroid": "安卓版APP地址",
            "qcCodeApplePicker": "苹果APP二维码（上传）",
            "qrCodeAndroidPicker": "安卓APP二维码（上传）",
            "wechatQrCodePicker": "微信二维码（上传）",
        }
    },#酒店：861
    u'导游':{
        "Required":{
            "name":"导游姓名",
            "certificateNo":"导游证号",
            "levelDict":"导游等级（列表）",
            "regionErrorPopups":"所属地区（列表）"
        },
        "1":{
            "name": "导游姓名",#*
            "certificateNo": "导游证号",#*
            "levelDict": "导游等级（列表）",#*
            "regionErrorPopups": "所属地区（列表）",#*
            "pinyinName":"拼音名称",
            "phoneNumber":"手机号码",
            "icCardNo": "导游IC卡号",
            "cardNo": "导游卡号",
            "idNo": "身份证号",
            "genderDict": "性别（列表）",
            "languages": "语言",
            "ethnicDict": "民族（列表）",
            "educationDict": "学历（列表）",
            "status": "状态（选择）",
        },
        "2":{
            "birthDate": "出生日期（日期）",
            "placeOfBirth": "出生地",
            "address": "地址",
            "homeAddress": "家庭住址",
            "hkMcPassNo": "港澳通行证号",
            "hkTwPassNo": "港台通行证号",
            "blogAddress": "博客地址",
            "age": "年龄",
            "passportNo": "护照号",
            "passportValidDate": "护照有效日期（日期）",
            "passportIssuingPlace":"护照签发地",
            "personalSituation":"个人情况",
            "favorite":"个人爱好"
        },
        "3":{
            "checkDate": "检查日期（日期）",
            "issueDate": "发卡日期（日期）",
            "auditDate": "年审日期（日期）",
            "gradeNo": "等级证号",
            "qualificationNoIssueDate": "资格证号发证日期",
            "qualificationNo": "资格证号",
            "workNature": "工作性质",
            "checkCardNo": "检查卡号",
            "checkCertNo": "检查证号",
            "inspectorName": "检查员姓名",
            "checkTimeDate": "检查时间（日期）",
            "checkResult": "检查结果",
            "outsideRecognition": "外阜识别",
            "issuingAuthority": "导游发证机关",
            "totalScore": "总分值",
            "detainedScore": "被扣分值",
            "guideStartDate": "从事导游起始日期（日期）",
            "position": "职位",
            "serviceStartDate": "服务开始日期（日期）",
            "serviceEndDate": "服务结束日期（日期）",
            "guideCertIssueDate": "导游证发证日期（日期）",
            "guideCertExpDate": "导游证到期日期（日期）",
            "guideTypeDict": "导游类型（列表）",
            "affiliationTypeDict": "挂靠单位类型（列表）",
            "affiliationName": "挂靠单位名称",
            "startWorkTimeDate": "参加工作时间（日期）",
            "affiliatedCompanies": "所属公司",
            "contactNumber": "联系电话",
            "guideCardScore": "导游卡分值",
            "yearCheckDate": "年检日期（日期）",
            "leaderCard": "有无领队证（选择）",
            "setPoint": "是否设点（选择）",
            "serviceUnits": "服务单位",
            "trainingSituation": "培训情况",
            "preRewarded": "以往被奖励情况",
            "pastComplaints": "以往被投诉情况",
            "groupInfo": "出团信息",
            "leaderInfo": "领队信息",
            "selfIntroduction": "个人介绍",
            "travelAgency": "上报旅行社",
            "picturePicker": "导游照片（上传）"
        },
    },#导游：1083
    u'旅行社':{
        "Required":{
            "name":"旅行社名称",
            "typeDict":"旅行社类型（列表）",
            "regionErrorPopups":"所属地区（列表）",
            "allowBusiness":"许可经营业务（选择）"
        },
        "1":{
            "name": "旅行社名称",#*
            "typeDict": "旅行社类型（列表）",#*
            "regionErrorPopups": "所属地区（列表）",#*
            "allowBusiness": "许可经营业务（选择）",#*
            "shortName": "中文简称",
            "pinyinName": "拼音名称",
            "englishName": "英文名称",
            "levelDict": "旅行社等级（列表）",
            "address": "旅行社地址",
            "locate": "经纬度（定位）",
            "creditCode": "统一社会信用代码",
            "permitNumber": "许可证号",
            "legalRepresent": "法人代表",
            "registrationTypeDict": "企业等级注册类型（列表）",
            "industryCode": "行业代码",
            "organizationCode": "组织机构代码",
            "contacts": "联系人",
            "phone": "联系电话",
            "location": "旅行社经营场所",
            "status": "状态（选择）",

        },
        "2":{
            "businessTypeDict": "经营业务（列表）",
            "mailingAddressCh": "通讯地址（中文）",
            "mailingAddressEn": "通讯地址（英文）",
            "travelDict": "总社/分社（列表）",
            "approvalNumber": "批准文号",
            "keywords": "关键字",
            "paymentMethod": "支付方式",
            "guaranteePayment": "质保金缴纳情况",
            "insuranceCoverage": "责任险投保情况",
            "registrationCode": "等级证号",
            "regCapital": "注册资本",
            "issueDate": "证发日期（日期）",
            "scale": "旅行社规模",
            "regAddressCh": "注册地址（中文）",
            "regAddressEn": "注册地址（英文）",
            "sealName": "盖章名称",
            "setUpName": "设立社名称",
            "representCertTypeDict": "法人代表证件类型（列表）",
            "representCertNo": "法人代表证件号",
            "guaranteeAccountName": "质保金开户行名称",
            "qualityGuarantee": "质量保证金",
            "investors": "投资人",
            "businessStatus": "业务状态（选择）",
            "agencyMember": "旅行社协会会员（选择）",
            "introduction": "简介",
            "serviceLanguage": "服务语种",
            "surroundingInfo": "周边信息",
            "mainLine": "主要线路",
            "productInfo": "旅游产品信息",
            "personnelInfo": "人事信息",
            "financialInfo": "财务信息",
            "recordRegCert": "备案登记证明",
            "squarePicker": "图片（营业执照）（上传）",
            "stampPicker": "盖章图片（上传）",
            "logoPicker": "LOGO（上传）",
        },
        "3":{
            "officePhone": "办公电话",
            "fixedPhone": "固定电话",
            "email": "电子邮箱",
            "postalCode": "邮政编码",
            "principle": "单位负责人",
            "principleNumber": "单位负责人电话",
            "principalIdNo": "负责人身份证号",
            "complaintPhone": "投诉电话",
            "emergencyContact": "紧急联系人",
            "emergencyPhone": "紧急联系电话",
            "fax": "传真",
        },
        "4":{
            "officialWebsite": "官方网站",
            "site": "网址",
            "tencentWeibo": "腾讯微博",
            "sinaWeibo": "新浪微博",
            "wechatPublic": "微信公众号",
            "wechatQrCodePicker": "微信二维码（上传）",
        }
    },#旅行社：909
    u'娱乐场所':{
        "Required":{
            "name":"娱乐场所名称",
            "parentDict":"娱乐场所类型（列表）",
            "regionErrorPopups":"所属地区（列表）"
        },
        "1":{
            "name": "娱乐场所名称",#*
            "parentDict": "娱乐场所类型（列表）",#*
            "regionErrorPopups": "所属地区（列表）",#*
            "shortName":"中文简称",
            "pinyinName":"拼音名称",
            "englishName": "英文名称",
            "organizationCode": "组织机构代码",
            "address": "娱乐场所地址",
            "locate": "经纬度（定位）",
            "contacts": "联系人",
            "phone": "联系电话",
            "status": "状态（选择）",
        },
        "2":{
            "businessHours": "营业时间",
            "keywords": "关键字",
            "consumptionAvg": "人均消费",
            "serviceTypeDict": "服务类型（列表）",
            "parkingSpaces": "车位",
            "introduction": "简介",
            "surroundingInfo": "周边信息",
            "detailIntroduction": "详细介绍",
            "serviceFacilities": "服务设施",
            "serviceProject": "服务项目",
            "logoPicker": "LOGO(上传)",
        },
        "3":{
            "email": "电子邮箱",
            "fax": "传真",
            "emergencyContact": "紧急联系人",
            "emergencyPhone": "紧急联系电话",
            "bookPhone": "预订电话",
        },
        "4":{
            "officialWebsite": "官方网站",
            "microUrl": "微网址",
            "appApple": "苹果版APP地址",
            "appAndroid": "安卓版APP地址",
            "tencentWeibo": "腾讯微博",
            "sinaWeibo": "新浪微博",
            "wechatPublic": "微信公众号",
            "qcCodeApplePicker": "苹果APP二维码（上传）",
            "qrCodeAndroidPicker": "安卓APP二维码（上传）",
            "wechatQrCodePicker": "微信二维码（上传）",
        }
    },#娱乐场所：1207
    u'餐饮场所':{
        "Required":{
            "name":"餐饮场所名称",
            "parentDict":"餐饮场所等级（列表）",
            "typeDict":"餐饮场所类型（列表）",
            "regionErrorPopups":"所属地区（列表）"
        },
        "1":{
            "name": "餐饮场所名称",#*
            "parentDict": "餐饮场所等级（列表）",#*
            "typeDict": "餐饮场所类型（列表）",#*
            "regionErrorPopups": "所属地区（列表）",#*
            "shortName": "中文简称",
            "pinyinName": "拼音名称",
            "englishName": "英文名称",
            "address": "餐饮场所地址",
            "locate": "经纬度（定位）",
            "contacts": "联系人",
            "phone": "联系电话",
            "permitNumber": "许可证号",
            "organizationCode": "组织机构代码",
            "status": "状态（选择）",
        },
        "2":{
            "gradeDict": "档次（列表）",
            "serviceTypeDict": "服务类型（列表）",
            "businessHours": "营业时间",
            "consumptionAvg": "人均消费",
            "mealsNumber": "同时就餐人数",
            "seatNumber": "餐位数量",
            "roomNumber": "包间数",
            "keywords": "关键字",
            "parkingSpaces": "车位",
            "introduction": "简介",
            "detailIntroduce": "详细介绍",
            "specialDishes": "特色菜品",
            "surroundingInfo": "周边信息",
            "logoPicker": "LOGO（上传）",
        },
        "3":{
            "email": "电子邮箱",
            "postalCode": "邮政编码",
            "fax": "传真",
            "complaintPhone": "投诉电话",
            "emergencyContact": "紧急联系人",
            "emergencyPhone": "紧急联系电话",
            "bookPhone": "预订电话",
        },
        "4":{
            "officialWebsite": "官方网站",
            "wapUrl": "WAP网址",
            "appApple": "苹果版APP地址",
            "appAndroid": "安卓版APP地址",
            "tencentWeibo": "腾讯微博",
            "sinaWeibo": "新浪微博",
            "wechatPublic": "微信公众号",
            "qcCodeApplePicker": "苹果APP二维码（上传）",
            "qrCodeAndroidPicker": "安卓APP二维码（上传）",
            "wechatQrCodePicker": "微信二维码（上传）",
        }
    },#餐饮场所：1713
    u'购物场所':{
        "Required":{
            "name":"购物场所名称",
            "typeDict":"购物场所类型（列表）",
            "regionErrorPopups":"所属地区（列表）",
            "address":"购物场所地址"
        },
        "1":{
            "name": "购物场所名称",#*
            "typeDict": "购物场所类型（列表）",#*
            "regionErrorPopups": "所属地区（列表）",#*
            "address": "购物场所地址",#*
            "shortName":"中文简称",
            "pinyinName":"拼音名称",
            "englishName": "英文名称",
            "organizationCode": "组织机构代码",
            "locate": "经纬度（定位）",
            "liceneseNo": "统一社会信用代码",
            "permitNumber": "许可证号",
            "contacts": "联系人",
            "phone": "联系电话",
            "status": "状态（选择）",
        },
        "2":{
            "parkingSpaces": "车位",
            "businessHours": "营业时间",
            "keywords": "关键字",
            "paymentMethod": "支付方式",
            "introduction": "简介",
            "detailIntroduce": "详细介绍",
            "surroundingInfo": "周边信息",
            "specialProduct": "特色商品",
            "logoPicker": "LOGO（上传）",
        },
        "3":{
            "email": "电子邮箱",
            "fax": "传真",
            "emergencyContact": "紧急联系人",
            "emergencyPhone": "紧急联系电话",
            "complaintPhone": "投诉电话",
        },
        "4":{
            "officialWebsite": "官方网站",
            "wapUrl": "WAP网址",
            "appApple": "苹果版APP地址",
            "appAndroid": "安卓版APP地址",
            "tencentWeibo": "腾讯微博",
            "sinaWeibo": "新浪微博",
            "wechatPublic": "微信公众号",
            "qcCodeApplePicker": "苹果APP二维码（上传）",
            "qrCodeAndroidPicker": "安卓APP二维码（上传）",
            "wechatQrCodePicker": "微信二维码（上传）",
        }
    },#购物场所：21
}

#下一步
button = ['basicBtn','introBtn','contactBtn','mediaBtn']    #依次为：第一页，第二页，第三页,第四页
daoyou = ['basicBtn','privateBtn','workBtn']    #导游

#类型
sep_list = ['regionErrorPopups']

list_data = ['parentDict','serviceTypeDict','holdingSituation','accountCategoryDict','levelDict',
             'dishesDict','genderDict','guideTypeDict','affiliationTypeDict','typeDict','representCertTypeDict',
             'parentDict','serviceTypeDict','gradeDict','serviceTypeDict']

list_data_span = ['registrationTypeDict','ethnicDict','educationDict','businessTypeDict','travelDict']

shangchuan_data = ['squarePicker','logoPicker','qcCodeApplePicker','qrCodeAndroidPicker','wechatQrCodePicker','picturePicker','stampPicker']

riqi = ['assessmentTime','openningHours','regDate','startRateTime','lastDecorateTime','openningHours','birthDate','passportValidDate',
        'checkDate','issueDate','auditDate','checkTimeDate','guideStartDate','serviceStartDate','serviceEndDate','guideCertIssueDate',
        'guideCertExpDate','startWorkTimeDate','yearCheckDate',]

sele_data = ['status','setPoint','leaderCard','allowBusiness','businessStatus','agencyMember']

dingwei_data = ['locate']


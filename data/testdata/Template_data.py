#coding=utf-8

from faker import Faker
from faker import Factory

fake = Factory.create("zh_CN")



Templata_data ={
    "旅游公共信息服务平台-基础资源": {
    "景区景点": {
        "name":"名称",    #   *
        "shortname":"简称",   # *
        "english":"英文名称",
        "impression":"印象",
        "regionSelector":"所属地区（下拉）",    #   *
        "mbBox9":"经纬度（弹窗）", #   *
        "tagsBox":"标签（选择）",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "individualityLogoBox":"个性标识（上传）",
        "logobigBox":"标识大图（上传）",
        "logosmallBox":"标识小图（上传）",
        "icname":"企业工商注册全称",
        "orgcode":"组织机构代码",
        "bizlicense":"营业执照号码",
        "licenseno":"许可证号",
        "legal":"法人代表",
        "manager":"经理",
        "phone":"电话",
        "rescuePhone":"救援电话",
        "complaintPhone":"投诉电话",
        "fax":"传真",
        "zipcode":"邮编",
        "address":"地址",
        "email":"E-mail",
        "site":"官方网站",
        "trafficInformation":"周边交通",
        "peripheralInformation":"周边信息",
        "mainLine":"主要线路",
        "summary":"景区简介",
        "iframe":"景区介绍",
        "iframe-1":"旅游活动",
        "iframe-2":"旅游购物",
        "iframe-3":"旅游美食",
        "jiedai":"总接待人数",
        "chewei":"总停车位数",
        "emergcontactor":"应急联系人",
        "emergphone":"应急联系电话",
        "chainstore":"连锁经营情况",
        "weibo":"微博地址",
        "videoBox":"宣传片（上传）",
        "audioBox":"语音介绍（上传）",
        "panoramaWebBox":"全景地址（web）（上传）",
        # "appPanoramaIdBox":"全景地址（App）（上传）",
        "monitorBox":"实景展播（上传）",
        "mapGuideNameBox":"导游导览（列表）",
        "opentime":"开放时间",
        "exponent":"推荐指数",
        "maxBearing":"景区最大承载量",
        "altitude":"海拔高度",
        "headUses":"人均消费",
        "onlineBooking":"在线购票",
        "ticketOrder":"门票预订（选择）",
        "ticketprice":"景区门票",
        "ticketType":"门票类型",
        "tourTime":"建议游玩时长",
        "tourMonth":"建议游玩月份",
        "advicedate":"最佳旅游季节",
        "scenicAdvice":"景区建议",
        "showSum":"查看数（只读）",
        "praiseNum":"点赞数（只读）",
        "sortno":"排序",  #有默认值   *
        "travelType":"玩法",
        "scenicTheme":"景区主题（选择）",
        "matterCrowd":"适合人群（选择）",
        "type":{
        "世界遗产":"",
        "风景名胜区":"",
        "森林公园":"",
        "旅游城镇":"",
        "对外开放是城市和地区":"",
        "历史文化名城":"",
        "文物保护单位":"",
        "乡村旅游区":"",
        "自然保护区":"",
        "湿地公园":"",
        "地质公园":"",
        "其他":""
      },
      "resourceLevel":"A级(选择)", #有默认值   *
      "recommend":"选择（多选）",
      "state":"状态（多选）"  #有默认值   *
    },
    "宾馆酒店": {
        "name":"名称",    #  *
        "shortname":"简称",   #  *
        "english":"英文名称",
        "mbBox9":"经纬度（弹窗）", #  *
        "regionSelector":"所属地区（下拉）",    #  *
        "impression":"印象",
        "tagsBox":"标签（选择）",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "individualityLogoBox":"个性标识（上传）",
        "logobigBox":"标识大图（上传）",
        "logosmallBox":"标识小图（上传）",
        "icname":"企业工商注册全称",
        "orgcode":"组织机构代码",
        "bizlicense":"营业执照号码",
        "licenseno":"许可证号",
        "legal":"法人代表",
        "manager":"经理",
        "phone":"电话",
        "emergphone":"应急联系电话",
        "park":"停车场",
        "weixinNumber":"微信公众号",
        "fax":"传真",
        "zipcode":"邮编",
        "address":"地址",
        "email":"E-Mail",
        "site":"官方网站",
        "zbxx":"周边信息",
        "summary":"简介",
        "iframe":"内容",
        "jiedai":"总接待人数",
        "chewei":"总停车位数",
        "emergcontactor":"应急联系人",
        "chainstore":"连锁经营情况",
        "hotelSetTime":"开业时间",
        "opentime":"开放时间",
        "lastRenovationTime":"新近装修时间",
        "earliest":"可办理入住时间",
        "latest":"退房时间",
        "exponent":"推荐指数",
        "showSum":"查看数（只读）",
        "praiseNum":"点赞数（只读）",
        "totalRoom":"总房间数",
        "roomtypes":"房型",
        "videoBox":"宣传片（上传）",
        "panoramaWebBox":"全景地址（web）（上传）",
        "panoramaAppBox":"全景地址（App）（上传）",
        "weibo":"微博地址",
        "price":"人均消费",
        "dining":"餐饮设施",
        "cheap":"在线购票",
        "hotelFloor":"酒店楼高",
        "sortno":"排序",  #有默认值   *
        "hotelBrand":"酒店品牌（选择）",
        "hotelTheme":"酒店主题（选择）",
        "suportCard":"支持卡类（选择）",
        "ticketOrder":"门票预订（选择）",
        "specialService":"特殊服务（选择）",
        "servicesItem":"服务项目(选择)",
        "cateringServices":"餐饮服务（选择）",
        "recreation":"休闲娱乐(选择)",
        "roomFacilities":"房间设施（选择）",
        "trafficServer":"交通服务（选择）",
        "receptionServer":"前台服务（选择）",
        "serverInclude":"服务包含（选择）",
        "network":"网络（选择）",
        "grade":"宾馆酒店类型（选择）",
        "resourceLevel":"级别（选择）",   #有默认值：1  *
        "cuisine":"提供主要菜系（选择）",
        "recommend":"选择（选择）",
        "state":"状态（选择）"    #有默认值：1  *
    },
    "旅行社": {
        "name": "name",     #  *
        "phone": "电话",
        "region":"所属地区（列表）",    #  *
        "mbBox9":"经纬度（弹窗）", #  *
        "zipcode":"邮编",
        "email":"E-Mail",
        "emergcontactor":"应急联系人",
        "emergphone":"应急联系电话",
        "orgcode":"组织机构代码",
        "fax":"传真",
        "address":"地址",
        "site":"网址",
        "bizlicense":"营业执照号码",
        "icname":"企业工商注册全称",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "logobigUploadBox":"企业标识大图（上传）",
        "logosmallUploadBox":"企业标识小图（上传）",
        "videoBox": "宣传片（上传）",
        "chewei":"车位",
        "exponent":"推荐指数",
        "headconsumer":"人均消费",
        "impression":"印象",
        "individualityLogo":"企业个性标识",
        "investor":"旅行社投资人",
        "jiedai":"接待人数",
        "legal":"法人代表",
        "licenseno":"许可证号",
        "chainstore":"连锁经营情况",
        "manager":"经营负责人",
        "managerphone":"经营负责人电话",
        "opentime":"开放时间",
        "showSum":"查看数（只读）",
        "praiseNum":"点赞数（只读）",
        "registeredoffice":"旅行社注册地址",
        "telephonecomplaIntegers":"旅行社投诉电话",
        "tourismzone":"所在旅游区",
        "weibo":"微博地址",

        "tag":"标签（选择）",
        "summary":"内容",
        "mainLine":"主要线路",
        "digest":"摘要",
        "iframe":"经营业务",
        "enterpriseType":"企业单位类别（选择）",
        "resourceLevel":"旅行社类型（选择）",
        "translations":"可提供翻译语种（选择）",
        "recommend":"选择（选择）",
        "state":"状态（选择）"    #有默认值：1  *
    },
    "餐饮场所": {
        "name": "name", #  *
        "shortname": "缩略名称",    #  *
        "region":"所属地区（下拉）",    #  *
        "mbBox9":"经纬度（弹窗）", #  *
        "zipcode":"邮编",
        "email":"E-Mail",
        "emergcontactor":"应急联系人",
        "consume":"人均消费",
        "openinghours":"开放时间",
        "phone":"电话",
        "orgcode":"组织机构代码",
        "fax":"传真",
        "address":"地址",
        "site":"网址",
        "emergphone":"应急联系电话",
        "weibo":"微博地址",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "individualityLogoBox":"企业个性标识(上传)",
        "logobigBox":"企业标识大图（上传）",
        "logosmallBox":"企业标识小图（上传）",
        "manager":"经营负责人",
        "bizlicense":"营业执照号码",
        "chainstore":"连锁经营情况",
        "exponent":"推荐指数",
        "icname":"企业工商注册全称",
        "impression":"印象",
        "sortno":"排序",
        "moreSite":"微网址",
        "optenTime":"开业时间",
        "legal":"法人代表",
        "jiedai":"接待人数",
        "licenseno":"许可证号",
        "videoBox":"宣传片（上传）",
        "tag":"标签（选择）",
        "summary":"简介",
        "iframe":"介绍",
        "foodSelectBox":"关联美食（上传）",
        "grade":"餐饮场所类型（选择）",
        "resourceLevel":"等级（选择）",
        "cuisine":"提供主要菜系（选择）",
        "recommend":"选择（选择）",
        "state":"状态（选择）"
    },
    "娱乐场所": {
        "name": "名称", #  *
        "shortname": "缩略名称",
        "english":"英文名称",
        "mbBox9":"经纬度（弹窗）",     #  *
        "region":"所属地区（下拉）",    #  *
        "impression":"印象",
        "tag":"标签（选择）",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "individualityLogoBox":"个性标识（上传）",
        "logobigBox":"标识大图(上传)",
        "logosmallBox":"标识小图（上传）",
        "icname":"企业工商注册全称",
        "orgcode":"组织机构代码",
        "bizlicense":"营业执照号码",
        "licenseno":"许可证号",
        "legal":"法人代表",
        "manager":"经理",
        "phone":"电话",
        "fax":"传真",
        "zipcode":"邮编",
        "address":"地址",
        "email":"E-Mail",
        "site":"网址",
        "summary":"简介",
        "iframe":"内容",
        "jiedai":"总接待人数",
        "chewei":"总停车位数",
        "emergcontactor":"应急联系人",
        "emergphone":"应急联系电话",
        "chainstore":"连锁经营情况",
        "weibo":"微博地址",
        "videoBox":"宣传片（上传）",
        "opentime":"开放时间",
        "exponent":"推荐指数",
        "headUses":" 人均消费",
        "showSum":"查看数(只读)",
        "praiseNum":"点赞数（只读）",
        "sortno":"排序",  #有默认值  *
        "resourceLevel":"娱乐场所类型(选择)",   #有默认值：1  *
        "recommend":"选择（选择）",
        "state":"状态（选择）"    #有默认值：1  *
    },
    "购物场所": {
        "name": "名称", #  *
        "shortname": "缩略名称",
        "english":"英文名称",
        "mbBox9":"经纬度（弹窗）",   #  *
        "region":"所属地区（下拉）",  #  *
        "impression":"印象",
        "tag":"标签（选择）",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "individualityLogoBox":"个性标识（上传）",
        "logobigBox":"标识大图（上传）",
        "logosmallBox":"标识小图(上传)",
        "icname":"企业工商注册全称",
        "orgcode":"组织机构代码",
        "bizlicense":"营业执照号码",
        "licenseno":"许可证号",
        "legal":"法人代表",
        "manager":"经理",
        "phone":"电话",
        "fax":"传真",
        "zipcode":"邮编",
        "address":"地址",
        "email":"E-Mail",
        "site":"网站",
        "summary":"简介",
        "iframe":"内容",
        "jiedai":"总接待人数",
        "chewei":"总停车位数",
        "emergcontactor":"应急联系人",
        "chainstore":"连锁经营情况",
        "weibo":"微博地址",
        "videoBox":"宣传片(上传)",
        "opentime":"开放时间",
        "exponent":"推荐指数",
        "price":"人均消费",
        "showSum":"查看数（只读）",
        "praiseNum":"点赞数（只读）",
        "sortno":"排序",  #  *
        "resourceLevel":"购物场所类型（选择）",   #有默认值：1  *
        "recommend":"选择(选择)",
        "state":"状态（选择）"    #有默认值：1  *
    },
    "乡村旅游": {
        "name": "名称", # *
        "shortname": "缩略名称",
        "english":"英文名称",
        "mbBox9":"经纬度（弹窗）",   # *
        "region":"所属地区（下拉）",  # *
        "impression":"印象",
        "tags":"标签（选择）",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "individualityLogoBox":"个性标识（上传）",
        "logobigBox":"标识大图（上传）",
        "logosmallBox":"标识小图（上传）",
        "icname":"企业工商注册全称",
        "orgcode":"组织机构代码",
        "bizlicense":"营业执照号码",
        "licenseno":"许可证号",
        "legal":"法人代表",
        "manager":"经理",
        "phone":"电话",
        "fax":"传真",
        "zipcode":"邮编",
        "address":"地址",
        "email":"E-mail",
        "site":"网址",
        "summary":"简介",
        "iframe":"内容",
        "jiedai":"总接待人数",
        "chewei":"总停车位数",
        "emergcontactor":"应急联系人",
        "emergphone":"应急联系电话",
        "chainstore":"连锁经营情况",
        "weibo":"微博地址",
        "videoBox":"宣传片(上传)",
        "opentime":"开放时间",
        "showSum":"点击查看数(只读)",
        "praiseNum":"点赞数（只读）",
        "sortno":"排序",    #有默认值   *
        "exponent":"推荐指数",
        "price":"人均消费",
        "zxTicket":"在线购票",
        "resourceLevel":"乡村旅游类型（选择）", #有默认值：1  *
        "recommend":"选择（选择）",
        "state":"状态（选择）"  #有默认值：1 *
    },
    "特色美食": {
        "name": "美食名称",   # *
        "price": "人均价格",
        "region":"所属地区（下拉）",  # *
        "mbBox9":"经纬度（弹窗）",
        "address":"地址",
        "showSum":"浏览量（只读）",
        "indexOrder":"排序",    #有默认值  *
        "tags":"标签（选择）",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "imagesUploadBox":"图片集（上传）",
        "diningSelectBox":"关联餐饮（上传）",
        "summary":"美食简介", # *
        "iframe":"美食详细介绍",
        "recommend":"选择（选择）",
        "state":"状态（选择）"  #有默认值：1 *
    },
    "旅游商品": {
        "name": "名称", # *
        "shortName": "缩略名称",
        "english":"英文名称",
        "mbBox9":"经纬度（弹窗）",   # *
        "region":"所属地区（下拉）",  # *
        "recPlace":"推荐购物场所",
        "logisticsTip":"物流提示",
        "shoppingTip":"购物提示",
        "recBrand":"推荐品牌",
        "showSum":"查看数（只读）",
        "praiseNum":"点赞数（只读）",
        "sortno":"排序",    #有默认值   *
        "tags":"标签（选择）",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "summary":"简介",
        "iframe":"内容",
        "commodityType":"商品类型（选择）",   #有默认值：1 *
        "state":"状态（选择）"  #有默认值：1 *
    },
    "导游信息": {
      "name": "名称", # *
      "region": "所属地区（下拉）", # *
      "guidelevel":"等级（选择）",    # *
      "gender":"性别（选择）",
      "guideiccardno":"导游IC卡号",
      "qualificationscard":"资格证号",
      "idno":"身份证号",
      "levelcardno":"等级证号",
      "education":"学历（列表）",
      "nationality":"民族",
      "english":"英文名称",
      "guidecardno":"导游卡号",
      "identification":"导游证号",
      "checkday":"年审日期（日期）",
      "birthday":"出生日期（日期）",
      "issueday":"发卡日期（日期）",
      "company":"所属公司",
      "phone":"手机",
      "zjzUploadBox":"证件照（上传）",
      "translations":"语种（选择）",
      "iframe":"导游介绍",
      "state":"状态（选择）"  #有默认值：1  *
    },
    "特色旅游场所": {
        "name": "名称（中文名称）",   # *
        "shortname": "缩略名称",
        "english":"英文名称",
        "mbBox9":"经纬度（弹窗）",   # *
        "region":"所属地区（下拉）",  # *
        "resourceType":"特色旅游场所类型（选择）",    # *
        "tag":"标签（选择）",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "individualityLogo":"个性标识（上传）",
        "logosmall":"标识小图（上传）",
        "logobig":"标识大图（上传）",
        "icname":"企业工商注册全称",
        "bizlicense":"营业执照号码",
        "legal":"法人代表",
        "phone":"电话",
        "zipcode":"邮编",
        "yuemail":"E-mail",
        "impression":"印象",
        "orgcode":"组织机构代码",
        "licenseno":"许可证号",
        "manager":"经理",
        "fax":"传真",
        "address":"地址",
        "site":"网址",
        "digest":"简介",
        "iframe":"内容",
        "jiedai":"总接待人数",
        "emergcontactor":"应急联系人",
        "chainstore":"连锁经营情况",
        "showSum":"查看数（只读）",
        "praiseNum":"点赞数(只读)",
        "recDegree":"推荐指数",
        "chewei":"总停车位数",
        "emergphone":"应急联系电话",
        "weibo":"微博地址",
        "consumption":"人均消费",
        "sortno":"排序",    #有默认值   *
        "openTime":"开放时间",
        "video":"宣传片（上传）",
        "recommend":"选择（选择）",
        "state":"状态（选择）"  #有默认值：1   *
    },
    "停车场": {
        "name": "停车场名称",  # *
        "shortname": "缩略名称",
        "region":"所属地区（下拉）",  # *
        "mbBox9":"经纬度（弹窗）",
        "phone":"电话",
        "address":"地址",
        "charging":"计费标准",
        "parkNumber":"车位总数",
        "serviceTime":"营业时间",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "state":"状态（选择）"  #有默认值：1  *
    },
    "加油站": {
        "name": "加油站名称",  # *
        "shortname": "中文简称",
        "region":"所属地区（下拉）",  # *
        "mbBox9":"经纬度（弹窗）",
        "phone": "联系电话",
        "address":"地址",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "state":"状态（选择）"  #有默认值：1  *
    },
    "厕所": {
        "name": "厕所名称",   # *
        "toilettype": "厕所类型(列表)",
        "region":"所属地区（下拉）",  # *
        "mbBox9":"经纬度（弹窗）",
        "scale":"规模大小",
        "feescale":"收费标准",
        "male":"男坑位",
        "female":"女坑位",
        "deformity":"残疾人专用",
        "mother":"母婴室",
        "phone":"联系电话",
        "address":"地址",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "toiletstar":"厕所星级（选择）",#有默认值;1
        "state":"状态（选择）"  #有默认值：1 *
    },
    "机场": {
        "name":"名称",  # *
        "threeCode":"所属机场三字代码",   # *
        "region":"所属地区（下拉）",  # *
        "mbBox9":"经纬度（弹窗）",   # *
        "passTime":"通航时间",
        "acreage":"占地面积",
        "address":"地址",
        "contactor": "联系人",
        "phone": "联系电话",
        "serverType":"服务类型（选择）",#有默认值;1
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "summary": "简介",
        "jcGrade":"机场等级（选择）",#有默认值：1
        "state":"状态（选择）"#有默认值：1
    },
    "客运站": {
        "name": "名称",   # *
        "shortname": "简称",
        "region":"所属地区（下拉）",    # *
        "mbBox9":"经纬度（弹窗）", # *
        "passTime":"开通时间",
        "acreage":"占地面积",
        "phone":"电话",
        "address":"地址",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "mainLine":"主要线路",
        "serverType":"服务类型(选择)",#有默认值：1
        "highGrade":"等级（选择）",#有默认值：1
        "state":"状态（选择）"#有默认值：1
    },
    "医疗点": {
        "name":"凯里新增医疗点" ,  # *
        "shortname":"缩略名称",
        "region":"所属地区（下拉）",   # *
        "mbBox9":"默认",
        "address":"凯里市",
        "phone":"急救电话",
        "logoUploadBox_1_1": "形象标识(1:1)",  # 选一个则全部生效
        "logoUploadBox_2_1": "形象标识(2:1)",
        "logoUploadBox_2_3": "形象标识(2:3)",
        "logoUploadBox_4_3": "形象标识(4:3)",
        "logoUploadBox_16_9": "形象标识(16:9)",
        "resourceLevel":"医院等级（选择）",#有默认值;1
        "hospitalType":"医院类别（选择）",#有默认值：1
        "state":"状态（选择）"#有默认值：1
    }
  },
    "旅游公共信息服务平台-内容管理":{
        "友情链接": {},
        "": {},
        "": {},
        "": {},
        "": {},
        "": {},
        "": {},
        "": {},
        "": {},
        "": {},
        "": {}
    }
}


shangchuan_data = ['logoUploadBox_1_1','logobigBox','logosmallBox','videoBox','audioBox','panoramaWebBox']
riqi = []
dingwei_data = ['mbBox9']
list_data = ['resourceLevel','hospitalType','state']
sep_list = ['regionSelector',]
list_data_span = []
sele_data = ['state','hospitalType','resourceLevel']
button = []



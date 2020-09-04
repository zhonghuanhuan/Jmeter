# -*- coding: utf-8 -*-
"""
    @Author  : zhh
    @Time    : 2019/4/24 0024 上午 9:19
    @Comment : 根据一个给定的XML Schema，使用DOM树的形式从空白文件生成一个XML。
"""
from xml.dom.minidom import Document

doc = Document()  #创建DOM文档对象

# def bool_prop(father,attribute_value,text,name="name"):
#     boolProp = doc.createElement('boolProp')
#     boolProp.setAttribute(name,attribute_value)
#     boolProp_text = doc.createTextNode(text)
#     boolProp.appendChild(boolProp_text)
#     father.appendChild(boolProp)
#
# def string_prop(father,attribute_value,text,name="name"):
#     stringProp = doc.createElement('stringProp')
#     stringProp.setAttribute(name,attribute_value)
#     stringProp_text = doc.createTextNode(text)
#     stringProp.appendChild(stringProp_text)
#     father.appendChild(stringProp)
'''
    函数说明：
        base_prop_1->只含有一个属性的元素
    参数说明：
        father->父元素；prop_name->元素名称；
        attribute_value->元素属性值；text->元素文本；
        attribute_name->元素属性名，默认值为'name'
'''
def base_prop_1(father,prop_name,attribute_value,text="",attribute_name="name"):
    base_prop = doc.createElement(prop_name)
    base_prop.setAttribute(attribute_name,attribute_value)
    base_prop_text = doc.createTextNode(text)
    base_prop.appendChild(base_prop_text)
    father.appendChild(base_prop)
    return base_prop

'''
    函数说明：
        base_prop_2->只含有两个属性的元素
    参数说明：
        father->父元素；prop_name->元素名称；
        attribute_name_N_value->元素第N个属性的值；
        attribute_name_N->元素第N个属性名
'''
def base_prop_2(father,prop_name,attribute_name_1_value,attribute_name_2_value,attribute_name_1='name',attribute_name_2='elementType'):
    base_prop = doc.createElement(prop_name)
    base_prop.setAttribute(attribute_name_1,attribute_name_1_value)
    base_prop.setAttribute(attribute_name_2, attribute_name_2_value)
    father.appendChild(base_prop)
    return base_prop

'''
    函数说明：
        base_prop_2->只含有两个属性的元素
    参数说明：
        father->父元素；prop_name->元素名称；
        attribute_name_N_value->元素第N个属性的值；
        attribute_name_N->元素第N个属性名
'''
def base_prop_4(father,prop_name,guiclass_value,testclass_value,testname_value,enabled_value='true'):
    base_prop = doc.createElement(prop_name)
    base_prop.setAttribute('guiclass',guiclass_value)
    base_prop.setAttribute('testclass',testclass_value )
    base_prop.setAttribute('testname',testname_value )
    base_prop.setAttribute('enabled', enabled_value)
    father.appendChild(base_prop)
    return base_prop

'''
    函数说明：
        base_prop_6->只含有7个属性的元素
    参数说明：
        father->父元素；prop_name->元素名称；
        attribute_name_N_value->元素第N个属性的值；
        attribute_name_N->元素第N个属性名
'''
def base_prop_5(father,prop_name,name_value,elementType_value,guiclass_value,testclass_value,enabled_value='true'):
    base_prop = doc.createElement(prop_name)
    base_prop.setAttribute('name', name_value)
    base_prop.setAttribute('elementType', elementType_value)
    base_prop.setAttribute('guiclass',guiclass_value)
    base_prop.setAttribute('testclass',testclass_value )
    base_prop.setAttribute('enabled', enabled_value)
    father.appendChild(base_prop)
    return base_prop

'''
    函数说明：
        base_prop_6->只含有7个属性的元素
    参数说明：
        father->父元素；prop_name->元素名称；
        attribute_name_N_value->元素第N个属性的值；
        attribute_name_N->元素第N个属性名
'''
def base_prop_6(father,prop_name,name_value,elementType_value,guiclass_value,testclass_value,testname_value,enabled_value='true'):
    base_prop = doc.createElement(prop_name)
    base_prop.setAttribute('name', name_value)
    base_prop.setAttribute('elementType', elementType_value)
    base_prop.setAttribute('guiclass',guiclass_value)
    base_prop.setAttribute('testclass',testclass_value )
    base_prop.setAttribute('testname',testname_value )
    base_prop.setAttribute('enabled', enabled_value)
    father.appendChild(base_prop)
    return base_prop

# def base_element_prop(father,attribute_value,elementType,name="name"):
#     elementProp = doc.createElement('elementProp')
#     elementProp.setAttribute(name,attribute_value)
#     elementProp.setAttribute('elementType',elementType)
#     father.appendChild(elementProp)

def header_element_prop(father,header_name,header_value):
    elementprop = base_prop_2(father,'elementProp',header_name,'Header')
    base_prop_1(elementprop,'stringProp',"Header.name",header_name)
    base_prop_1(elementprop, 'stringProp', "header_value", header_value)



    # elementProp = doc.createElement('elementProp')
    # elementProp.setAttribute('name',header_name)
    # elementProp.setAttribute('elementType',"Header")
    # father.appendChild(elementProp)
    # base_prop_1(elementProp,'stringProp','Header.name',header_name)
    # base_prop_1(elementProp,'stringProp','Header.value',header_value)

# hash_tree 空元素
def hash_tree(father):
    hashTree = doc.createElement('hashTree')
    father.appendChild(hashTree)
    return hashTree

def transaction_controller(father,testname):
    TransactionController = doc.createElement('TransactionController')
    TransactionController.setAttribute('guiclass',"TransactionControllerGui")
    TransactionController.setAttribute('testclass',"TransactionController")
    TransactionController.setAttribute('testname',testname)
    TransactionController.setAttribute('enabled',"true")
    father.appendChild(TransactionController)
    base_prop_1(TransactionController,'boolProp','TransactionController.includeTimers','false')
    base_prop_1(TransactionController,'boolProp','TransactionController.parent','true')
    return TransactionController

# def http_sampler_proxy(father,testname):
#     HTTPSamplerProxy = doc.createElement('HTTPSamplerProxy')
#     HTTPSamplerProxy.setAttribute('guiclass',"HttpTestSampleGui")
#     HTTPSamplerProxy.setAttribute('testclass', "HTTPSamplerProxy")
#     HTTPSamplerProxy.setAttribute('testname', testname)
#     HTTPSamplerProxy.setAttribute('enabled', "true")
#     father.appendChild(HTTPSamplerProxy)

# ------------------------------------根元素------------------------------------------------------------
DOCUMENT = doc.createElement('jmeterTestPlan') #创建根元素
DOCUMENT.setAttribute('version',"1.2")#设置命名空间
DOCUMENT.setAttribute('properties',"5.0")
DOCUMENT.setAttribute('jmeter',"5.3")
#DOCUMENT.setAttribute('xsi:noNamespaceSchemaLocation','DOCUMENT.xsd')#引用本地XML Schema
doc.appendChild(DOCUMENT)
############item:Python处理XML之Minidom################
# item.setAttribute('genre','XML')

#---------------------------------------TestPlan------------------------------------------
testPlan_hashTree = hash_tree(DOCUMENT)

test_plan = base_prop_4(testPlan_hashTree,'TestPlan','TestPlanGui','TestPlan','测试计划')

base_prop_1(test_plan,'stringProp',"TestPlan.comments","")
base_prop_1(test_plan,'boolProp',"TestPlan.functional_mode","false")
base_prop_1(test_plan,'boolProp',"TestPlan.tearDown_on_shutdown","true")
base_prop_1(test_plan,'boolProp',"TestPlan.serialize_threadgroups","false")
testplan_elementProp = base_prop_6(test_plan,'elementProp',"TestPlan.user_defined_variables","Arguments","ArgumentsPanel","Arguments","用户定义的变量","true")
base_prop_1(test_plan,'stringProp',"TestPlan.user_define_classpath","")

base_prop_1(testplan_elementProp,'collectionProp',"Arguments.arguments","")

#---------------------------------------ThreadGroup------------------------------------------
ThreadGroup_hashTree = hash_tree(testPlan_hashTree)

thread_group = base_prop_4(ThreadGroup_hashTree,'ThreadGroup',"ThreadGroupGui","ThreadGroup","线程组")

base_prop_1(thread_group,'stringProp',"ThreadGroup.on_sample_error","continue")
ThreadGroup_elementProp = base_prop_6(thread_group,'elementProp',"ThreadGroup.main_controller",\
                                      "LoopController","LoopControlPanel","LoopController","循环控制器"
                                      )
base_prop_1(thread_group,'stringProp',"ThreadGroup.num_threads","1")
base_prop_1(thread_group,'stringProp',"ThreadGroup.ramp_time","0")
base_prop_1(thread_group,'boolProp',"ThreadGroup.scheduler","false")
base_prop_1(thread_group,'stringProp',"ThreadGroup.duration","600")
base_prop_1(thread_group,'stringProp',"ThreadGroup.delay","")
base_prop_1(thread_group,'boolProp',"ThreadGroup.same_user_on_next_iteration","true")

base_prop_1(ThreadGroup_elementProp,'boolProp',"LoopController.continue_forever","false")
base_prop_1(ThreadGroup_elementProp,'stringProp',"LoopController.loops","1")

#---------------------------------------hashTree_data------------------------------------------
hashTree_data = hash_tree(ThreadGroup_hashTree)

#---------------------------------------CookieManager------------------------------------------
cookie_manager = base_prop_4(hashTree_data,'CookieManager',"CookiePanel","CookieManager","HTTP Cookie管理器")

base_prop_1(cookie_manager,'collectionProp',"CookieManager.cookies")
base_prop_1(cookie_manager,'boolProp',"CookieManager.clearEachIteration","true")

#---------------------------------------HeaderManager------------------------------------------
hash_tree(hashTree_data)

header_manager = base_prop_4(hashTree_data,'HeaderManager',"HeaderPanel","HeaderManager","HTTP信息头管理器")

HeaderManager_collectionProp = base_prop_1(header_manager,'collectionProp',"HeaderManager.headers")

header_element_prop(HeaderManager_collectionProp,'Referer',"http://auth.idscloud.bamboocloud.com:6080/idp/authcenter/ActionAuthChain?entityId=oauth1")
header_element_prop(HeaderManager_collectionProp,'Accept-Language',"zh-CN,zh;q=0.9")
header_element_prop(HeaderManager_collectionProp,"Upgrade-Insecure-Requests","1")
header_element_prop(HeaderManager_collectionProp,"Cache-Control","max-age=0")
header_element_prop(HeaderManager_collectionProp,"Accept-Encoding","gzip, deflate")
header_element_prop(HeaderManager_collectionProp,"User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
header_element_prop(HeaderManager_collectionProp,'Accept',"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3")

#---------------------------------------ConfigTestElement------------------------------------------
hash_tree(hashTree_data)

config_test_element = base_prop_4(hashTree_data,'ConfigTestElement',"HttpDefaultsGui","ConfigTestElement","HTTP请求默认值")

ConfigTestElement_elementProp = base_prop_6(config_test_element,'elementProp',"HTTPsampler.Arguments","Arguments","HTTPArgumentsPanel","Arguments","用户定义的变量")
base_prop_1(config_test_element,'stringProp',"HTTPSampler.domain","auth.idscloud.bamboocloud.com")
base_prop_1(config_test_element,'stringProp',"HTTPSampler.port","6080")
base_prop_1(config_test_element,'stringProp',"HTTPSampler.protocol","http")
base_prop_1(config_test_element,'stringProp',"HTTPSampler.contentEncoding","")
base_prop_1(config_test_element,'stringProp',"HTTPSampler.path","/idp/oauth2/")
base_prop_1(config_test_element,'stringProp',"HTTPSampler.concurrentPool","6")
base_prop_1(config_test_element,'stringProp',"HTTPSampler.connect_timeout","")
base_prop_1(config_test_element,'stringProp',"HTTPSampler.response_timeout","")

base_prop_1(ConfigTestElement_elementProp,'collectionProp',"Arguments.arguments")

#---------------------------------------CSVDataSet------------------------------------------
hash_tree(hashTree_data)

csv_data_set = base_prop_4(hashTree_data,'CSVDataSet',"TestBeanGUI","CSVDataSet","CSV 数据文件设置","false")

base_prop_1(csv_data_set,'stringProp',"delimiter",",")
base_prop_1(csv_data_set,'stringProp',"fileEncoding","UTF-8")
base_prop_1(csv_data_set,'stringProp',"filename",",C:/Users/Administrator/Desktop/apache-jmeter-5.0/bin/bam/user.csv")
base_prop_1(csv_data_set,'boolProp',"ignoreFirstLine","false")
base_prop_1(csv_data_set,'boolProp',"quotedData","false")
base_prop_1(csv_data_set,'boolProp',"recycle","true")
base_prop_1(csv_data_set,'stringProp',"shareMode","shareMode.all")
base_prop_1(csv_data_set,'stringProp',"stopThread",",")
base_prop_1(csv_data_set,'boolProp',"quotedData","false")
base_prop_1(csv_data_set,'stringProp',"variableNames","user")

'''
#---------------------------------------TransactionController------------------------------------------
hash_tree(hashTree_data)

transaction_controller = base_prop_4(hashTree_data,'TransactionController',"TransactionControllerGui","TransactionController","01_login_page")

base_prop_1(transaction_controller,'boolProp',"TransactionController.includeTimers","false")
base_prop_1(transaction_controller,'boolProp',"TransactionController.parent","true")


#*************************************************TransactionController_HTTPSamplerProxy(01-1)**************************************************
TransactionController_hashTree = hash_tree(hashTree_data)

HTTPSamplerProxy = base_prop_4(TransactionController_hashTree,'HTTPSamplerProxy',"HttpTestSampleGui","HTTPSamplerProxy","01-1 /idp/oauth2/authorize")

elementProp = base_prop_5(HTTPSamplerProxy,'elementProp',"HTTPsampler.Arguments","Arguments","HTTPArgumentsPanel","Arguments","true")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.domain","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.port","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.protocol","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.contentEncoding","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.path","/idp/oauth2/authorize")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.method","GET")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.follow_redirects","true")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.auto_redirects","false")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.use_keepalive","true")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.DO_MULTIPART_POST","false")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.embedded_url_re","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.connect_timeout","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.response_timeout","")
base_prop_1(HTTPSamplerProxy,'stringProp',"TestPlan.comments","Detected the start of a redirect chain")

collectionProp = base_prop_1(elementProp,'collectionProp',"Arguments.arguments")

elementProp = base_prop_2(collectionProp,'elementProp',"redirect_uri","HTTPArgument")

base_prop_1(elementProp,'elementProp',"HTTPArgument.always_encode","false")
base_prop_1(elementProp,'stringProp',"Argument.name","redirect_uri")
base_prop_1(elementProp,'stringProp',"Argument.value","https://www.baidu.com")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'elementProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"state","HTTPArgument")

base_prop_1(elementProp,'elementProp',"HTTPArgument.always_encode","false")
base_prop_1(elementProp,'stringProp',"Argument.name","state")
base_prop_1(elementProp,'stringProp',"Argument.value","123")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'elementProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"client_id","HTTPArgument")

base_prop_1(elementProp,'elementProp',"HTTPArgument.always_encode","false")
base_prop_1(elementProp,'stringProp',"Argument.name","client_id")
base_prop_1(elementProp,'stringProp',"Argument.value","oauth1")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'elementProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"response_type","HTTPArgument")

base_prop_1(elementProp,'elementProp',"HTTPArgument.always_encode","false")
base_prop_1(elementProp,'stringProp',"Argument.name","response_type")
base_prop_1(elementProp,'stringProp',"Argument.value","code")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'elementProp',"HTTPArgument.use_equals","true")

#---------------------------------------HeaderManager_TransactionController------------------------------------------
hashTree = hash_tree(TransactionController_hashTree)

header_manager = base_prop_4(hashTree,'HeaderManager',"HeaderPanel","HeaderManager","HTTP信息头管理器")

HeaderManager_collectionProp = base_prop_1(header_manager,'collectionProp',"HeaderManager.headers")

# header_element_prop(HeaderManager_collectionProp,'Referer',"http://auth.idscloud.bamboocloud.com:6080/idp/authcenter/ActionAuthChain?entityId=oauth1")
header_element_prop(HeaderManager_collectionProp,'Accept-Language',"zh-CN,zh;q=0.9")
header_element_prop(HeaderManager_collectionProp,"Upgrade-Insecure-Requests","1")
# header_element_prop(HeaderManager_collectionProp,"Cache-Control","max-age=0")
header_element_prop(HeaderManager_collectionProp,"Accept-Encoding","gzip, deflate")
header_element_prop(HeaderManager_collectionProp,"User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
header_element_prop(HeaderManager_collectionProp,'Accept',"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3")

#*************************************************TransactionController_HTTPSamplerProxy(01-4)**************************************************
# TransactionController_hashTree = hash_tree(hashTree_data)

HTTPSamplerProxy = base_prop_4(TransactionController_hashTree,'HTTPSamplerProxy',"HttpTestSampleGui","HTTPSamplerProxy","01-4 /idp/displayVerificationCode.do")

elementProp = base_prop_5(HTTPSamplerProxy,'elementProp',"HTTPsampler.Arguments","Arguments","HTTPArgumentsPanel","Arguments","true")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.domain","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.port","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.protocol","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.contentEncoding","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.path","/idp/displayVerificationCode.do")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.method","POST")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.follow_redirects","true")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.auto_redirects","false")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.use_keepalive","true")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.DO_MULTIPART_POST","false")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.embedded_url_re","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.connect_timeout","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.response_timeout","")
# base_prop_1(HTTPSamplerProxy,'stringProp',"TestPlan.comments","Detected the start of a redirect chain")

collectionProp = base_prop_1(elementProp,'collectionProp',"Arguments.arguments")

#---------------------------------------HeaderManager_TransactionController------------------------------------------
hashTree = hash_tree(TransactionController_hashTree)

header_manager = base_prop_4(hashTree,'HeaderManager',"HeaderPanel","HeaderManager","HTTP信息头管理器")

HeaderManager_collectionProp = base_prop_1(header_manager,'collectionProp',"HeaderManager.headers")

header_element_prop(HeaderManager_collectionProp,'Referer',"http://auth.idscloud.bamboocloud.com:6080/idp/authcenter/ActionAuthChain?entityId=oauth1")
header_element_prop(HeaderManager_collectionProp,'Accept-Language',"zh-CN,zh;q=0.9")
header_element_prop(HeaderManager_collectionProp,"Origin","http://auth.idscloud.bamboocloud.com:6080")
header_element_prop(HeaderManager_collectionProp,"X-Requested-With","XMLHttpRequest")
header_element_prop(HeaderManager_collectionProp,"Accept-Encoding","gzip, deflate")
header_element_prop(HeaderManager_collectionProp,'Accept',"*/*")
header_element_prop(HeaderManager_collectionProp,"User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")

#*************************************************TransactionController_HTTPSamplerProxy(01-5)**************************************************
# TransactionController_hashTree = hash_tree(hashTree_data)

HTTPSamplerProxy = base_prop_4(TransactionController_hashTree,'HTTPSamplerProxy',"HttpTestSampleGui","HTTPSamplerProxy","01-5 /idp/displayVerificationCode.do")

elementProp = base_prop_5(HTTPSamplerProxy,'elementProp',"HTTPsampler.Arguments","Arguments","HTTPArgumentsPanel","Arguments","true")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.domain","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.port","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.protocol","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.contentEncoding","UTF-8")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.path","/idp/displayVerificationCode.do")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.method","POST")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.follow_redirects","true")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.auto_redirects","false")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.use_keepalive","true")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.DO_MULTIPART_POST","false")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.embedded_url_re","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.connect_timeout","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.response_timeout","")
# base_prop_1(HTTPSamplerProxy,'stringProp',"TestPlan.comments","Detected the start of a redirect chain")

collectionProp = base_prop_1(elementProp,'collectionProp',"Arguments.arguments")

elementProp = base_prop_2(collectionProp,'elementProp',"j_username","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","false")
base_prop_1(elementProp,'stringProp',"Argument.name","j_username")
base_prop_1(elementProp,'stringProp',"Argument.value","keke1")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"j_authMethodID","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","false")
base_prop_1(elementProp,'stringProp',"Argument.name","j_authMethodID")
base_prop_1(elementProp,'stringProp',"Argument.value","1")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"spAuthChainCode","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","false")
base_prop_1(elementProp,'stringProp',"Argument.name","spAuthChainCode")
base_prop_1(elementProp,'stringProp',"Argument.value","cc2fdbc3599b48a69d5c82a665256b6b")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

#---------------------------------------HeaderManager_TransactionController------------------------------------------
hashTree = hash_tree(TransactionController_hashTree)

header_manager = base_prop_4(hashTree,'HeaderManager',"HeaderPanel","HeaderManager","HTTP信息头管理器")

HeaderManager_collectionProp = base_prop_1(header_manager,'collectionProp',"HeaderManager.headers")

header_element_prop(HeaderManager_collectionProp,'Referer',"http://auth.idscloud.bamboocloud.com:6080/idp/authcenter/ActionAuthChain?entityId=oauth1")
header_element_prop(HeaderManager_collectionProp,'Accept-Language',"zh-CN,zh;q=0.9")
header_element_prop(HeaderManager_collectionProp,"Origin","http://auth.idscloud.bamboocloud.com:6080")
header_element_prop(HeaderManager_collectionProp,"X-Requested-With","XMLHttpRequest")
header_element_prop(HeaderManager_collectionProp,"Content-Type","application/x-www-form-urlencoded; charset=UTF-8")
header_element_prop(HeaderManager_collectionProp,"Accept-Encoding","gzip, deflate")
header_element_prop(HeaderManager_collectionProp,'Accept',"*/*")
header_element_prop(HeaderManager_collectionProp,"User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")

#---------------------------------------TransactionController------------------------------------------
# hash_tree(hashTree_data)

transaction_controller = base_prop_4(hashTree_data,'TransactionController',"TransactionControllerGui","TransactionController","01_login_page")

base_prop_1(transaction_controller,'boolProp',"TransactionController.includeTimers","false")
base_prop_1(transaction_controller,'boolProp',"TransactionController.parent","true")

#*************************************************TransactionController_HTTPSamplerProxy(01-6)**************************************************
TransactionController_hashTree = hash_tree(hashTree_data)

HTTPSamplerProxy = base_prop_4(TransactionController_hashTree,'HTTPSamplerProxy',"HttpTestSampleGui","HTTPSamplerProxy","01-6 /idp/authcenter/ActionAuthChain")

elementProp = base_prop_5(HTTPSamplerProxy,'elementProp',"HTTPsampler.Arguments","Arguments","HTTPArgumentsPanel","Arguments","true")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.domain","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.port","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.protocol","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.contentEncoding","UTF-8")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.path","/idp/authcenter/ActionAuthChain")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.method","POST")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.follow_redirects","true")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.auto_redirects","false")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.use_keepalive","true")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.DO_MULTIPART_POST","false")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.embedded_url_re","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.connect_timeout","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.response_timeout","")
# base_prop_1(HTTPSamplerProxy,'stringProp',"TestPlan.comments","Detected the start of a redirect chain")

collectionProp = base_prop_1(elementProp,'collectionProp',"Arguments.arguments")

elementProp = base_prop_2(collectionProp,'elementProp',"j_username","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","false")
base_prop_1(elementProp,'stringProp',"Argument.name","j_username")
base_prop_1(elementProp,'stringProp',"Argument.value","keke1")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"j_password","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","true")
base_prop_1(elementProp,'stringProp',"Argument.name","j_password")
base_prop_1(elementProp,'stringProp',"Argument.value","em6fxLIASRhsfIKWdccwLA==")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"j_checkcode","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","true")
base_prop_1(elementProp,'stringProp',"Argument.name","j_checkcode")
base_prop_1(elementProp,'stringProp',"Argument.value","验证码")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"op","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","true")
base_prop_1(elementProp,'stringProp',"Argument.name","op")
base_prop_1(elementProp,'stringProp',"Argument.value","login")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

#---------------------------------------HeaderManager_TransactionController------------------------------------------
hashTree = hash_tree(TransactionController_hashTree)

header_manager = base_prop_4(hashTree,'HeaderManager',"HeaderPanel","HeaderManager","HTTP信息头管理器")

HeaderManager_collectionProp = base_prop_1(header_manager,'collectionProp',"HeaderManager.headers")

header_element_prop(HeaderManager_collectionProp,'Referer',"http://auth.idscloud.bamboocloud.com:6080/idp/authcenter/ActionAuthChain?entityId=oauth1")
header_element_prop(HeaderManager_collectionProp,'Accept-Language',"zh-CN,zh;q=0.9")
header_element_prop(HeaderManager_collectionProp,"Origin","http://auth.idscloud.bamboocloud.com:6080")
header_element_prop(HeaderManager_collectionProp,"X-Requested-With","XMLHttpRequest")
header_element_prop(HeaderManager_collectionProp,"Content-Type","application/x-www-form-urlencoded; charset=UTF-8")
header_element_prop(HeaderManager_collectionProp,"Accept-Encoding","gzip, deflate")
header_element_prop(HeaderManager_collectionProp,'Accept',"*/*")
header_element_prop(HeaderManager_collectionProp,"User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")

#---------------------------------------ResponseAssertion_TransactionController------------------------------------------
hash_tree(hashTree)

response_assertion = base_prop_4(hashTree,'ResponseAssertion',"AssertionGui","ResponseAssertion","响应断言")

collectionProp = base_prop_1(response_assertion,'collectionProp','Asserion.test_strings')
base_prop_1(response_assertion,'stringProp',"Assertion.custom_message","")
base_prop_1(response_assertion,'stringProp',"Assertion.test_field","Assertion.response_data")
base_prop_1(response_assertion,'boolProp',"Assertion.assume_success","false")
base_prop_1(response_assertion,'intProp',"Assertion.test_type","2")

base_prop_1(collectionProp,'stringProp',"57423749","&quot;loginFailed&quot;:&quot;false&quot;")

#*************************************************TransactionController_HTTPSamplerProxy(01-7)**************************************************
# TransactionController_hashTree = hash_tree(hashTree_data)

HTTPSamplerProxy = base_prop_4(TransactionController_hashTree,'HTTPSamplerProxy',"HttpTestSampleGui","HTTPSamplerProxy","01-7 /idp/AuthnEngine?currentAuth=urn_oasis_names_tc_SAML_2.0_ac_classes_BAMUsernamePassword")

elementProp = base_prop_5(HTTPSamplerProxy,'elementProp',"HTTPsampler.Arguments","Arguments","HTTPArgumentsPanel","Arguments","true")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.domain","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.port","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.protocol","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.contentEncoding","UTF-8")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.path","/idp/AuthnEngine?currentAuth=urn_oasis_names_tc_SAML_2.0_ac_classes_BAMUsernamePassword")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.method","POST")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.follow_redirects","true")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.auto_redirects","false")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.use_keepalive","true")
base_prop_1(HTTPSamplerProxy,'boolProp',"HTTPSampler.DO_MULTIPART_POST","false")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.embedded_url_re","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.connect_timeout","")
base_prop_1(HTTPSamplerProxy,'stringProp',"HTTPSampler.response_timeout","")
base_prop_1(HTTPSamplerProxy,'stringProp',"TestPlan.comments","Detected the start of a redirect chain")

collectionProp = base_prop_1(elementProp,'collectionProp',"Arguments.arguments")

elementProp = base_prop_2(collectionProp,'elementProp',"j_username","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","false")
base_prop_1(elementProp,'stringProp',"Argument.name","j_username")
base_prop_1(elementProp,'stringProp',"Argument.value","keke1")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"j_password","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","true")
base_prop_1(elementProp,'stringProp',"Argument.name","j_password")
base_prop_1(elementProp,'stringProp',"Argument.value","oobx4gfvjUJsfIKWdccwLA%3D%3D")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"j_checkcode","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","true")
base_prop_1(elementProp,'stringProp',"Argument.name","j_checkcode")
base_prop_1(elementProp,'stringProp',"Argument.value","%E9%AA%8C%E8%AF%81%E7%A0%81")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"op","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","true")
base_prop_1(elementProp,'stringProp',"Argument.name","op")
base_prop_1(elementProp,'stringProp',"Argument.value","login")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")

elementProp = base_prop_2(collectionProp,'elementProp',"spAuthChainCode","HTTPArgument")

base_prop_1(elementProp,'boolProp',"HTTPArgument.always_encode","true")
base_prop_1(elementProp,'stringProp',"Argument.name","spAuthChainCode")
base_prop_1(elementProp,'stringProp',"Argument.value","cc2fdbc3599b48a69d5c82a665256b6b")
base_prop_1(elementProp,'stringProp',"Argument.metadata","=")
base_prop_1(elementProp,'boolProp',"HTTPArgument.use_equals","true")
#---------------------------------------HeaderManager_TransactionController------------------------------------------
hashTree = hash_tree(TransactionController_hashTree)

header_manager = base_prop_4(hashTree,'HeaderManager',"HeaderPanel","HeaderManager","HTTP信息头管理器")

HeaderManager_collectionProp = base_prop_1(header_manager,'collectionProp',"HeaderManager.headers")

header_element_prop(HeaderManager_collectionProp,'Referer',"http://auth.idscloud.bamboocloud.com:6080/idp/authcenter/ActionAuthChain?entityId=oauth1")
header_element_prop(HeaderManager_collectionProp,'Accept-Language',"zh-CN,zh;q=0.9")
header_element_prop(HeaderManager_collectionProp,"Origin","http://auth.idscloud.bamboocloud.com:6080")
# header_element_prop(HeaderManager_collectionProp,"X-Requested-With","XMLHttpRequest")
header_element_prop(HeaderManager_collectionProp,'Accept',"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3")
# header_element_prop(HeaderManager_collectionProp,'Upgrade-Insecure-Requests',"1")
header_element_prop(HeaderManager_collectionProp,"Content-Type","application/x-www-form-urlencoded; charset=UTF-8")
header_element_prop(HeaderManager_collectionProp,"Cache-Control","max-age=0")
header_element_prop(HeaderManager_collectionProp,"Accept-Encoding","gzip, deflate")

header_element_prop(HeaderManager_collectionProp,"User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")

#---------------------------------------BoundaryExtractorGui_TransactionController------------------------------------------
hash_tree(hashTree)

boundary_extractor = base_prop_4(hashTree,'BoundaryExtractor',"BoundaryExtractorGui","BoundaryExtractor","边界提取器","false")

base_prop_1(boundary_extractor,'stringProp',"BoundaryExtractor.useHeaders","true")
base_prop_1(boundary_extractor,'stringProp',"BoundaryExtractor.refname","code")
base_prop_1(boundary_extractor,'stringProp',"BoundaryExtractor.lboundary","code=")
base_prop_1(boundary_extractor,'stringProp',"BoundaryExtractor.rboundary","&amp;state")
base_prop_1(boundary_extractor,'stringProp',"BoundaryExtractor.default","")
base_prop_1(boundary_extractor,'boolProp',"BoundaryExtractor.default_empty_value","false")
base_prop_1(boundary_extractor,'stringProp',"BoundaryExtractor.match_number","1")
base_prop_1(boundary_extractor,'stringProp',"Sample.scope","all")

#---------------------------------------RegexExtractor_TransactionController------------------------------------------
hash_tree(hashTree)

regex_extractor = base_prop_4(hashTree,'RegexExtractor',"RegexExtractorGui","RegexExtractor","正则表达式提取器","true")

base_prop_1(regex_extractor,'stringProp',"RegexExtractor.useHeaders","true")
base_prop_1(regex_extractor,'stringProp',"RegexExtractor.refname","code")
base_prop_1(regex_extractor,'stringProp',"RegexExtractor.regex","code=(\w{32})")
base_prop_1(regex_extractor,'stringProp',"RegexExtractor.template","$1$")
base_prop_1(regex_extractor,'stringProp',"RegexExtractor.default","")
base_prop_1(regex_extractor,'stringProp',"RegexExtractor.match_number","1")
base_prop_1(regex_extractor,'stringProp',"Sample.scope","all")
'''

'''
price = doc.createElement('price')
price_text = doc.createTextNode('28')
price.appendChild(price_text)
item.appendChild(price)
'''
########### 将DOM对象doc写入文件
f = open('py_jmeter.jmx','w')
#f.write(doc.toprettyxml(indent = '\t', newl = '\n', encoding = 'utf-8'))
doc.writexml(f, indent='  ', newl='\n', addindent='  ', encoding='utf-8')
f.close()





print("用户定义的变量")
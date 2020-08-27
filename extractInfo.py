# coding=utf-8
'''
Author: 上九万里
LastEditors: 上九万里
version: 
Date: 2020-08-26 19:58:36
LastEditTime: 2020-08-27 10:14:42
Description: 
'''
import re

def get_location(text):
    location_list = r'北京|帝都|魔都|天津|河北|山西|内蒙|辽宁|吉林|黑龙江|东北|上海|江苏|浙江|安徽|福建|江西|山东|河南|湖北|湖南|广东|广西|海南|重庆|四川|贵州|云南|陕西|甘肃|青海|宁夏|新疆|沈阳|长春|哈尔滨|南京|武汉|广州|成都|西安|石家庄|唐山|太原|包头|大连|徐州|杭州|福州|南昌|济南|青岛|郑州|长沙|贵阳|昆明|兰州|乌鲁木齐|苏州|宁波|海淀|合肥|厦门|深圳|南宁|美国|英国|日本|法国|海口|三亚'
    li = re.findall(location_list,text)
    li = list(set(li))
    res = ""
    if(len(li) == 0):
        res = "unknown"
        return res
    else:
        while len(li)!=0:
            res = res + li.pop() + ' '

    return res

def get_height(text):
    '''
    description:提取出身高，我们默认每个人的身高都是160-199之间的整数，且只匹配最先出现的身高数字
    param {type} 
    return {type} 
    '''
    p_height = r'1[6789][0-9][^0-9]'
    res = re.search(p_height,text)
    if(res == None):
        res = "unknown"
        return res
    else:
        return res.group(0)[0:3]

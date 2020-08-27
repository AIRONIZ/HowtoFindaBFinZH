# coding=utf-8

'''
Author: 上九万里
LastEditors: 上九万里
version: 1.0
Date: 2020-08-25 11:11:41
LastEditTime: 2020-08-26 20:07:18
'''
import re
def wash_content(content):
    p_para_end = r'</p>'                                #遇到</p>则换行
    res = re.sub(p_para_end,"\n",content)
    p_tag = r'<[^\u4E00-\u9FA5]*>'                      #删掉所有标签
    res = re.sub(p_tag,"\n",res)
    return res


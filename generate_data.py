#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Arthur Mei

import random
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

#生成随机的字符串(字母数字混合)
def random_string(str1,length):
	for i in range(0,length):
		tmp=random.randint(0,2)
		if(tmp==0):
			ch=chr(random.randint(0,25)+65)
			str1+=ch
		elif(tmp==1):
			ch=chr(random.randint(0,25)+97)
                        str1+=ch
		elif(tmp==2):
			ch=str(random.randint(0,9))
			str1+=ch
		else:
			print("generate error in random")
	
	return str1	

#生成随机的数字
def random_int(str2,length):
	for i in range(0,length):
		ch=str(random.randint(0,9))
		str2+=ch

	return str2	

#生成随机时间戳
def random_time():
	start_time=time.mktime((1976,1,1,0,0,0,0,0,0))
	stop_time=time.mktime((2038,12,12,23,59,59,0,0,0))
	crt=random.randint(start_time,stop_time)
	date=time.localtime(crt)
	date_time=time.strftime("%Y-%m-%d %H:%M:%S",date)
	
	return date_time




#生成随机的中文(姓名)
def random_chinese():
    val = random.randint(0x4E00, 0x9FA5)
    return unichr(val)

def first_name():  #   随机取姓氏字典
    first_name_list = [
        '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
        '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
        '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
        '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
        '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
        '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
        '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    n = random.randint(0, len(first_name_list) - 1)
    f_name = first_name_list[n]
    return f_name

def second_name():
    # 随机取数组中字符，取到空字符则没有second_name
    second_name_list = [random_chinese(), '']
    n = random.randint(0, 1)
    s_name = second_name_list[n]
    return s_name

def last_name():
    return random_chinese()

def create_name():
    name = first_name()+second_name()+last_name()
    return name



if __name__=='__main__':
	with open('/home/postgres/test.csv','a+') as file:	
		for i in range(0,10000):
			str1=""
			str2=""
			a=random_int(str2,6)
			b=create_name()
			c=random_time()
			d=random_string(str1,8)
			file.write(a+'\t'+b+'\t'+c+'\t'+d+'\n')
	file.close()


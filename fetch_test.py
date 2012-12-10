#!/usr/bin/python
import re
fp = open('/home/chen/test.html', 'r')
html_text = ''
for line in fp:
    html_text += line
tag_name = 0
tag_attr = 1
tag_end =  2
tag_text = 3
tag_child = 4
tag_parent = 5

tag_ss = '<'
tag_ee = '>'
tag_es = '</'
html_list = gen_taglist(6)

con_nu = html_text.find(tag_ss)


def fetch_tag(test_string):
    tag_ss = '<' 
    tag_ee = '>' 
    tag_es = '</'

    s_cont = 0
    e_cont = 0
    while(s_cont != len(test_string) or e_cont != len(test_string) or e_cont != -1 or s_cont != -1):
        tmp_cont = s_cont
        tag_tmp_text = ''
        test_string = test_string[e_cont:]
        s_cont = test_string.find(tag_ss)
        e_cont = test_string.find(tag_ee)

        if tmp_cont > e_cont:
            tag_tmp_string = test_string[s_cont:e_cont + 1]
            for tmp_char in tag_tmp_string:
                tag_tmp_text += tmp_char
            tag_list_text.append(tag_tmp_text)

        tag_tmp_string = test_string[s_cont:e_cont + 1]
        for tmp_char in tag_tmp_string:
            tag_tmp_text += tmp_char
def gen_taglist(range_num):
    tag_list = []
    for i in range(range_num):
        tag_list.append('')
    return tag_list



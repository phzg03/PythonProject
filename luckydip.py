#!/usr/bin/python
# coding=utf-8
import csv
import sys
import random

print("开始进行抽奖")


class LuckyDip:
    # 定义scv文件路径
    def __init__(self, filepath):
        self.empfile = filepath

    def creat_num(self):
        emplist = []
        with open(self.empfile) as f:
            empf = csv.reader(f)
            for emp in empf:
                emplist.append(emp)
        print('共有%s 人参与抽奖' % len(emplist))
        levels = int(input('抽奖等级，请输入：'))
        level_dict = {}
        for i in range(0, levels):
            print('请输入当前抽奖等级 %s 对应的奖品个数' % (i + 1))
            str_level_dict_key = sys.stdin.readline()
            int_level_dict_key = int(str_level_dict_key)
            level_dict[i] = int_level_dict_key
        for i in range(0, len(level_dict)):
            winers = []
            for j in range(0, int(level_dict[i])):
                winer = random.choice(emplist)
                winers.append(winer)
                emplist.remove(winer)
            print('抽奖等级 %s 下产出的获奖人员有：' % (i + 1))
            print(winers)


if __name__ == '__main__':
    peoples = LuckyDip('emps.csv')
    peoples.creat_num()

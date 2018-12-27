#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn
@CONTACT:zhaojing17@foxmail.com
@SOFTWERE:PyCharm
@FILE:main.py
@TIME:2018/12/26 00:17
@DES:
'''


locals = ["xiamen","guangzhou","sanya","hangzhou","beihai"]
local_star1 =  "changsha"
local_end1 = "chongqing"
local_star2 = local_end1
local_end2 = "wuhan"
lines1 = []
prices = []
lines2 = []

def create_rout_line1():
    for local in locals:
        print
        line =[]
        line.append(local_star1)
        line.append(local)
        line.append(local_end1)
        lines1.append(line)
    return lines1

def create_rout_line2():
    file_data = open("data_store.txt","w")
    for first_local in locals:
        first_line = []
        first_line.append(local_star1)
        first_line.append(first_local)
        first_line.append(local_end1)
        for sec_local in locals:
            if  sec_local == first_local:
                continue #跳过这个选择，去过的地方不用去了
            sec_line = []
            for data in first_line:
                sec_line.append(data)
            sec_line.append(sec_local)
            for thr_local in locals:
                if thr_local==first_local or thr_local==sec_local:
                    continue
                thr_line = []
                for data in sec_line:
                    thr_line.append(data)
                thr_line.append(thr_local)
                thr_line.append(local_end2)
                lines2.append(thr_line)
                for i in range(len(thr_line)-1):
                    file_data.write(thr_line[i]+" ")
                file_data.write(thr_line[-1]+"\n")



labels1 = ["changsha","chongqing"]
set1 = {}
labels2 = ["chongqing","xiamen","guangzhou","sanya","hangzhou","beihai"]
set2_car = {}
set2_air = {}
labels3 = "wuhan"
set3_car ={}
set3_air ={}

# routs =[]
# def get_data_store():



def get_list(datas,i):
    data = datas[i].strip()
    list = data.split(" ")
    set ={}
    for i in range(len(locals)):
        set[locals[i]] = list[i]
    return set

def get_sets():
    file = open("data.txt", "r")
    datas = file.readlines()
    for i in range(2):
        price_set =get_list(datas,i)
        set1[labels1[i]] = price_set
    for i in range(6):
        price_set = get_list(datas,i+2)
        set2_car[labels2[i]]=price_set
    set2_car["way"]="by car"
    for i in range(6):
        price_set = get_list(datas,i+8)
        set2_air[labels2[i]]=price_set
    set2_air["way"]="by air"
    price_set = get_list(datas,15)
    set3_car[labels3]=price_set
    set3_car["way"]="by car"
    price_set = get_list(datas,14)
    set3_air["way"]="by air"
    set3_air[labels3] =price_set

cases = []
def rout_price(local_list,index):

    sec_place = local_list[1]
    thr_place = local_list[3]
    for_place = local_list[4]
    price1 = []
    price1.append(set1[labels1[0]][sec_place])
    price1.append(set1[labels1[1]][sec_place])
    way1=[]
    way1.append("by air")
    way1.append("by car")
    list_set2=[set2_car,set2_air]
    list_set3=[set3_car,set3_air]
    for set2 in list_set2:
        price2=[]
        price2.extend(price1)
        way2 = []
        way2.extend(way1)
        price2.append(set2[labels2[0]][thr_place])
        way2.append(set2["way"])
        for set22 in list_set2:
            price3 =[]
            price3.extend(price2)
            way3 =[]
            way3.extend(way2)
            price3.append(set22[thr_place][for_place])
            # if (for_place =="guangzhou" and set22["way"]=="by car"):
            #     print "找到了"
            #     return
            way3.append(set22["way"])
            for set3 in list_set3:
                price4 = []
                price4.extend(price3)
                way4 = []
                way4.extend(way3)
                price4.append(set3[labels3][for_place])
                way4.append(set3["way"])
                if "/" in price4:
                    continue
                num_price = []
                for price in price4:
                    num_price.append(float(price))
                total_price=0
                for num in num_price:
                    total_price =total_price+num
                if (total_price>2000):
                    continue
                case = {}
                case["price_total"] = total_price
                case["rout"]=local_list
                case["price_detail"]=num_price
                case["way"]=way4
                cases.append(case)

    # return price_info,way_info

import  numpy as np
counts_info =[]
trans_way =[]
def get_counts_info():
    file_routs = open("data_store.txt", "r")
    routs = file_routs.readlines()
    file_routs.close()
    for i in range(len(routs)):
    # for rout in routs:
        rout = routs[i]
        rout = rout.strip()
        local_list =rout.split(" ")
        # price_info,way_info = rout_price(local_list,i)
        # counts_info.append(price_info)
        # trans_way.append(way_info)
        rout_price(local_list,i)

        # break
# min_price = 5000
# opt_rout =""

def get_min():
    if(len(counts_info)==0):
        print "please run get_counts_info() first!"
        return 0
    file_routs = open("data_store.txt", "r")
    routs = file_routs.readlines()
    file_routs.close()
    min_price = 5000
    min_i = 0
    min_j = 0
    for  i in range(len(counts_info)):
        rout = routs[i]
        prices = counts_info[i]
        for j in range(len(prices)):
            price = prices[j]
            total_price = price[5]
            if(total_price<min_price):
                min_price = total_price
                min_i= i
                min_j= j
                opt_rout = rout
                opt_prices = price
                opt_way = trans_way[min_i][min_j]
    return opt_rout,opt_prices,opt_way,min_i,min_j

# def get_all_case
def show_all_case():
    print len(cases)
    # for case in cases:
    #     print case
    sort_case = sorted(cases,key=lambda cases: cases['price_total'])
    print "_____________________________________________________________"
    for case in sort_case:
        print case



if __name__ =="__main__":
    create_rout_line2()
    get_sets()

    # get_data_store()
    # get_routs()
    get_counts_info()
    print len(counts_info)
    show_all_case()

    # rout="changsha hangzhou chongqing beihai guangzhou wuhan"
    # local_list =rout.split(" ")
    # cases = rout_price(local_list, 1)
    # print len(cases)
    # show_all_case()
    # rout,price,way,i,j = get_min()
    # print rout
    # print price
    # print way
    # print i,j



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import table_info as info
import xml.etree.ElementTree as ET

aliases = '      <aliases enabled=\'yes\' />\n'
dimension = ['      <column caption=\''
            ,'\' datatype=\'string\' name=\''
            ,'\' role=\'dimension\' type=\'nominal\' />']
measure = ['      <column caption=\''
          ,'\' datatype=\'real\' name=\''
          ,'\' role=\'measure\' type=\'quantitative\' />']

# Tableauテーブル名取得
def getTableName(root):
    for t in root.iter('datasource'):
        table_name = t.get('caption').split()
    return table_name[0]

# Tableauカラム名称取得
def getColumnName(root):
    twb_key = []
    for k in root.iter('local-name'):
        twb_key.append(k.text)
    return twb_key

# 日本語化カラム名称取得
def getColumnNameJP():
    twb_value = list(info.table_info[table_name]['columns_name'].values())
    return twb_value

# xml挿入レコードの生成(ディメンション)
def xmlRecordsD(twb_value):
    for n in range(len(twb_key)):
        record = dimension[0] + twb_value[n] + dimension[1] + twb_key[n] + dimension[2] + '\n'
        output_data.writelines(record)
        print(record)

# xml挿入レコードの生成(メジャー)
# def xmlRecordsM():
#     for n in range(len(twb_key)):
#         record = measure[0] + twb_value[n] + measure[1] + twb_key[n] + measure[2]
#         print(record)

# .twbファイルレコードの読書き
def recordsIO():
    for line in input_data:
        if '</connection>' in line:
            output_data.writelines(line)
            print(line)
            output_data.write(aliases)
            print(aliases)
            twb_value = getColumnNameJP()
            xmlRecordsD(twb_value)
        else:
            output_data.writelines(line)
            print(line)

if __name__ == '__main__':
    input_data = open("BEFORE.twb", "r")
    output_data = open("AFTER.twb", "w")
    tree = ET.parse('比較用変更前.twb')
    root = tree.getroot()
    table_name = getTableName(root)
    twb_key = getColumnName(root)
    recordsIO()
    input_data.close()
    output_data.close()


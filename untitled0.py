#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:13:19 2019

@author: s-ushikubo

refs: https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200521&tstat=000001011777&cycle=0&tclass1=000001094741
"""

import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("./dataset/c01.csv", encoding='cp932')
    print(df.columns[0])
    df_s = df.sort_values("都道府県コード")
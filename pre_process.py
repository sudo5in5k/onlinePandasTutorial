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
    column_list = list(df.columns)
    print(column_list)  # columnを取得する

    df_s = df.sort_values("都道府県コード")  # ソート
    print(type(df_s.columns))

    """インデックス"""
    index = df_s.index  # インデックス
    df_s = df_s.reset_index(drop=True)  # Falseでindexが中に含まれる
    print(df_s.index)

    print(df_s.head)  # 最初だけ表示する、重いデータに対してよく使う

    """値抽出の仕方"""
    print(type(df_s.values[0]))

    prefecture_code_series = df_s['都道府県コード']
    print(prefecture_code_series)  # 直接column nameで指定してseries型で返す

    print(df_s.values[0][1])
    print(prefecture_code_series[0])

    # at, iat: 単独の要素の値
    print(df_s.at[0, r"都道府県コード"])  # index & column name
    print(df_s.iat[0, 1])  # num and num

    # loc, iloc: 単独及び複数の要素の値
    # speed: at iat > loc, iloc
    print(df_s.loc[0, r"都道府県コード"])
    print(df_s.loc[:, ::2])
    print(df_s.iloc[0, 1])

    """"""

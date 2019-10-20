#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:13:19 2019

@author: ussy
"""

import pandas as pd
import numpy as np

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
    # print(type(df_s.values[0]))
    #
    # prefecture_code_series = df_s['都道府県コード']
    # print(prefecture_code_series)  # 直接column nameで指定してseries型で返す
    #
    # print(df_s.values[0][1])
    # print(prefecture_code_series[0])
    #
    # # at, iat: 単独の要素の値
    # print(df_s.at[0, r"都道府県コード"])  # index & column name
    # print(df_s.iat[0, 1])  # num and num
    #
    # # loc, iloc: 単独及び複数の要素の値
    # # speed: at iat > loc, iloc
    # print(df_s.loc["0":"1", ::4])  # slice
    # print(df_s.loc[::, "都道府県コード":"元号"])  # slice

    """"""

    """欠損値の扱い"""
    # 削除
    df_d = df_s.dropna(how='all', axis=1)
    print(df_d)

    print(df_s.dropna(subset=['注']))

    # 一括で置き換え
    df_r = df_s.replace('-', np.nan)
    print(df_r)

    # 指定した列を指定した値に置き換え
    df_cr = df_r.fillna({"人口（総数）": "hoge", "人口（男）": np.nan, "人口（女）": np.nan})
    print(df_cr)

    # 欠損値を0で補完
    df_0 = df_r.fillna(0)
    print(df_0)
    

    """"""



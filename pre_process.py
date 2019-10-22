#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:13:19 2019

@author: ussy
"""

import numpy as np
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
    print(df_s.loc["0":"1", ::4])  # slice
    print(df_s.loc[::, "都道府県コード":"元号"])  # slice
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
    df_cr = df_r.fillna({"人口（総数）": "hoge", "人口（男）": 0, "人口（女）": 0})
    print(df_cr)

    # 欠損値を0で補完
    df_0 = df_cr.fillna(0)
    print(df_0)
    """"""

    """条件抽出"""
    df_tokyo = df_0[df_0[r"都道府県名"] == "東京都"]  # ブールインデックス
    df_tokyo = df_0.query("都道府県コード == '13'")
    df_kyoto = df_0[df_0["都道府県名"].isin(["京都府"])]
    print(df_kyoto)
    """"""

    """統計量算出"""
    # 基本統計量
    print(df_0.dtypes)
    df_men = df_0["人口（男）"].astype(float)
    print(df_men.describe())
    print(df_men.max())
    print(df_men.min())
    print(df_men.count())
    print(df_men.std())
    print(df_men.mean())

    # 相関
    df_women = df_0["人口（女）"].astype(int)
    print(df_men.corr(df_women))
    """"""

    """特徴抽出"""
    # カテゴリ化
    df_tokyo = df_tokyo.sort_values("西暦（年）")


    def era_to_binary(x):
        return 1 if x == "平成" else 0


    df_tokyo["元号"] = df_tokyo["元号"].apply(lambda e: 1 if e == "平成" else 0)
    print(df_tokyo)

    # 四則演算
    df_tokyo["男女比"] = df_men / df_tokyo["人口（女）"].astype(float)
    df_tokyo["平均差_男"] = df_men.mean() - df_men
    df_tokyo["log_men"] = np.log1p(df_men)
    print(df_tokyo)

    # one-hot-encoding
    print(pd.get_dummies(prefecture_code_series))

    # binning

    # 最大値・最小値からのアプローチ
    bin_quad, bins = pd.cut(df_tokyo["人口（男）"].astype(float), 4, retbins=True, labels=False)  # 最大値と最小値の間でn分割, 区間も同時に取得
    print(bin_quad, bins)
    bin_quad_label = pd.cut(df_tokyo["人口（男）"].astype(float), 4, retbins=True, labels=False)  # ラベリング化
    print(bin_quad_label)
    bin_quad_original_label = pd.cut(df_tokyo["人口（男）"].astype(float), 4, retbins=True,
                                     labels=['S', 'M', 'L', 'XL'])  # ラベル付きの分割
    print(bin_quad_original_label)

    # 任意の境界でのアプローチ
    twenty_first_century = pd.cut(df_tokyo["西暦（年）"].astype(float), [0, 2000, 2100], retbins=True)
    print(twenty_first_century)

    # 等分割
    bin_quartile, bins = pd.qcut(df_tokyo["人口（男）"].astype(float), 4, retbins=True, labels=False,
                                 duplicates='drop')  # 最大値と最小値の間でn分割, 区間も同時に取得
    print(bin_quartile, bins)
    """"""

    # 書き出し
    df_tokyo.to_csv('tokyo.csv', header=True, index=False, encoding='utf-8')

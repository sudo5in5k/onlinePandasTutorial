# 今回使用したデータのダウンロード先
https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200521&tstat=000001011777&cycle=0&tclass1=000001094741

# Pandasのドキュメント
https://pandas.pydata.org/pandas-docs/stable/index.html

# one-hot-encoding

* one-hot
    * あるカラムだけ1、他が0のベクトルのことを指す
    * ダミー変数とも言う
    
one-hot-encoding = one-hotなベクトルの特徴量エンジニアリング

例)

`行列A`

|Skill|
|----|
|Python|
|Java|
|Python|
|Ruby|

数値変換したい


`行列B`

|Skill|
|----|
|1|
|2|
|1|
|3|

学習にかけづらい

`行列C`

|Skill|Python|Java|Ruby|
|----|----|----|----|
|Python|1|0|0|
|Java|0|1|0|
|Python|1|0|0|
|Ruby|0|0|1|


* メリット
    * 回帰モデルや機械学習での精度向上が見込める
    
* デメリット
    * 大量のベクトルを生成することになるので、メモリ使用量・計算量が爆発的に増えていく
    
## binning
binning = 連続値を境界を使って離散値に変換する処理

例)
* 20代, 30代, 40代

## 応用
メモリ問題

基本的にはガベージコレクションでなんとかしてくれるが、実際にデータ分析をする際にメモリ使用量が気になる => 即時的にメモリ解放を行う必要あり

* 読み込みを最低限にする
```python
import pandas as pd

df_100_interval = pd.read_csv('input.csv', chunksize=100)  # 100行だけ読み込み
next(df_100_interval)  # 100-200
```

* 読み込みを最適化する
    * [Dask](https://docs.dask.org/en/latest/)
    
```python
import dask.dataframe as dd

df = dd.read_csv('*.csv')
```

* いらないものを即座に消す
    * `del df`

* ファイルにダンプする
    * オーバーヘッドが欠点
    
*  破壊的代入

```python
big_data = [func(x) for x in big_data]

for i, e in enumerate(big_data):
    big_data[i] = func(e)

```

* 64bit型を使わない
    * float32 (intも同様)
        * float64よりも1/2のメモリ消費量で済む
        * 一方正確な数値表現ではなくなる
            * だが、大抵の機械学習では必要ない

```python
import numpy as np

np.float32
```

* pandasの場合、デフォルトが64のためあらかじめ指定しておく必要がある

```python
import pandas as pd

# example
dtype = {'id': 'int16', 'date': 'int32', 'value': 'float32'}
df = pd.read_csv('input.csv', dtype=dtype)

df['value'] = df['value'].astype('float32')

```

メモリ溢れはないが、pythonでのfor文で配列/dataFrame処理はとても重くなりがち

## 特徴量生成
機械学習寄り
* [scikit-learn.preprocessing](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing)
* [featuretools](https://docs.featuretools.com/#)
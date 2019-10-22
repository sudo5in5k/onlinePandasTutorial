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

## 特徴量生成
機械学習寄り
* [scikit-learn.preprocessing](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing)
* [featuretools](https://docs.featuretools.com/#)
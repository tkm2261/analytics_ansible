# 分析環境Ansible

分析環境構築に必要そうなものをとりあえずまとめました。

方針としては、全部入りを目指しているので、必要と思うものはバンバン入れて下さい。

# 動作環境

* Python2系のみ
* Ubuntu 15.04で動作確認済

# 構築環境概要

Infrastructure as Codeなんでここには概要のみ

### Python

* Anaconda - バージョンはgroup_varsで管理
* xgboost
* jupyter notebook が8888で自動起動

### R

最新版をダウンロード。

* R
* RStudio - 8787で自動起動

### クラウド

* AWS - group_varsにkeyが記載できるので,awsコマンドが使えます
* GCP - 一応aptでSDK入れたが、gcloud init やgcloud auth loginなどインタラクティブが多いのでアカウント自動設定は未実装。改善求む

# 使用方法

分析環境は都度マシンが変わるのでinventryファイルは用意せず、コマンドライン指定を想定

最も基本的な使用方法は下記。-i 以下の**ダブルクオート**と**末尾カンマ**は必須なので注意

```
# ansible-playbook -i "[IPアドレス]," -u [ユーザ名] -k site.yml
# 秘密鍵指定は --private-key オプション
ansible-playbook -i "192.168.33.10," -u vagrant -k site.yml

# 時間掛かるのでローカル(分析サーバ上で)実行したい場合は以下
ansible-playbook -i "localhost," --connection=local site.yml
```

Anacondaインストールに非常に時間かかるので、PythonのみRのみのインストールにも対応

詳細はsite.ymlのtagsを参照

```
# Pythonのみ
ansible-playbook -i "192.168.33.10," -u vagrant -k site.yml --tags python_only 

# Rのみ
ansible-playbook -i "192.168.33.10," -u vagrant -k site.yml --tags r_only 
```

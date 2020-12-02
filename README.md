# Django3系の技術検証用のベースリポジトリ

## 概要
本リポジトリはDjango3系の技術検証用のベースリポジトリです。
以下の手順でリポジトリをコピーして使ってください。
## リポジトリをコピーする手順

・リポジトリのベアクローンを作成する。
```shell
$ git clone --bare https://github.com/delhi09/django3_demo_base.git
```

・新しいリポジトリをミラープッシュする。
```shell
$ cd django3_demo_base.git
※ 先にGitHub上でリポジトリを作成しておくこと
$ git push --mirror https://github.com/delhi09/newrepo.git
```

・先ほど作成した一時ローカルリポジトリを削除する。
```shell
$ cd ..
$ rm -rf django3_demo_base.git
```
## 実行手順

・MySQLのdockerコンテナを起動する。
```shell
$ docker-compose up -d
```

・アプリケーションを起動する。
```shell
$ cd django3_demo
$ python manage.py runserver
```
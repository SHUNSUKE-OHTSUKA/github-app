# github-app

## 概要

* GitHua App を用いて認証を行い、ローカルから GitHubActions(workflow) を実行します。
* GitHubActions(workflow) は再帰ワークフローを指定します。
    * 参考 : https://zenn.dev/dzeyelid/articles/fc4bd999fbccd8

## 動作環境

* Python 3.11.4

## 実行方法

### ローカル

1. ローカルにレポジトリをクローンする
1. 依存パッケージをインストールする
    ```
    pip inatall -r requirements.txt
    ```
1. .envファイルに環境変数を設定する
    ```
    cp -p .env.sample .env
    ```
1. スクリプトを実行する
    ```
    python localhost.py
    ```
    
    参考 : 実行Log
    ```
    INFO:root:token_header : {'Authorization': 'token ghs_xxxx', 'Accept': 'application/vnd.github.inertia-preview+json'}
    INFO:root:status_code : 204
    ```

### GitHub

1. Actionsを実行する

    * https://github.com/SHUNSUKE-OHTSUKA/github-app/actions/workflows/trigger-workflow.yml

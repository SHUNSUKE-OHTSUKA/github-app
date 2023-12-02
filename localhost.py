from github.client import App
import os

import logging
logging.basicConfig(level=logging.INFO)

# .envファイルから環境変数を読み込む
from dotenv import load_dotenv
load_dotenv()

# 環境変数から設定を読み込む
app_id = os.getenv('APP_ID')
org = os.getenv('ORG')
private_key = os.getenv('PRIVATE_KEY')

def main():
    app = App(
        app_id = app_id,
        org = org,
        private_key = private_key
    )
    
    # https://github.com/SHUNSUKE-OHTSUKA/github-app/actions/workflows/starter-workflow.yml
    response = app.workflow(
        repo='github-app',
        ref = 'main',
        inputs= {},
        workflow_id='77335733',
    )
    logging.info('status_code : ' + str(response.status_code))

if __name__ == '__main__':
    main()
from github.client import App
import os

import logging
logging.basicConfig(level=logging.INFO)

# .envファイルから環境変数を読み込む
from dotenv import load_dotenv
load_dotenv()

# 環境変数から設定を読み込む
app_id = os.getenv('APP_ID')
installation_id = os.getenv('INSTALLATION_ID')
pem = os.getenv('PEM')

def main():
    app = App(app_id, installation_id, pem)
    
    # https://github.com/SHUNSUKE-OHTSUKA/github-app/actions/workflows/starter-workflow.yml
    response = app.workflow(
        owner='SHUNSUKE-OHTSUKA',
        repo='github-app',
        ref = 'main',
        inputs= {},
        workflow_id='77335733',
    )
    logging.info('status_code : ' + str(response.status_code))

if __name__ == '__main__':
    main()
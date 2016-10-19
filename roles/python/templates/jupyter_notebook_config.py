
c = get_config()

# matplotlibで描画したものがnotebook上で表示できるようにする
c.IPKernelApp.pylab = 'inline'
# 全てのIPから接続を許可
c.NotebookApp.ip = '*'
# IPython notebookのログインパスワード
#c.NotebookApp.password = 'sha1:<ハッシュ化されたパスワード>'
# 起動時にブラウザを起動させるかの設定(デフォルトは起動させる)
c.NotebookApp.open_browser = False
# ポート指定(デフォルトは8888)
c.NotebookApp.port = 8888

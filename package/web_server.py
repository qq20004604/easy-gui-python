from flask import Flask
import os
from route.route import init_route
from route.debug import init_debug_route
from package.utils.find_root_path import find_root_path

app = Flask(__name__)

debug = False
# pycharm在本地调试时，这个值通常会默认添加并且为1
if os.environ.get("debug") == 'true' or os.environ['PYTHONUNBUFFERED'] == '1':
    debug = True

# 在上级目录中查找包含html目录的路径
html_dir = os.path.join(find_root_path(), 'html')
print(f"html_dir: {html_dir}")

if html_dir:
    app.static_folder = html_dir
else:
    raise ValueError("No 'html' directory found in the parent directories.")

init_route(app)

if debug:
    init_debug_route(app)


def run_flask(port=9000):
    print(f"服务器启动成功，debug={debug}")
    # 测试环境下，可以从浏览器窗口打开页面。而生产环境下，只能从webview窗口访问
    if debug:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(port=port)


if __name__ == '__main__':
    run_flask()

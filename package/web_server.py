from flask import Flask
import os
from route.route import init_route
from route.debug import init_debug_route

app = Flask(__name__)

# pycharm在本地调试时，这个值通常会默认添加并且为1
if os.environ.get("debug") == 'true' or os.environ['PYTHONUNBUFFERED'] == '1':
    debug = True


def find_html_dir(current_dir):
    while current_dir != '/':
        html_dir = os.path.join(current_dir, 'html')
        if os.path.exists(html_dir) and os.path.isdir(html_dir):
            return html_dir
        current_dir = os.path.dirname(current_dir)
    return None


# 获取当前工程根目录的绝对路径
root_dir = os.path.abspath(os.path.dirname(__file__))
# 如果这里指向了package目录，那么则取package目录的上一级目录
if os.path.basename(root_dir) == 'package':
    root_dir = os.path.dirname(root_dir)

# 在上级目录中查找包含html目录的路径
html_dir = find_html_dir(root_dir)
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

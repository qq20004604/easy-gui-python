import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import web_server
import os, random, socket
import multiprocessing

# 判断当前是否为测试模式。方法是设置环境变量【PYTHONUNBUFFERED=1】或者【debug=true】
if os.environ['PYTHONUNBUFFERED'] == '1':
    os.environ['debug'] = "true"


# 打开一个webview的gui界面
class Webview(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("WebView Example")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        webview = QWebEngineView()
        layout.addWidget(webview)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        url = QUrl(self.run_flash())
        webview.setUrl(url)

        self.closeEvent = self.handle_close

    def run_flash(self):
        port = self.get_free_port()
        # port = run_flask()

        app_process = multiprocessing.Process(target=web_server.run_flask, kwargs={'port': port})
        app_process.start()
        url = f"http://127.0.0.1:{port}/web/test.html"
        print(f"url: {url}")
        return url

    def get_free_port(self):
        if os.environ.get("debug") == 'true':
            port = 9000
        else:
            # 随机生成30000到40000之间未被占用的端口
            while True:
                port = random.randint(30000, 40000)
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.bind(('127.0.0.1', port))
                    s.close()
                    break
                except socket.error:
                    continue
        return port

    def handle_close(self, event):
        # 在窗口关闭事件发生时，终止所有进程并退出应用程序
        self.terminate_all_processes()
        event.accept()

    def terminate_all_processes(self):
        # 终止所有进程
        for process in multiprocessing.active_children():
            process.terminate()
            process.join()


def run():
    app = QApplication(sys.argv)
    window = Webview()
    window.show()
    sys.exit(app.exec())
    print('exit')


if __name__ == "__main__":
    run()
    # app = QApplication(sys.argv)
    # window = Webview()
    # window.show()
    # sys.exit(app.exec())

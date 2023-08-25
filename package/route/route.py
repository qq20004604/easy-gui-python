from package.service.update_files import update_files
from flask import jsonify


def init_route(app):
    # 定义路由，将/web/* 映射到静态文件
    @app.route('/web/<path:filename>')
    def serve_static(filename):
        return app.send_static_file(filename)

    # 更新web文件
    @app.route('/updateWebFiles')
    def update_web_files():
        msg = update_files()
        if len(msg) == 0:
            return jsonify({"code": 200, "msg": "更新成功"})
        else:
            return jsonify({"code": 0, "msg": msg})

def init_route(app):
    # 定义路由，将/web/* 映射到静态文件
    @app.route('/web/<path:filename>')
    def serve_static(filename):
        return app.send_static_file(filename)

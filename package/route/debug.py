def init_debug_route(app):
    # 专门处理 /web 路径的路由
    if app.debug:
        @app.route('/web/')
        def serve_test_html():
            return app.send_static_file('test.html')

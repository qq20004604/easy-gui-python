import os

# 工程根目录，获取一次之后，直接返回
ROOT_PATH = ""
ERROR = None


# 使用场景，有些时候，我们直接执行某个py文件，但这个py文件在项目子目录里，因此我们需要获取项目的根目录，方便进行一些文件操作处理
# 找到项目根目录，并返回根目录的路径（pwd）
def find_root_path():
    global ROOT_PATH
    global ERROR

    # 如果当前有根目录，则直接返回根目录
    if len(ROOT_PATH) > 0:
        return ROOT_PATH

    # 如果有报错信息，直接抛错
    if ERROR is not None:
        raise ValueError(ERROR)

    # 根目录标识符是：有 LICENSE 文件和html文件夹
    # 获取当前目录
    root_dir = os.path.abspath(os.path.dirname(__file__))

    # 如果当前目录的绝对路径，不是 "/"，这个是指系统的根目录
    while root_dir != '/':
        html_dir = os.path.join(root_dir, 'html')
        license_path = os.path.join(root_dir, 'LICENSE')
        # 判断当前目录下有没有html文件夹和 LICENSE 文件
        if os.path.exists(html_dir) and os.path.isdir(html_dir) and os.path.exists(license_path):
            # 如果有，则返回路径
            ROOT_PATH = root_dir
            return ROOT_PATH
        root_dir = os.path.dirname(root_dir)

    # 到根目录下，再判断最后一次
    if root_dir == '/':
        html_dir = os.path.join(root_dir, 'html')
        license_path = os.path.join(root_dir, 'LICENSE')
        # 判断当前目录下有没有html文件夹和 LICENSE 文件
        if os.path.exists(html_dir) and os.path.isdir(html_dir) and os.path.exists(license_path):
            # 如果有，则返回路径
            ROOT_PATH = root_dir
            return ROOT_PATH

    ERROR = "未找到项目根目录。请在项目根目录下，添加html文件夹和LICENSE文件"
    raise ValueError(ERROR)

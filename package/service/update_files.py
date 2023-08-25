import os
import requests
import shutil
from zipfile import ZipFile
from package.utils.find_root_path import find_root_path


def update_files():
    # 这个是前端接口调用。当检查到当前web文件的版本不是最新版时，提示用户是否需要更新。如果用户确认更新，则调用本接口
    # 本接口会去获取远程的文件列表，并将这些文件更新到本地。
    url = "http://lovelovewall.com/ttt/abc.zip"
    file_name = "abc.zip"
    response = requests.get(url)

    # 检查请求状态码是否为200 (成功)
    if response.status_code == 200:
        try:
            root = find_root_path()
            filepath = os.path.join(root, 'html', file_name)
            # 将文件保存到当前目录
            with open(filepath, 'wb') as file:
                file.write(response.content)
            print(f"File '{file_name}' downloaded successfully.")
        except IOError as e:
            errmsg = f"无法打开文件 {e}"
            print(errmsg)
            return errmsg

        # 解压缩文件到html文件夹
        with ZipFile(filepath, 'r') as zip_ref:
            # os.makedirs('html', exist_ok=True)  # 创建html文件夹
            zip_ref.extractall(os.path.join(root, 'html'))
        print("文件夹解压成功")
        # 删除zip文件，以及可能的mac解压缩文件夹
        if os.path.exists(filepath):
            os.remove(filepath)
            mac_extra_path = os.path.join(root, 'html', '__MACOSX')
            if os.path.exists(mac_extra_path) and os.path.isdir(mac_extra_path):
                shutil.rmtree(mac_extra_path)
            print("临时文件已删除")

        return ""
    else:
        errmsg = "文件下载失败。"
        print(errmsg)
        return errmsg

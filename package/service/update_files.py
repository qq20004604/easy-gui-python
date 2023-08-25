import os
import requests
from zipfile import ZipFile


def update_files():
    # 这个是前端接口调用。当检查到当前web文件的版本不是最新版时，提示用户是否需要更新。如果用户确认更新，则调用本接口
    # 本接口会去获取远程的文件列表，并将这些文件更新到本地。
    url = "http://lovelovewall.com/ttt/abc.zip"
    file_name = "abc.zip"
    response = requests.get(url)

    # 检查请求状态码是否为200 (成功)
    if response.status_code == 200:
        try:
            # 将文件保存到当前目录
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"File '{file_name}' downloaded successfully.")
        except IOError as e:
            errmsg = f"无法打开文件 {e}"
            print(errmsg)
            return errmsg

        # 解压缩文件到html文件夹
        with ZipFile(file_name, 'r') as zip_ref:
            os.makedirs('html', exist_ok=True)  # 创建html文件夹
            zip_ref.extractall('html')
        print("ZIP file extracted to 'html' folder.")
    else:
        errmsg = "文件下载失败。"
        print(errmsg)
        return errmsg

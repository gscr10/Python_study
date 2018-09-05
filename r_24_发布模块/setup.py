from distutils.core import setup

# 多值的字典参数
setup(name="package",  # 包名
      version="1.0",  # 版本
      description="发送接收",  # 描述信息
      long_description="完整的发送接收模块",  # 完整的描述信息
      author="111",  # 作者
      author_email="1111111@gmail.com",  # 作者邮箱
      url="www.123.com",  # 主页
      py_modules=["package.send_message",
                  "package.receive_message"])

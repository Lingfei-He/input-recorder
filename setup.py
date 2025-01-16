from setuptools import setup, find_packages
 
setup(
    name="input_recorder",  # 包名
    version="1.0.0",  # 版本号
    author="Lingfei, He",  # 作者名字
    author_email="lingfei@tju.edu.cn",  # 作者邮箱
    description="A simple python tool to record and replay user's input operations.",  # 描述
    # long_description="A longer description of this project",  # 详细描述
    url="https://github.com/Lingfei-He/input_recorder",  # 主页 URL
    packages=find_packages(),  # 包列表
    install_requires=[],  # 运行时依赖关系
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        # "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],  # 分类标签
    include_package_data=True
)
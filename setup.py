from setuptools import setup

setup(
    name="tiny-todo-jasonkingmax",
    version="0.1.0",
    py_modules=["todo_cli"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "tiny-todo=todo_cli:main",
        ],
    },
    author="jasonkingmax",
    description="一个简单的命令行待办工具",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)

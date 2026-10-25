# Tiny TODO

一个简单的 Python 命令行待办工具，用于学习项目组织、版本管理与开源发布。

## 已实现

- 添加待办事项
- 查看列表与完成状态
- 按列表编号标记完成
- 将数据保存到本机用户目录下的 `.tiny-todo.json`

## 从源码开始

需要 Python 3.7 或更新版本（依据当前 setup.py）。建议使用仍受支持的 Python 3 版本。

```bash
git clone https://github.com/jasonkingmax/tiny-todo-demo.git
cd tiny-todo-demo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Windows 激活虚拟环境使用 `.venv\Scripts\activate`。

## 使用

```bash
tiny-todo add 学习 Python
tiny-todo list
tiny-todo done 1
```

也可以不安装，直接运行：

```bash
python3 todo_cli.py add 学习 Python
python3 todo_cli.py list
python3 todo_cli.py done 1
```

任务编号以列表显示为准；`done` 后请填写数字。

## 数据与限制

- 数据保存在 `~/.tiny-todo.json`，不在仓库目录中；卸载工具不会自动删除该文件。
- 当前为本地明文 JSON 存储，无加密、云同步、多用户或并发写入保护。
- 当前没有删除、编辑、到期提醒功能。
- 非数字任务编号或损坏的 JSON 文件可能导致报错；相关错误处理待完善。
- 本文安装与命令依据源码整理，本次文档更新未执行运行测试；未核验 PyPI 发布状态。

## 个性化编辑

- **作者介绍：**【待填写】
- **运行截图或终端演示：**【待补充】
- **你的使用场景：**【待填写】
- **验证环境与结果：**【实际运行后填写 Python 版本、系统及结果】

## 后续计划

- [ ] 完善输入校验与错误提示
- [ ] 添加删除和编辑任务
- [ ] 添加有意义的自动化测试
- [ ] 核验打包与发布流程

以上为计划，不代表已经实现。

## 许可证

[MIT License](LICENSE)

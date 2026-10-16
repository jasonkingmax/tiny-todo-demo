"""Tiny TODO - 简单的命令行待办工具"""
import json
import os
from pathlib import Path

TODO_FILE = Path.home() / ".tiny-todo.json"

def load_todos():
    if TODO_FILE.exists():
        with open(TODO_FILE) as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def add_task(text):
    todos = load_todos()
    todos.append({"text": text, "done": False})
    save_todos(todos)
    print(f"✓ 已添加: {text}")

def list_tasks():
    todos = load_todos()
    if not todos:
        print("暂无待办事项")
        return
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else "○"
        print(f"{i}. [{status}] {todo['text']}")

def complete_task(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
        print(f"✓ 已完成: {todos[index - 1]['text']}")
    else:
        print("错误: 无效的任务编号")

def main():
    import sys
    if len(sys.argv) < 2:
        print("用法:")
        print("  tiny-todo add <任务内容>")
        print("  tiny-todo list")
        print("  tiny-todo done <任务编号>")
        return
    
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done" and len(sys.argv) > 2:
        complete_task(int(sys.argv[2]))
    else:
        print("未知命令")

if __name__ == "__main__":
    main()

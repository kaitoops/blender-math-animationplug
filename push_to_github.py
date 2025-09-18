#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GitHub 推送脚本
此脚本可以帮助您将更改推送到 GitHub 仓库
"""

import os
import subprocess
import sys

def run_command(command):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def push_to_github():
    """推送更改到 GitHub"""
    # 切换到项目目录
    project_dir = r"g:\GitHubcodecollection\blender-math-animationplug"
    os.chdir(project_dir)
    
    print("正在添加所有更改到暂存区...")
    code, stdout, stderr = run_command("git add .")
    if code != 0:
        print(f"错误: {stderr}")
        return False
    
    # 获取提交信息
    commit_message = input("请输入提交信息: ")
    if not commit_message:
        commit_message = "Update files"
    
    print(f"正在提交更改: {commit_message}")
    code, stdout, stderr = run_command(f'git commit -m "{commit_message}"')
    if code != 0:
        if "nothing to commit" in stderr:
            print("没有新的更改需要提交")
        else:
            print(f"提交错误: {stderr}")
            return False
    
    print("正在推送到 GitHub...")
    code, stdout, stderr = run_command("git push origin main")
    if code != 0:
        print(f"推送错误: {stderr}")
        return False
    
    print("推送成功!")
    return True

if __name__ == "__main__":
    try:
        push_to_github()
    except KeyboardInterrupt:
        print("\n操作已取消")
    except Exception as e:
        print(f"发生错误: {e}")
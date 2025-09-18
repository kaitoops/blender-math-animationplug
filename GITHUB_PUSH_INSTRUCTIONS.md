# GitHub 推送操作指南

## 1. SSH 密钥信息

SSH 密钥已生成并保存在您的用户目录中：
- 私钥位置：`C:\Users\WIN10\.ssh\id_rsa`
- 公钥位置：`C:\Users\WIN10\.ssh\id_rsa.pub`

## 2. SSH 配置

SSH 配置文件位于：`C:\Users\WIN10\.ssh\config`
配置内容：
```
Host github.com
  HostName ssh.github.com
  Port 443
  User git
  IdentityFile ~/.ssh/id_rsa
```

## 3. 推送步骤

要将更改推送到 GitHub，请按以下步骤操作：

1. 打开终端或命令提示符
2. 切换到项目目录：
   ```
   cd "g:\GitHubcodecollection\blender-math-animationplug"
   ```

3. 添加所有更改到暂存区：
   ```
   git add .
   ```

4. 提交更改：
   ```
   git commit -m "您的提交信息"
   ```

5. 推送到 GitHub：
   ```
   git push origin main
   ```

## 4. 注意事项

- 如果您在新环境中工作，可能需要重新配置 SSH 密钥
- 确保您的 GitHub 账户已添加了公钥
- 如果遇到连接问题，请检查防火墙设置

## 5. 故障排除

如果推送失败，请尝试以下操作：
1. 测试 SSH 连接：
   ```
   ssh -T git@github.com
   ```
2. 检查 SSH 配置文件是否正确
3. 确认 GitHub 账户中的 SSH 密钥是否有效
### 连接记录
Linux SSH的连接记录通常会被记录在/var/log/auth.log文件中。该文件包含了系统身份验证和授权的相关信息，例如用户登录、SSH连接等。您可以使用以下命令查看SSH连接记录：<br />sudo grep sshd /var/log/auth.log<br />如果您想查看最近的SSH连接记录，可以使用以下命令：<br />sudo tail -f /var/log/auth.log | grep sshd<br />这将显示实时日志文件中所有与sshd相关的行。

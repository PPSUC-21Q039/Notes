# 知识点
[ARM64 vs X64: What’s the Difference?](https://www.partitionwizard.com/partitionmanager/arm64-vs-x64.html)<br />AWS日志查询<br />AWS CLI的使用
#### 相关命令
```shell
aws s3api list-buckets   # To list the buckets
aws s3 sync s3://flaws2-logs .   # 将s3://flaws2-logs导出到本地
find AWSLogs -type f -exec gunzip "{}" \;  # 寻找在AWSLogs中的文件并执行gunzip解压
```
```python
find AWSLogs -type f -exec jq . "{}" \; | grep eventTime | sort | uniq

"""
"find AWSLogs -type f"：这将在 "AWSLogs" 目录及其子目录中搜索所有文件。
"-exec jq . "{}" ;"：对于每个文件，这会运行 "jq" 命令来格式化输出 JSON 内容。"{}" 是一个占位符，将被替换为正在处理的文件名。反斜杠是为了将分号转义，使其作为参数传递给 "find"，而不是被 Shell 解释。
"| grep eventTime"：这将把 "jq" 的输出传递给 "grep"，以过滤出仅包含字符串 "eventTime" 的行。
"| sort"：这将对行按字母顺序排序。
"| uniq"：这将去除任何重复的行。
"""
```
```python
grep -r -F '"eventTime":"2018-11-28T22:31:59Z"' AWSLogs

"""
在这个命令中，
使用了 "grep" 命令，
指定了参数 "-r" 表示递归搜索子目录，
并且使用了 "-F" 参数表示按照字符串字面值进行匹配。
具体来说，这个命令会在 "AWSLogs" 目录及其子目录中递归搜索，
查找所有包含字符串 '"eventTime":"2018-11-28T22:31:59Z"' 的行，
并将它们输出到终端。
"""
```
```python
jq . example.json  # 解析example.json并输出结果
```
```python
whois '34.234.236.212' | grep 'Organization' -B 5 -A 5

"""
这个命令会查询 IP 地址 "34.234.236.212" 的 WHOIS 信息，
并将输出结果通过管道传递给 "grep" 命令，
指定了参数 "Organization" 表示过滤出包含字符串 "Organization" 的行，
同时使用了 "-B 5" 和 "-A 5" 参数表示输出包含匹配行的前面和后面各 5 行。
"""
```
# 工具

- [AWS-CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [jq](https://stedolan.github.io/jq/download/)    一款解析JSON文件的命令行工具
# 思路
[CyberDefenders: Bucket](https://forensicskween.com/ctf/cyberdefenders/bucket/)



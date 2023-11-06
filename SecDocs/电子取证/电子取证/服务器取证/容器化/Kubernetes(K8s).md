# 教程
[Kubernetes教程](https://kuboard.cn/learning/)<br />[GitHub - guangzhengli/k8s-tutorials: k8s tutorials | k8s 教程](https://github.com/guangzhengli/k8s-tutorials)<br />[Kubernetes入门实验：概述 - 掘金](https://juejin.cn/post/6985383911438319652)

# 概述
Kubernetes 是一个可移植、可扩展的开源平台，用于管理容器化的工作负载和服务，可促进声明式配置和自动化。 Kubernetes 拥有一个庞大且快速增长的生态，其服务、支持和工具的使用范围相当广泛。Kubernetes用于管理多容器集群。<br />Kubernetes 为你提供：

- **服务发现和负载均衡**

Kubernetes 可以使用 DNS 名称或自己的 IP 地址来暴露容器。 如果进入容器的流量很大， Kubernetes 可以负载均衡并分配网络流量，从而使部署稳定。

- **存储编排**

Kubernetes 允许你自动挂载你选择的存储系统，例如本地存储、公共云提供商等。

- **自动部署和回滚**

你可以使用 Kubernetes 描述已部署容器的所需状态， 它可以以受控的速率将实际状态更改为期望状态。 例如，你可以自动化 Kubernetes 来为你的部署创建新容器， 删除现有容器并将它们的所有资源用于新容器。

- **自动完成装箱计算**

你为 Kubernetes 提供许多节点组成的集群，在这个集群上运行容器化的任务。 你告诉 Kubernetes 每个容器需要多少 CPU 和内存 (RAM)。 Kubernetes 可以将这些容器按实际情况调度到你的节点上，以最佳方式利用你的资源。

- **自我修复**

Kubernetes 将重新启动失败的容器、替换容器、杀死不响应用户定义的运行状况检查的容器， 并且在准备好服务之前不将其通告给客户端。

- **密钥与配置管理**

Kubernetes 允许你存储和管理敏感信息，例如密码、OAuth 令牌和 ssh 密钥。 你可以在不重建容器镜像的情况下部署和更新密钥和应用程序配置，也无需在堆栈配置中暴露密钥。
# Kuboard安装（可视化管理工具）
[安装Kubernetes Dashboard](https://kuboard.cn/install/install-k8s-dashboard.html#%E8%AE%BF%E9%97%AE)<br />[吊炸天的Kubernetes微服务图形化管理工具：Kuboard，必须推荐给你！](https://zhuanlan.zhihu.com/p/369375227)
# Kuboard常用命令
[k8s（kubernetes） 常用命令-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1876774)<br />获取全局配置
```powershell
kubectl get configmap -n kube-system -o yaml
```

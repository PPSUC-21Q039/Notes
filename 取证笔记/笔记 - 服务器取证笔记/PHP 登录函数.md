<img src="img/PHP 登录函数.assets/image-20231231165429458.png" alt="image-20231231165429458" style="zoom:67%;" />

```php
// 用户信息验证
            $map = ['is_deleted' => '0', 'username' => $data['username']];
            $user = Db::name('SystemUser')->where($map)->order('id desc')->find();
            if (empty($user)) $this->error('登录账号或密码错误，请重新输入!');
            if ($user['password'] !== substr(md5($data['password']),3,-3)) {
                $this->error('登录账号或密码错误，请重新输入!');
            }
```

在这里是截取的 MD5 的第三位到-3位，例如 `ac98a61d8044be1ed3d19b2cfd` ，那么前面舍去了4个，后面舍去了4个，如果要解密的话可以截取中间16位来倒推MD5.

如果 CMD5 查不到，可以试试这个：https://www.somd5.com


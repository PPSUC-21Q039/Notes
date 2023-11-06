```python
<?php

highlight_file(__FILE__);
error_reporting(0);

$data=base64_decode($_GET['data']);
$host=$_GET['host'];
$port=$_GET['port'];

$fp=fsockopen($host,intval($port),$error,$errstr,30);
if(!$fp) {
    die();
}
else {
    fwrite($fp,$data);
    while(!feof($data))
    {
        echo fgets($fp,128);
    }
    fclose($fp);
}
```
这种形式也可以SSRF<br />可以看fsockopen的文档<br />[https://www.php.net/manual/en/function.fsockopen.php](https://www.php.net/manual/en/function.fsockopen.php)<br />有以下的示例
```python
Here's a function to just fetch the contents behind an URL.

<?php
function fetchURL( $url ) {
    $url_parsed = parse_url($url);
    $host = $url_parsed["host"];
    $port = $url_parsed["port"];
    if ($port==0)
        $port = 80;
    $path = $url_parsed["path"];
    if ($url_parsed["query"] != "")
        $path .= "?".$url_parsed["query"];

    $out = "GET $path HTTP/1.0\r\nHost: $host\r\n\r\n";

    $fp = fsockopen($host, $port, $errno, $errstr, 30);

    fwrite($fp, $out);
    $body = false;
    while (!feof($fp)) {
        $s = fgets($fp, 1024);
        if ( $body )
            $in .= $s;
        if ( $s == "\r\n" )
            $body = true;
    }
    
    fclose($fp);
    
    return $in;
}
?>
```
按照这个示例去请求/flag.php就可以获取flag了

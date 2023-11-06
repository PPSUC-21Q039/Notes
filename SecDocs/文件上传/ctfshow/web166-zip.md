# 知识点
# 思路
```python
<?php
error_reporting(0);

$file= $_GET['file'];
if(!isset($file)){
	die('文件不存在');
}

if(preg_match('/log|flag|data|input|file|compress|phar|http|https|ftp/', $file)){
	die('文件不存在');
}

if(check($file)){
	die('文件不存在!');
}else{
	include($file);
	header('Content-Type:application/x-zip-compressed');
}


function check($str){
	$ret = FALSE;
	$arrayName = array('ftp','file','/','http','https','phar','tmp','php','data','compress');
	foreach ($arrayName as $key) {
		$ret = checkPro($key,$str);
	}
	return $ret;
}

function checkPro($key,$str){
	$len = strlen($key);
	$mt = substr($str, 0,$len);
	return $len==$mt;
}



```
```python
<?php
error_reporting(0);
if ($_FILES["file"]["error"] > 0)
{
	$ret = array("code"=>2,"msg"=>$_FILES["file"]["error"]);
}
else
{
    $filename = $_FILES["file"]["name"];
    $filesize = ($_FILES["file"]["size"] / 1024);
    if($filesize>1024){
    	$ret = array("code"=>1,"msg"=>"文件超过1024KB");
    }else{
    	if($_FILES['file']['type'] == 'application/x-zip-compressed'){
            $arr = pathinfo($filename);
            $ext_suffix = $arr['extension'];
            if(in_array($ext_suffix, array("zip"))){
                move_uploaded_file($_FILES["file"]["tmp_name"], './upload/'.md5($_FILES["file"]["tmp_name"]).'.zip');
                $ret = array("code"=>0,"msg"=>md5($_FILES["file"]["tmp_name"]).'.zip');
            }else{
                $ret = array("code"=>3,"msg"=>"只允许上传zip格式文件");
            }
            
    		
    	}else{
    		$ret = array("code"=>2,"msg"=>"文件类型不合规");
    	}
    	
    }

}


echo json_encode($ret);
```
### 自己思路 上传图片马
上传图片马，但把图片后缀改为.zip <br />可以成功上传<br />![image.png](./images/20231018_0000427205.png)<br />用蚁剑连接，获取flag<br />![image.png](./images/20231018_0000434047.png)

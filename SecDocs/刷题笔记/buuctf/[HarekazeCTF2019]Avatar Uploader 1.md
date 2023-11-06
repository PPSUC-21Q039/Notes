# WP
[Harekaze CTF 2019 で出題した問題の解説](https://st98.github.io/diary/posts/2019-05-21-harekaze-ctf-2019.html#misc-100-avatar-uploader-1)
# 知识点
`finfo_file`和`getimagesize`判断文件类型的差异<br />`finfo_file`对PNG图片的识别
```powershell
root@950378d61f89:/tmp# echo '<?php $f = finfo_open(FILEINFO_MIME_TYPE); var_dump(finfo_file($f, "test.bin"));' > test.php
root@950378d61f89:/tmp# echo -en "\x89PNG\r\n\x1a\n\0\0\0\rIHDR\0\0\1\x90\0\0\1\x90\8\6\0\0\0\x80\xbf6\xcc" > test.bin; php test.php
string(9) "image/png"
root@950378d61f89:/tmp# echo -en "\x89PNG\r\n\x1a\n\0\0\0\rIHDR" > test.bin; php test.php
string(9) "image/png"
root@950378d61f89:/tmp# echo -en "\x89PNG\r\n\x1a\n\0\0\0\r" > test.bin; php test.php
string(24) "application/octet-stream"
```
`getimagesize`对PNG图片的识别
```powershell
root@950378d61f89:/tmp# echo '<?php $s = getimagesize("test.bin"); var_dump($s[2] === IMAGETYPE_PNG);' > test.php
root@950378d61f89:/tmp# echo -en "\x89PNG\r\n\x1a\n\0\0\0\rIHDR\0\0\1\x90\0\0\1\x90\8\6\0\0\0\x80\xbf6\xcc" > test.bin; php test.php
bool(true)
root@950378d61f89:/tmp# echo -en "\x89PNG\r\n\x1a\n\0\0\0\rIHDR" > test.bin; php test.php
bool(false)
root@950378d61f89:/tmp# echo -en "\x89PNG\r\n\x1a\n\0\0\0\r" > test.bin; php test.php
bool(false)
```
有可能是删除了PNG的宽高，导致`getimagesize`识别出现问题<br />![image.png](./images/20231017_2356421384.png)<br />代码
```php
// check file type
$finfo = finfo_open(FILEINFO_MIME_TYPE);
$type = finfo_file($finfo, $_FILES['file']['tmp_name']);
finfo_close($finfo);
if (!in_array($type, ['image/png'])) {
  error('Uploaded file is not PNG format.');
}

// check file width/height
$size = getimagesize($_FILES['file']['tmp_name']);
if ($size[0] > 256 || $size[1] > 256) {
  error('Uploaded image is too large.');
}
if ($size[2] !== IMAGETYPE_PNG) {
  // I hope this never happens...
  error('What happened...? OK, the flag for part 1 is: <code>' . getenv('FLAG1') . '</code>');
}
```

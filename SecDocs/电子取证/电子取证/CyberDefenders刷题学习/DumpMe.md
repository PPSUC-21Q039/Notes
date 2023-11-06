# 知识点
## 内存取证
Hint #Use "strings -e l" on dumped file as notepad stores text in the little-endian format.:<br />Use "strings -e l" on dumped file as notepad stores text in the little-endian format.

Indeed, when dealing with text files that were created on Windows, it's important to keep in mind that Windows uses a different encoding than Unix/Linux. Windows uses a 16-bit encoding called UTF-16, which is little-endian by default, while Unix/Linux use a variable-length encoding called UTF-8.<br />When you use the strings command to extract text from a file that was created on Windows, you need to use the -e l option to specify that the text should be interpreted as little-endian. If you don't use this option, the strings command will assume that the text is in big-endian format, which will result in garbled output.<br />I'm glad that you were able to identify the issue and resolve it by using the correct command-line options. If you have any other questions or concerns, feel free to ask!

#### MFT(file record)
-- mftparser<br />[Windows 取证之$MFT - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/network/278525.html)

#### VAD树
-- vadinfo<br />[VAD树结构体的属性以及遍历 - OneTrainee - 博客园](https://www.cnblogs.com/onetrainee/p/11741909.html)
# 工具

1. [Volatility 2](https://github.com/volatilityfoundation/volatility)
2. [sha1sum](https://en.wikipedia.org/wiki/Sha1sum)
# 思路
[Cyberdefenders: DumpMe CTF Writeup](https://www.discosec.org/post/cyberdefenders-dumpme-ctf-writeup)


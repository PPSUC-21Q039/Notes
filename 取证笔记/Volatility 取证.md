# Volatility 内存取证

Volatility 3:

```
python3 vol.py -f ../../RedLine/MemoryDump.mem windows.filescan.FileScan # 扫描文件

python3 vol.py -f ../../RedLine/MemoryDump.mem windows.netscan.NetScan # 扫描网络连接（相比2来说更加全面）

vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem -o pid6988/ windows.pslist.PsList --pid 6988 --dump # Dump the process of 6988, and it contains a full excutable file

xxd --seek 0x45BE876 20210430-Win10Home-20H2-64bit-memdump.mem | less # get the offset, and it can also be using command head

vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem  windows.cmdline.CmdLine | grep notepad
```

Volatility 2:

```
vol.py -f MemoryDump.mem --profile=Win10x64_19041 netscan
vol.py -f MemoryDump.mem --profile=Win10x64_19041 pslist
vol.py -f MemoryDump.mem --profile=Win10x64_19041 pstree
```


from hashlib import sha256
import sys

# 区号
area_code = "86"
# 常见手机号开头
begins = ["186","133","142","144","146","148","149","153","180","181","189","130","131","132","141","143","145","155","156","185","134","135","136","137","138","139","140","147","150","151","152","157","158","159","182","183","187","188"]
# 字符集
for begin in begins:
    for i in range(99999999):
        s256 = sha256()
        v = area_code+begin+"0"*(8-len(str(i))) + str(i)
        s256.update(v.encode('utf-8'))
        _hash = s256.hexdigest()
        if _hash[:5] == "eeb59" and _hash[-5:] == "2d29d":
            print("手机号已找到")
            print(begin+"0"*(8-len(str(i))) + str(i))
            sys.exit(0)
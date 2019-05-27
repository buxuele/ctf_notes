*********** commom *********
1. exiftool a.png
2. foremost -v a.png
3. binwalk -e flag.png
binwalk --dd='.*' hydra.png  提取所有类型的隐藏文件
4. steghide extract -sf stg.jpg
5. 解密图片的一个库,zsteg:
# zteg a.png
6. identify  + some.gif 查看摸个图片的基本信息.imagemagick的一个命令
7. ghex broken.jpg   来编辑一个文件的hex值


***************** png ******************
1. pngcheck -v  a.png # 检查 png文件

*********** others  *********
1. imagemagick, 命令行图片处理库,有很多丰富的功能.
# maigck -version


jpg:
 header: FF D8 FF E0 xx xx 4A 46 49 46 00, footer: FF D9
png:
 header: 89 50 4E 47 0D 0A 1A 0A, footer: 49 45 4E 44 AE 42 60 82
gif:
 header: 47 49 46 38 39 61, footer: 00 3B

*********** commom *********
1. exiftool a.png
2. foremost -v a.png
5. zsteg　-a a.png  检查隐藏如图片      # 这个是很常用的
3. binwalk -e flag.png
binwalk --dd='.*' hydra.png  提取所有类型的隐藏文件
4. steghide extract -sf stg.jpg
6. identify  + some.gif 查看摸个图片的基本信息.imagemagick的一个命令
7. ghex broken.jpg   来编辑一个文件的hex值
8. pngcheck -v  a.png # 检查 png文件

*********** others  *********
1. imagemagick, 命令行图片处理库,有很多丰富的功能.
# maigck -version
2.

jpg:
 header: FF D8 FF E0 xx xx 4A 46 49 46 00, footer: FF D9
png:
 header: 89 50 4E 47 0D 0A 1A 0A, footer: 49 45 4E 44 AE 42 60 82
gif:
 header: 47 49 46 38 39 61, footer: 00 3B

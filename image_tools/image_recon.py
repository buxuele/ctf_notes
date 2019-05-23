
1. exiftool a.png
2. foremost -v a.png
3. binwalk -e flag.png

1. pngcheck -v  a.png # 检查 png文件
2. steghide extract -sf stg.jpg


17. 解密图片的一个库,zsteg:
#　detect stegano-hidden data in PNG & BMP

1. imagemagick, 命令行图片处理库,有很多丰富的功能.
# maigck -version



jpg:
 header: FF D8 FF E0 xx xx 4A 46 49 46 00, footer: FF D9
png:
 header: 89 50 4E 47 0D 0A 1A 0A, footer: 49 45 4E 44 AE 42 60 82
gif:
 header: 47 49 46 38 39 61, footer: 00 3B

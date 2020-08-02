conda 基本使用流程:

```bash
# 1. 创建并激活虚拟环境 
conda create -n open-mmlab python=3.7 -y
conda activate open-mmlab	# conda deactivate 退出
# 2. conda 下载太慢了
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
# 3. 使用 conda 安装包 去掉最后的 -c pytorch。 删除这个 -c pytorch 才是从清华源下载！
conda install pytorch torchvision
# 4. 参考官网给出的cuda版本 https://pytorch.org/get-started/locally/
conda install pytorch torchvision cudatoolkit=10.2
# 5.

```

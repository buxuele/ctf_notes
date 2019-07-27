1. pip3 找不到 main, 直接重装 pip3
sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall
2. 强制重新安装某个包
pip3 install --no-deps --ignore-installed --no-cache-dir numpy
3.from string import ascii_letters, digits
characters = ascii_letters + digits
4. 如何退出　venv?  deactivate
5. 如何能利用缓存按照其他的包?
6.


pipenv 个人经验，　按照以下顺序，　速度最快
1. pipenv install
2. pipenv shell         # start env
3. pip3 install <packageName>  # now install

4. pipenv lock -r :   generate a requirements.txt

django
1.'DIRS': [],   this is default
'DIRS': [os.path.join(BASE_DIR, 'templates')],  # let multi apps use same html templates
2.

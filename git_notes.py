
1. 如何加速git clone
	- 官方推荐使用https, 而不是ssh. stackoverflow上的解释是:可以通过防火墙
	- 如果不需要 历史记录的话:
# git clone --depth 1 some@repo


```
git reflog 可以查看所有分支的所有操作记录
	（包括已经被删除的 commit 记录和 reset 的操作）
git reset --hard HEAD~1，退回到上一个版本
git show 39e85b2	# show details
# Amend Author Of Previous Commit
$ git commit --amend --author "D <d@r.com>"
```
************************　分割线　*******************************
```

1. git checkout -b <new_branch>	# -b == branch, 新建一个分支。

#### github workflow

0. Fork. copy a repo under my account.
(need access to the repo)
1. branching,start a new work placef
2. commit, make some changes
3. pull request, compare with others' branch
4. collaborate, 协作。
5. merge
6. open pull request

**********************************
###git command means:

1. git pull, shows some changes from other people
1. git cofig -l ， 列出所有的配置信息
2. git help cmd  ， 查看某个命令的帮助信息

#### 初次安装git需要配置的信息

（这里的 --global，意思是整个系统全局的配置。）
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
$ git config --global core.editor subl


Git fork（修改别人的内容）笔记：
1. git remote -v
查看本地仓库所属的远程信息（这个仓库属于谁的，从哪来的）
2. git remote add upstream + 原始仓库地址
	这个命令的目的是：添加 本地与远程的同步关系
	再次 输入 git remote -v 查看显示结果
3. 然后是 写上自己需要修改的内容。 git push就行了？？？？？ 需要再测试一下。

```

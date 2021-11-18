学习网站：https://www.mongodb.org.cn/tutorial/7.html
下载：https://cloud.mongodb.com/v2/61932cc9dc491d241fbeff48#clusters
菜鸟数据库学习：https://www.runoob.com/mongodb/mongodb-osx-install.html
网站：https://pymongo.readthedocs.io/en/stable/tutorial.html
查询高级：https://docs.mongodb.com/manual/reference/operator/

# 存放数据库及打印的log位置，并且放后台
mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork

# 查看后台进程
ps aux | grep -v grep | grep mongod

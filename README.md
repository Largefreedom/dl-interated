# dl-Intergrated-django
以 Vue+ElementPlus作为前端，Django为后端集成 Paddle OCR模型; 实现 OCR 识别+敏感词检测

项目功能预览
* ✔️PaddleOCR 图片识别
* ✔️账号登录注册、及注销
* ✔️OCR 文本敏感词检测与过滤
* ✔️保留识别历史记录 并保存



## 项目启动流程 -- Django 端
* 1，创建虚拟环境(可选)
```shell
# 创建文件夹
mkdir venv

# 创建虚拟环境
python -m venv venv
```
* 2，检查数据库迁移
```shell
python manage.py makemigrations
```

* 3，数据库迁移
```shell
python manage.py migrate
```


* 4，项目启动
```shell
python manage.py runserver
```



## 前端
首先需要确保你的电脑中安装了 nodejs
* 1,安装依赖
```shell
npm i
```
* 2, 前端启动
```shell
npm run serve
```

# Simple Search Engine

## 应用介绍

社会信息检索与计算作业，要求实现功能如下：

* TFIDF:  给定用自己名字命名的文件夹，请自己爬取一定数量的网页、微博形成语料集合，存入该文件夹；在线状态下，对其中的词语进行TFIDF统计，且输出到文件中。文件存储目录为`app/tfidf/tfidf_result`。
* SIM:  在线状态下，从网页页面输入任意两个句子，求其相似度，包括：内积，余弦及Jaccard三种度量方式。


* SJet：实现基于向量空间模型（VSM）的搜索引擎。 

## 运行环境

* Linux
* python 2.7
* jieba
* flask 0.12
* 若干flask扩展

## 运行方法

* 在工程根目录下打开终端

* 用如下命令激活python虚拟环境

  ```Linux
  source venv/bin/activate
  ```

* 用如下命令运行程序

  ```Linux
  python hello.py runserver
  ```

* 访问`127.0.0.1:5000`

## 项目结构

1. net_ease_roll.py

   爬虫。爬取内容为[网易滚动新闻](http://news.163.com/latest)国内、国际、社会版块，共计416篇新闻。爬虫运行环境为Windows。

2. tfidf_calc.py

   对爬取的新闻文本做分词预处理。

3. config.py

   存储配置。

4. hello.py

   用于启动程序以及其他的任务程序。

5. app

   1. \_\_init\_\_.py

      Flask工程文件

   2. sim

      实现SIM功能蓝本，具体算法实现在此文件夹下views.py文件中

   3. sjet

      实现Sjet功能蓝本，具体算法实现在此文件夹下views.py文件中

   4. tfidf

      实现TFIDF功能蓝本，具体算法实现在此文件夹下views.py文件中

   5. templates

      前端模板。模板使用Jinja2模板引擎做前端渲染。


























#### 1.basic bash command lines: 

```bash 
head -n 2 filename  // show first 2 lines of the file 
tail -n 2 filename  // show last 2 lines of the file

cat filename // show contents of filename 
```



#### 2. DNA RNA Finder Doc

环境：python 2.7 

Modules: os, multiprocessing, pandas, glob, sys 



##### 使用
试验的DNA数据存在data/文件夹下，结果存储在rlt/下。

打开terminal, 在FrogFinder目录下执行命令。每次执行程序时候保证rlt/文件夹下的结果已经转存到别处，该文件夹需为空的。

```bash
python DNA_RNA_Finder.py shRNA.csv
# shRNA.csv 是我们要找的RNA文件 
```


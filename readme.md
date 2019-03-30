#### 1.basic bash command lines: 

```bash 
cd /foldername  # change directory to folder 
cd FrogFinder   # change directory 

pwd   # print directory 
ls   # show all files 

head -n 2 filename  # show first 2 lines of the file 
tail -n 2 filename  # show last 2 lines of the file

cat filename # show contents of filename

pwd 

git clone <https://github.com/Daynity/FrogFinder>

# ACTIVATE venv 
source bin/activate
 
```



#### 2. DNA RNA Finder Doc

环境：python 2.7 

Modules: multiprocessing, pandas, glob, sys 



##### 使用
试验的DNA数据存在 data/ 文件夹下，结果存储在 rlt/ 下。

打开terminal, 在FrogFinder目录下执行命令。每次执行程序时候保证 rlt/ 文件夹下的结果已经转存到别处，该文件夹需为空的。

```bash
mkdir data  # create a folder for data 
mkdir rlt   # create a folder to store results

python DNA_RNA_Finder.py shRNA.csv
# shRNA.csv 是我们要找的RNA文件 
```


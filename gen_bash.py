import pandas as pd
from glob import glob


# STEP 1
"""
# delete a certain pattern line 

awk '!/^F/' large-library-B11_FKDL190729648-1a-23_1.clean.fq > temp0 
awk '!/^@/' temp0 > temp1
awk '!/^F/' temp1 > temp2
awk '!/^:/' temp2 > temp3

rm large-library-B11_FKDL190729648-1a-23_1.clean.fq
mv temp3 large-library-B11_FKDL190729648-1a-23_1.clean.fq
rm temp*
 


"""

fq_filenames = glob('*.fq')
for fq_filename in fq_filenames:
    s0 = "awk '!/^F/' {} > temp0 \n".format(fq_filename)
    s1 = "awk '!/^@/' temp0 > temp1 \n"
    s2 = "awk '!/^F/' temp1 > temp2 \n"
    s3 = "awk '!/^:/' temp2 > temp3 \n"
    s4 = "rm {} \n".format(fq_filename)
    s5 = "mv temp3 {} \n".format(fq_filename)
    s6 = "rm temp* \n"
    with open('run_awk_simplify_fq.sh', 'a') as the_file:
        the_file.write(s0)
        the_file.write(s1)
        the_file.write(s2)
        the_file.write(s3)
        the_file.write(s4)
        the_file.write(s5)
        the_file.write(s6)







# STEP 2
"""
# awk '/dan/{ print $0 }' test.fq
# awk '{ print $2 }' text.txt > outputfile.txt


awk '/GTGCGTTGCTAGTACCAACCTA/{ print $0 }' new_data/large-library-B11_FKDL190729648-1a-23_1.clean.fq > GTGCGTTGCTAGTACCAACCTA.B11_FKDL190729648-1a-23_1.txt

"""
df_rna = pd.read_csv('new_data/large_scale.csv', header=None)
ls_rna = list(df_rna[0])

fq_filenames = glob('new_data/*.fq')

print(len(ls_rna))
print(len(fq_filenames))


cnt = 0
for rna in ls_rna:
    for fq_filename in fq_filenames:
        ss = "awk '/{rna}/{left_bra} print $0 {right_bra}' {fq_filename} > rlt/{rna}.{fq_filename_nofolder}.txt".format(
            rna=rna,
            fq_filename=fq_filename,
            left_bra="{",
            right_bra="}",
            fq_filename_nofolder=fq_filename.replace('new_data/', ''))

        with open('run_awk_find.sh', 'a') as the_file:
            the_file.write(ss+'\n')

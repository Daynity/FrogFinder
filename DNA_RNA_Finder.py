import os
import pandas as pd
from glob import glob
import multiprocessing
import sys


def find_matched_dna_partial(rna_val, dna_filename_nofolder, dna, index_min, index_max):
    write_filename = 'rlt/{}.{}.{}.csv'.format(rna_val, dna_filename_nofolder, index_min)
    for k in range(index_min, index_max):
        dna_val = list(dna.iloc[k])[0]
        if len(dna_val) > 50:
            # print(k, val_dna, '\t\t', len(val_dna))
            if rna_val in dna_val:
                # print(k, dna_val)
                with open(write_filename, 'a') as the_file:
                    the_file.write('{},{}\n'.format(rna_val, dna_val))
    return None


def find_matched_dna(rna_val, dna_filename, poolnum=6):
    dna = pd.read_csv(dna_filename, sep='\n', header=None)
    dna_filename_nofolder = dna_filename.replace('data/', '')
    pool = multiprocessing.Pool(processes=poolnum)
    inds = list(range(0, len(dna), 50000)) + [len(dna)]
    for j in range(len(inds) - 1):
        print('batch number: {}'.format(j))
        index_min = inds[j]
        index_max = inds[j + 1]
        pool.apply_async(find_matched_dna_partial, (rna_val, dna_filename_nofolder, dna, index_min, index_max,))

    pool.close()
    pool.join()
    print('finished batch processing')
    return None


def get_rna_list(rna_filename):
    """
    rna: rna_filename, 'data/shRNA.csv'
    """
    rna = pd.read_csv(rna_filename, header=None)
    # print(list(rna.iloc[1]), len(list(rna.iloc[1])[0]))
    rna.head(10)
    ls_rna = []
    for k in range(len(rna)):
        val = list(rna.iloc[k])[0]
        if len(val) > 15:
            ls_rna.append(val)
    return ls_rna


def DNA_RNA_Finder(rna_filename, dna_file_folder='data/'):
    dna_filenames = glob('{}*.fq'.format(dna_file_folder))
    rna_ls = get_rna_list(rna_filename)
    for rna_val in rna_ls:
        for dna_filename in dna_filenames:
            print('start finding rna {} from dan file {} ......'.format(rna_val, dna_filename))
            find_matched_dna(rna_val, dna_filename)

    # sum and save sub-results
    for rna_val in rna_ls:
        rlt_filenames = glob('rlt/{}*fq.*.csv'.format(rna_val))
        rlt = pd.DataFrame()
        for f in rlt_filenames:
            tmp_rlt = pd.read_csv(f, header=None)
            rlt = pd.concat([rlt, tmp_rlt])
            # os.remove(f)
        rlt.to_csv('rlt/FINAL_RESULT.rna.{}.csv'.format(rna_val))
        print('saved result for rna {}'.format(rna_val))
    return None


if __name__ == '__main__':
    rna_filename = sys.argv[1] # 'shRNA.csv'
    DNA_RNA_Finder(rna_filename)
    # python DNA_RNA_Finder.py shRNA.csv

# todo: qa results


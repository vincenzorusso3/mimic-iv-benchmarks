from __future__ import absolute_import
from __future__ import print_function

import os
import shutil
import argparse


def move_to_partition(args, patients, partition):
    if not os.path.exists(os.path.join(args.subjects_root_path, partition)):
        os.mkdir(os.path.join(args.subjects_root_path, partition))
    for patient in patients:
        src = os.path.join(args.subjects_root_path, patient)
        dest = os.path.join(args.subjects_root_path, partition, patient)
        shutil.move(src, dest)


def main():
    parser = argparse.ArgumentParser(description='Split data into train and test sets.')
    parser.add_argument('subjects_root_path', type=str, help='Directory containing subject sub-directories.')
    args, _ = parser.parse_known_args()

    test_set = set()
    train_set = set()
    with open(os.path.join(os.path.dirname(__file__), '../resources/testset.csv'), "r") as test_set_file:
        for line in test_set_file:
            x, y = line.split(',')
            if int(y) == 1:
                test_set.add(x)#il criterio che mi genera lo split qui è diverso dai nomi delle cartelle

                #print(x)

    folders = os.listdir(args.subjects_root_path) #è come se caricasse male i nomi delle cartelle mette delle cifre all' inizio
    #print(folders)
    folders = list((filter(str.isdigit, folders)))

    #devo modificare gli elementi della lista per matchare
    #print(type(folders))

    #devo mantenere solo gli n caratteri più a destra nella lista
    #folders = [s[1:] for s in folders]
    ##devo togliere tutti gli zeri a sx
    #folders = [s.lstrip('0') for s in folders]




    #print(folders)
    #test_patients=set()
    #train_patients=set()
    test_patients = [x for x in folders if x in test_set]

    """for x in folders:
        if x in test_set:
            test_patients.add(x)"""

    train_patients = [x for x in folders if x not in test_set]##non fa bene la differenza

    """for x in folders:
        if x not in test_set:
            train_patients.add(x)"""

    assert len(set(train_patients) & set(test_patients)) == 0
    print(test_set)
    print(len(set(train_patients)))
    print(len(set(test_patients)))
    

    move_to_partition(args, train_patients, "train")
    move_to_partition(args, test_patients, "test")


if __name__ == '__main__':
    main()

# Tests for checking whether the benchmark datasets were generated correctly

The main script is the `mimic4benchmark/tests/hash_tables.py` script which takes a directory and hashes all `.csv` files inside it recursively.
The output is a `.pkl` file which lists all `.csv` files and their hashes.
If this files matches with the corresponding file from `mimic4benchmark/tests/resources` then the test is successful.
Here are a couple of examples.

### Root directory
```bash
python -um mimic4benchmark.tests.hash_tables -d data/root -o root-final.pkl;
diff root-final.pkl mimic4benchmark/tests/resources/root-final.pkl;
```

### In-hospital mortality
```bash
python -um mimic4benchmark.tests.hash_tables -d data/in-hospital-mortality -o ihm.pkl;
diff ihm.pkl mimic4benchmark/tests/resources/ihm.pkl;
```

### Decompensation
```bash
python -um mimic4benchmark.tests.hash_tables -d data/decompensation -o decomp.pkl;
diff decomp.pkl mimic4benchmark/tests/resources/decomp.pkl;
```

### Length-of-stay
```bash
python -um mimic4benchmark.tests.hash_tables -d data/length-of-stay -o los.pkl;
diff los.pkl mimic4benchmark/tests/resources/los.pkl;
```

### Phenotyping
```bash
python -um mimic4benchmark.tests.hash_tables -d data/phenotyping -o pheno.pkl;
diff pheno.pkl mimic4benchmark/tests/resources/pheno.pkl;
```

### Multitasking
```bash
python -um mimic4benchmark.tests.hash_tables -d data/multitask -o multitasking.pkl;
diff multitasking.pkl mimic4benchmark/tests/resources/multitasking.pkl;
```

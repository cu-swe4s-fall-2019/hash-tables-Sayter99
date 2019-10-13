# Hash tables


## Usage
```python
python hash_functions.py --input rand_words.txt --hash_method ascii | python scatter.py --out_file images/ascii_hash_function_rand.png --x_label "Hashed Word" --y_label "Hashed Value"
```
![](images/ascii_hash_function_rand.png)

```python
python hash_functions.py --input non_rand_words.txt --hash_method ascii | python scatter.py --out_file images/ascii_hash_function_non_rand.png --x_label "Hashed Word" --y_label "Hashed Value"
```
![](images/ascii_hash_function_non_rand.png)

```python
python hash_functions.py --input rand_words.txt --hash_method rolling | python scatter.py --out_file images/rolling_hash_function_rand.png --x_label "Hashed Word" --y_label "Hashed Value"
```
![](images/rolling_hash_function_rand.png)

```python
python hash_functions.py --input non_rand_words.txt --hash_method rolling | python scatter.py --out_file images/rolling_hash_function_non_rand.png --x_label "Hashed Word" --y_label "Hashed Value"
```
![](images/rolling_hash_function_non_rand.png)

```bash
for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method rolling --collision_strategy linear --input rand_words.txt --key_nums $M --search_nums 100 > test_rolling_linear_rand.$M.txt
done

grep add test_rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file images/rolling_linear_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file images/rolling_linear_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method ascii --collision_strategy linear --input rand_words.txt --key_nums $M --search_nums 100 > test_ascii_linear_rand.$M.txt
done

grep add test_ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file images/ascii_linear_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file images/ascii_linear_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method rolling --collision_strategy chain --input rand_words.txt --key_nums $M --search_nums 100 > test_rolling_chain_rand.$M.txt
done

grep add test_rolling_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file images/rolling_chain_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_rolling_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file images/rolling_chain_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method ascii --collision_strategy chain --input rand_words.txt --key_nums $M --search_nums 100 > test_ascii_chain_rand.$M.txt
done

grep add test_ascii_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file images/ascii_chain_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_ascii_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file images/ascii_chain_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt
```
![](images/ascii_chain_add_time.png)
![](images/ascii_chain_search_time.png)
![](images/ascii_linear_add_time.png)
![](images/ascii_linear_search_time.png)
![](images/rolling_chain_add_time.png)
![](images/rolling_chain_search_time.png)
![](images/rolling_linear_add_time.png)
![](images/rolling_linear_search_time.png)

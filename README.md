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
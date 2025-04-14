# Joins in Spark

In Apache Spark, joins are used to combine data from two or more DataFrames based on a common column (or condition). When working with Spark, you can perform several types of joins to merge data based on how you want to handle the records that don't have a match in both DataFrames. Here's an explanation of the different types of joins:

### 1. **Inner Join (Default Join)**

* **Definition** : An inner join returns only the rows that have matching values in both DataFrames.
* **How it works** : If there is a match based on the join condition (such as matching columns), the row is included in the result. Rows without a match in either DataFrame are excluded.
* **Example** : If you're joining two DataFrames on a "user_id" column, only the users that exist in both DataFrames will be included in the output.

```python
  df1.join(df2, df1.user_id == df2.user_id, 'inner')
```

### 2. **Left Join (Left Outer Join)**

* **Definition** : A left join returns all the rows from the left DataFrame, along with the matching rows from the right DataFrame. If there's no match, `null` values will be filled in for columns from the right DataFrame.
* **How it works** : Every record from the left DataFrame will appear in the result. If there's no corresponding record in the right DataFrame, the right DataFrame's columns will contain `null` for that row.
* **Example** : If you want to include all users from the left DataFrame, even if some of them don’t have a matching record in the right DataFrame.

```python
  df1.join(df2, df1.user_id == df2.user_id, 'left')
```

### 3. **Right Join (Right Outer Join)**

* **Definition** : A right join returns all the rows from the right DataFrame, along with the matching rows from the left DataFrame. If there's no match, `null` values will be filled in for columns from the left DataFrame.
* **How it works** : Similar to the left join, but the emphasis is on keeping all the rows from the right DataFrame. If there’s no match in the left DataFrame, the left DataFrame’s columns will be filled with `null`.
* **Example** : If you want to keep all records from the right DataFrame and include data from the left DataFrame wherever there’s a match.

```python
  df1.join(df2, df1.user_id == df2.user_id, 'right')
```

### 4. **Full Join (Full Outer Join)**

* **Definition** : A full join returns all rows from both DataFrames. If there's no match, `null` values will be used for the columns from the DataFrame that doesn’t have a matching row.
* **How it works** : This join includes all records from both DataFrames. If one DataFrame has rows that don't match the other, the result will still include those rows, filling in `null` where necessary.
* **Example** : If you want to include all records from both DataFrames, even if they don't match, with `null` for missing data.

```python
  df1.join(df2, df1.user_id == df2.user_id, 'outer')
```

---

### Summary of Join Types

* **Inner Join** : Returns rows with matching values in both DataFrames.
* **Left Join** : Returns all rows from the left DataFrame, with matching rows from the right DataFrame (or `null` if no match).
* **Right Join** : Returns all rows from the right DataFrame, with matching rows from the left DataFrame (or `null` if no match).
* **Full Join** : Returns all rows from both DataFrames, with `null` for non-matching rows.

These joins allow you to combine data in Spark based on different requirements for handling non-matching rows

.

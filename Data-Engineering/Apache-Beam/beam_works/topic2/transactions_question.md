# Tasks

1. Calculate the total amount spent by each customer.
2. Count the total number of each item purchased across all transactions.
3. Partition the customers into two groups:
   - **Group 1**: Customers who spent more than ₹10,000 in total.
   - **Group 2**: Customers who spent ₹10,000 or less in total.

## Solution using Apache Beam

1. **`map`**: Parse the input records (e.g., CSV lines) to create a dictionary for each transaction, containing `CustomerID`, `TransactionAmount`, and `ItemsPurchased`.
2. **`flatMap`**: Split the `ItemsPurchased` field into individual items and emit `(item, 1)` key-value pairs for each item purchased.
3. **`filter`**: Remove transactions with a `TransactionAmount` less than or equal to zero.
4. **`groupByKey`**: Group the key-value pairs of items by their item names to aggregate all occurrences of each item.
5. **`combine`**: Use a `CombineFn` to calculate the total amount spent by each customer by summing their transaction amounts.
6. **`partition`**: Divide the customers into two groups based on their total spending.

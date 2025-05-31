# Module 2 3 4

### **Assignment: Sales Commission Calculator**  
**Estimated Time:** ~2 hours  
**Objective:** Build a simple Python program to calculate sales commission based on performance.  

#### **Problem Statement:**  
You are working as a developer for a retail company. The sales team wants a program that helps calculate their commission based on the sales amount they achieve. The commission structure is as follows:  

- Sales below **$5000** → No commission  
- Sales between **$5000 and $10,000** → **5% commission**  
- Sales between **$10,000 and $20,000** → **10% commission**  
- Sales above **$20,000** → **15% commission**  

**Additional Requirements:**  
- If the salesperson meets or exceeds **$15,000**, they get a **$500 performance bonus** in addition to their commission.  
- The program should:  
  1. Take **sales amount** as input from the user.  
  2. Calculate the commission based on the given criteria.  
  3. Add a performance bonus if applicable.  
  4. Display the total earnings (sales + commission + bonus).
  5. Retry input until the user enters a valid sales amount
  6. Print a detailed commission breakdown using a loop

**Bonus:** Using a Loop to Display Commission Breakdown
- If we want to show the commission at each sales level, a for loop can be used:

```python
print("Commission Breakdown:")
for level in [5000, 10000, 20000]:
    if sales > level:
        print(f"Sales exceeded ${level}: Applying next commission rate")
```


#### **Example Output:**  
```plaintext
Enter your total sales: 12000
Sales: $12,000.00
Commission (10%): $1,200.00
Bonus: $500.00
Total Earnings: $13,700.00
```

---

### **Submission Guidelines:**  
- Write the program in **Python** with clear comments.  
- Save your file as `sales_commission_calculator.py`.  
- Test the program with different sales amounts.  

---

This scenario mimics a real-world business application while testing their knowledge of **variables, data types, operators, type casting, and control flow statements**.🚀
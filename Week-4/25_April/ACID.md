# ACID Properties :
    - In order to maintain consistency in a database, before and after the transaction, certain properties are followed.These are called ACID properties. 

## Atomicity : All Or Nothing Rule
    - Each transaction is considered as one unit and either runs to completion or is not executed at all.

[<img src="https://media.geeksforgeeks.org/wp-content/uploads/11-6.jpg" width="500"/>](image)


## Consistency : Preserving Database Invariants
    - This means that integrity constraints must be maintained so that the database is consistent before and after the transaction. It refers to the correctness of a database.
   
### Example :
    - The total amount before and after the transaction must be maintained.
    - Total before T occurs = 500 + 200 = 700.
    - Total after T occurs = 400 + 300 = 700.


## Isolation : 
    - multiple transactions can occur concurrently without leading to the inconsistency of the database state.
    - Transactions occur independently without interference. 

### Example

    - Let X= 500, Y = 500. 
    - Consider two transactions T and T”. 

[<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210402015259/isolation-300x137.jpg" width="500"/>](image)

    - Suppose T has been executed till Read (Y) and then T’’ starts. As a result, interleaving of operations takes place due to which T’’ reads the correct value of X but the incorrect value of Y and sum computed by 
    T’’: (X+Y = 50, 000+500=50, 500) 
    is thus not consistent with the sum at end of the transaction: 
    T: (X+Y = 50, 000 + 450 = 50, 450).
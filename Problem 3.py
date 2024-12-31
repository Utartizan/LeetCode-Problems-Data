
# Write a solution to find all customers who never order anything.
#
# Return the result table in any order.
#
# The result format is in the following example.


import pandas as pd # import library for data manip and filtration again

# set up a function which is designed to take two arguments;
## set up a dataframe that contains information about customers
## as well as one that contains information about their orders
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    # utilise the '.unique()' function to retrieve all... unique 'customerId' values from
    # the 'orders' dataframe

    # necessary to identify all customers who have ordered at least once, or placed at least one order
    customersWithOrders = orders['customerId'].unique()

    # checks if customer ids exist in the 'customersWithOrders' array
    # which would be true had there not been a ~ operator
    # which reverts this entire function and does the opposite
    # meaning it checks the prior line to see if there are customers who haven't placed any orders

    customersWithoutOrders = customers[~customers['id'].isin(customersWithOrders)]


    # set only the 'name' column from the customersWithoutOrders dataframe and renames it to 'Customers'
    # assign all of this to a variable called 'result'.
    result = customersWithoutOrders[['name']].rename(columns={'name': 'Customers'})

    # return this variable.
    # upon returning this you should expect to have received an output containing
    # a list of customers who have not placed any orders
    return result


# Quick Note, the `.isin()` function in Pandas is used to filter values in a DataFrame or Series.
# It checks whether each element in a column (or Series) is **present in a provided list, set, or iterable**.

# It returns a Boolean Series, where:
### True indicates that the value is in the provided list/set.
### False indicates that the value is not in the provided list/set.

# Write a solution to find the ids of products that are both low fat and recyclable.
#
# Return the result table in any order.
#
# The result format is in the following example.


import pandas as pd # import panda libraries to enable data manipulation

# set up sample data in which the data manipulation process acts on
data = {
    'product_id': [1, 2, 3, 4],
    'low_fats': ['Y', 'N', 'Y', 'N'],
    'recyclable': ['Y', 'Y', 'N', 'Y']
}

# function -> parameter of name 'products' -> which is assigned to the pandas dataframe
# to return another
def find_products(products: pd.DataFrame) -> pd.DataFrame:

    # filters dataset so that the rows include both 'low_fats' and 'recyclable' products only.
    # the & is a logical AND operator which means both conditions have to be met to pass the filter
    find_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]

    # return the filtered result, which in this case is only the 'product_id' column
    # that passes the find_products filtration
    return find_products[['product_id']]


# assign the newly filtered dataframe into a new variable 'products_df'
products_df = pd.DataFrame(data)

# call the function
result = find_products(products_df)

# print the result
print(result)

# Big Countries Problem on Leetcode;
# A country is big if:
#
# it has an area of at least three million (i.e., 3000000 km2), or
# it has a population of at least twenty-five million (i.e., 25000000).
# Write a solution to find the name, population, and area of the big countries.
#
# Return the result table in any order.
#
# The result format is in the following example.


import pandas as pd #imports pandas library for data manipulation

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_countries = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    # selects rows where the values in 'area' >= 3,000,000 and values in 'population' >= 25,000,000
    # the | acts as an OR operator, meaning the row is to be selected if EITHER condition is satisfied

    table = big_countries[['name', 'population', 'area']]
    # this function selects specific columns from the now filtered big_countries dataframe


    return table
    # return these specific columns in output

#This function `big_countries` filters and returns information about countries that:
# 1. Have a land area of 3,000,000 square kilometers or more OR
# 2. Have a population of 25,000,000 or more.

# The output includes only the `name`, `population`, and `area` columns for these countries.

## When as specific data table is specified, e.g.

dataSpecified = {

    'name': ['Alpha', 'Beta', 'Gamma', 'Delta', 'Zeta'],
    'population': [100000000, 200000000, 300000000, 400000000, 500000000],
    'area': [3000000, 1000000, 6000000, 4000000, 8000000],

}

dataWorld = pd.DataFrame(dataSpecified)

result = big_countries(dataWorld)

print(result)

# The result therefore would include the table consisting of the countries
# that follows the requirements: Gamma, Delta, and Zeta
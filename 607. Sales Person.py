import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Firstly join `sales_person` and `orders` dataframe. `outer` join because we don't want information loss in any of the two dataframes.
    intermediate_merge = sales_person.merge(right=orders, how="outer", on="sales_id")

    # Perform a second (final) join with `company` dataframe. `left` because we don't want redundant information from company.
    final_merge = intermediate_merge.merge(right=company, how="left", on="com_id")

    # Filter sales persons involved in sales related to RED.
    red= final_merge[final_merge["name_y"] == "RED"][["name_x"]]

    # To obtain people who are not related to RED, perform an outer join between `sales_person[[name]]` and `red` dataframes with indicator flag set to True. 
    non_red = sales_person[["name"]].merge(right=red, how="outer", left_on="name", right_on="name_x", indicator=True)

    # Return the name of the people with "left_only" indicator in the "_merge" column of `non_red` dataframe.
    return non_red[non_red["_merge"] == "left_only"][["name"]]

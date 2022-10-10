from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_views_dataframe, get_view_data_dataframe
import pandas as pd


tableau_server_config = {
        'tableau_prod': {
                'server': 'https://prod-useast-a.online.tableau.com/',  # was https://online.tableau.com
                'api_version': '3.16',
                'username': 'longdisdick27@gmail.com',
                'password': 'Bruh76%1',
                'site_name': 'bullish',
                'site_url': 'realinventory',
        }
}

conn = TableauServerConnection(tableau_server_config)
conn.sign_in()


# setting pandas global data options
pd.options.display.max_columns = None
pd.options.display.max_rows = None


# getting (all) the site data (not in pretty pandas and idk why. [should learn how])
views_df = get_views_dataframe(conn)
clean = views_df
# print(clean)


# how to parse-> return: 'name' & 'updatedAt'
parse_names = views_df['name']
parse_updateat = views_df['updatedAt']
parse_contenturl = views_df['contentUrl']
# print(parse_names)
# print(parse_update)
print(parse_contenturl)


# locating the specific site using pandas (and brute force)
just_bullish = views_df.iloc[17]
# print(just_bullish)
# this is what i wanted -> the bullish/sheets/Sheet1 id: 8a03bff6-f3d8-459c-a6e2-32339a73014f


# getting specific view data
view_data_df = get_view_data_dataframe(conn, view_id='8a03bff6-f3d8-459c-a6e2-32339a73014f')
print(view_data_df)


# translating tab_qty & tab_product data to a combined list of dictionaries
row_id_product = view_data_df.index[view_data_df['Product'] == 'rose'].to_numpy(dtype=int)
tab_qty_table = view_data_df['Measure Values']
tab_product_table = view_data_df['Product']

table2 = []

table2.append(dict(zip(tab_product_table, tab_qty_table)))

print(list(table2))




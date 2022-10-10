from sheet2api import Sheet2APIClient
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_views_dataframe, get_view_data_dataframe
import pandas as pd
import numpy as np
import time


# test dictionaries
mock_xml = [
    {'product': 'cabernet', 'qty': 33},
    {'product': 'rose', 'qty': 66},
    {'product': 'bob jones', 'qty': 99}]


s2a_client_write = Sheet2APIClient(
    api_url='https://sheet2api.com/v1/bSRF25UR2yBL/final_inventory',  # google sheets version
    username='',
    password='',
)


s2a_client_read = Sheet2APIClient(
    api_url='https://sheet2api.com/v1/bSRF25UR2yBL/scannedinventory2',  # google sheets version
    username='',
    password='',
)


# pulls all data from google sheet storing scanned inventory
xml_live = s2a_client_read.get_rows()
print('xml_live = ', xml_live)
print('xxx_linebreakk_xxx')


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


# getting the specific view data (by view id)
view_data_df = get_view_data_dataframe(conn, view_id='8a03bff6-f3d8-459c-a6e2-32339a73014f')
print('tableau view data = ', view_data_df)
print('xxx_linebreakk_xxx')


# getting specific view data as tables
tab_product_table = view_data_df['Product']
tab_qty_table = view_data_df['Measure Values']


# creating the final tab_proper_inventory[{}]
tab_proper_inventory = []


def proper_tab():
    for x in tab_product_table:
        row_id_product = view_data_df.index[view_data_df['Product'] == x].tolist()

        for y in tab_qty_table:
            row_id_qty = view_data_df.index[view_data_df['Measure Values'] == y].tolist()
            if row_id_product == row_id_qty:
                tab_proper_inventory.append({'product': x, 'qty': y})


proper_tab()
print('tab_proper_inventory = ', tab_proper_inventory)
print('xxx_linebreakk_xxx')


# creates the final live_inventory[{}] then uploads it to final_inventory google sheet
def ledger_live_handler():
    for itab in tab_proper_inventory:

        for ixml in xml_live:
            data_qty_xml = ixml['qty']
            data_qty_tab = itab['qty']
            if itab['product'] == ixml['product']:
                ixml['qty'] = data_qty_tab + data_qty_xml
                ledger_live = xml_live
                break
            else:
                pass

    print('ledger_live = ', ledger_live)

    s2a_client_write.delete_rows(
        sheet='Sheet1'
    )

    for i in ledger_live:
        s2a_client_write.create_row(
            sheet='Sheet1',
            row=i
        )


ledger_live_handler()
print('end :)')

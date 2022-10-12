from sheet2api import Sheet2APIClient
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_views_dataframe, get_view_data_dataframe
# import pandas as pd
# import numpy as np
# import time


def makes_ledger_live():

    s2a_client_write = Sheet2APIClient(
        api_url='https://sheet2api.com/v1/bSRF25UR2yBL/final_inventory',
        username='',
        password='',
    )

    s2a_client_read = Sheet2APIClient(
        api_url='https://sheet2api.com/v1/bSRF25UR2yBL/scannedinventory2',
        username='',
        password='',
    )

    xml_live = s2a_client_read.get_rows()

    tableau_server_config = {
        'tableau_prod': {
            'server': 'https://prod-useast-a.online.tableau.com/',
            'api_version': '3.16',
            'username': 'longdisdick27@gmail.com',
            'password': 'Bruh76%1',
            'site_name': 'bullish',
            'site_url': 'realinventory',
        }}

    conn = TableauServerConnection(tableau_server_config)
    conn.sign_in()

    view_data_df = get_view_data_dataframe(conn, view_id='8a03bff6-f3d8-459c-a6e2-32339a73014f')

    tab_product_table = view_data_df['Product']
    tab_qty_table = view_data_df['Measure Values']
    
    tab_proper_inventory = []

    for x in tab_product_table:
        row_id_product = view_data_df.index[view_data_df['Product'] == x].tolist()

        for y in tab_qty_table:
            row_id_qty = view_data_df.index[view_data_df['Measure Values'] == y].tolist()
            if row_id_product == row_id_qty:
                tab_proper_inventory.append({'product': x, 'qty': y})

    for itab in tab_proper_inventory:

        for ixml in xml_live:
            if itab['product'] == ixml['product']:
                ixml['qty'] = itab['qty'] + ixml['qty']
                ledger_live = xml_live
                break
            else:
                pass

    s2a_client_write.delete_rows(
        sheet='Sheet1'
    )

    for i in ledger_live:
        s2a_client_write.create_row(
            sheet='Sheet1',
            row=i
        )

    print('end :)')

if __name__ == '__makes_ledger_live__':
    makes_ledger_live()

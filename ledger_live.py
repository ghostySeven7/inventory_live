import time
from sheet2api import Sheet2APIClient
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_views_dataframe, get_view_data_dataframe
import pandas as pd

# test dictionaries
mock_xml = [
    {'product': 'cabernet', 'qty': 33},
    {'product': 'rose', 'qty': 66},
    {'product': 'bob jones', 'qty': 99}]

mock_tab = [
    {'product': 'mint mobile', 'qty': 100},
    {'product': 'cabernet', 'qty': 200},
    {'product': 'rose', 'qty': 300},
    {'product': 'bob jones', 'qty': 400},
    {'product': 'beer', 'qty': 21}]


s2a_client = Sheet2APIClient(
    api_url='https://sheet2api.com/v1/bSRF25UR2yBL/scannedinventory2',  # google sheets version
    username='',
    password='',
)


def ledger_merger_demo():
    for elm2 in mock_tab:

        for elm1 in mock_xml:
            data_sku_xml = elm1['product']
            data_qty_xml = elm1['qty']
            data_qty_tab = elm2['qty']
            if elm2['product'] == elm1['product']:
                elm1['product'] = data_sku_xml
                elm1['qty'] = data_qty_tab + data_qty_xml
                mock_live = mock_xml
                break
            else:
                pass

    print('ledger_live = ', mock_live)

    s2a_client.delete_rows(
        sheet='Sheet1'
    )

    for i in mock_live:
        s2a_client.create_row(
            sheet='Sheet1',
            row=i
        )


ledger_merger_demo()


# tableau shenanigans below

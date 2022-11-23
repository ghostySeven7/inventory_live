from sheet2api import Sheet2APIClient
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_view_data_dataframe


def makes_ledger_live():

    s2a_client_write = Sheet2APIClient(
        api_url='https://sheet2api.com/v1/bSRF25UR2yBL/final_inventory',  # google sheet
        username='',
        password='',
    )

    # pulls all data from shared pull sheet excel online. stores scanned inventory
    # xls_live = s2a_client_read.get_rows()
    # print('xls_live = ', xls_live)

    mock_xls = [
        {'product': 'cabernet', 'qty': 33},
        {'product': 'rose', 'qty': 66},
        {'product': 'bob jones', 'qty': 99}]

    mock_tab = [
        {'product': 'mint mobile', 'qty': 100},
        {'product': 'cabernet', 'qty': 200},
        {'product': 'rose', 'qty': 300},
        {'product': 'bob jones', 'qty': 400},
        {'product': 'beer', 'qty': 21}]

    # creates the final live_inventory[{}] then uploads it to final_inventory google sheet
    for itab in mock_tab:

        for ixls in mock_xls:
            if itab['product'] == ixls['product']:
                ixls['qty'] = itab['qty']
                ledger_live = mock_xls
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

    print('end :)')

    print('Finished :)')


makes_ledger_live()

from sheet2api import Sheet2APIClient
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_view_data_dataframe


def makes_ledger_live():

    s2a_client_write = Sheet2APIClient(
        api_url='https://sheet2api.com/v1/bSRF25UR2yBL/final_inventory',  # google sheet
        username='',
        password='',
    )

    s2a_client_read = Sheet2APIClient(
        api_url='https://sheet2api.com/v1/bSRF25UR2yBL/scanned-inventory',  # MS sheet :o
        username='',
        password='',
    )

    # pulls all data from shared pull sheet excel online. stores scanned inventory
    xls_live = s2a_client_read.get_rows()
    # print('xls_live = ', xls_live)

    tableau_server_config = {
        'tableau_prod': {
            'server': 'https://prod-useast-a.online.tableau.com/',
            'api_version': '3.17',  # here is where you update api version
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
    # print('tableau view data = ', view_data_df)

    # getting specific view data as tables
    tab_product_table = view_data_df['Product']
    tab_qty_table = view_data_df['Measure Values']

    # creating the final tab_proper_inventory[{}]
    tab_proper_inventory = []

    # reformats tableau data into [{}]
    for x in tab_product_table:
        row_id_product = view_data_df.index[view_data_df['Product'] == x].tolist()

        for y in tab_qty_table:
            row_id_qty = view_data_df.index[view_data_df['Measure Values'] == y].tolist()
            if row_id_product == row_id_qty:
                tab_proper_inventory.append({'product': x, 'qty': y})

    # print('tab_proper_inventory = ', tab_proper_inventory)

    # creates the final live_inventory[{}] then uploads it to final_inventory google sheet
    for itab in tab_proper_inventory:

        for ixls in xls_live:
            if itab['product'] == ixls['product']:
                ixls['qty'] = itab['qty']
                ledger_live = xls_live
                break
            else:
                pass

    # print('ledger_live = ', ledger_live)

    s2a_client_write.delete_rows(
        sheet='Sheet1'
    )

    for i in ledger_live:
        s2a_client_write.create_row(
            sheet='Sheet1',
            row=i
        )

    print('end :)')
    
    
makes_ledger_live()



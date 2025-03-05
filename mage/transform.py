import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df["Customer Country"] = df["Customer Country"].replace("EE. UU.", "USA")

    df["Customer State"] = df["Customer State"].replace({"95758": "CA", "91732": "CA"})

    date_columns = ["order date", "shipping date"]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col], format='%m/%d/%Y %H:%M').dt.strftime('%m-%d-%Y')

    df.columns = df.columns.str.replace(' ', '_').str.lower()

    fact_table = df[[
    "order_id",
    "customer_id",
    "product_card_id",
    "shipping_date",
    "shipping_mode",
    "days_for_shipping",
    "days_for_shipment",
    "sales_per_customer",
    "benefit_per_order",
    "type",
    "delivery_status",
    "late_delivery_risk",
    "order_item_discount",
    "order_item_discount_rate",
    "order_item_profit_ratio",
    "order_item_quantity",
    "department_name"]]
    
    dim_customer = df[[
    "customer_id",
    "customer_city",
    "customer_country",
    "customer_segment",
    "customer_state",
    "customer_street",
    "customer_zipcode"]].drop_duplicates().reset_index(drop=True)

    dim_product = df[[
    "product_card_id",
    "product_name",
    "product_price",
    "category_name"]].drop_duplicates().reset_index(drop=True)

    dim_order = df[['order_id',
   'order_date',
   'order_city',
   'order_country',
   'order_region',
   'order_state',
   'order_status',
   'latitude',
   'longitude',
   'market']].drop_duplicates().reset_index(drop=True)

    return [fact_table, dim_customer, dim_product, dim_order]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'


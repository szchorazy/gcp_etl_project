SELECT 
f.order_id,
f.product_card_id,
f.shipping_mode,
f.sales_per_customer,
f.benefit_per_order,
f.type,
f.delivery_status,
p.product_name,
p.category_name,
o.order_region,
o.order_status,
o.latitude,
o.longitude,
o.market
FROM `de-test-project-444415.supply_chain.fact_table` f
JOIN `de-test-project-444415.supply_chain.dim_product` p ON f.product_card_id = p.product_card_id
JOIN `de-test-project-444415.supply_chain.dim_order` o ON f.order_id = o.order_id
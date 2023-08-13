select
    order_year_month,
    payment_methods_payment_type,
    sum(charged_amt_usd)
from (with
        edco as
            (select
                distinct co_uuid,
                lc_to_usd_rate,
                concat (calendar_year_nbr, '-', calendar_month_of_year_nbr) as order_year_month
            from emea_direct_sales_prod.emea_direct_consumer_order
            where marketplace_type_cd = 'DIGITAL'
                and transaction_type_desc = 'SALES_ORDER'
                and calendar_year_nbr >= 2021
            ),
           charges as
           (select
                order_header_uuid,
                payment_methods_payment_type,
                sum (payment_methods_total_charged_amount) as payment_methods_total_charged_amount
           from consumption_secure.order_payment_clean_delta
           where payment_methods_total_charged_amount != 0
           group by 1,2
           )
       select
            co_uuid,
            order_year_month,
            payment_methods_payment_type,
            payment_methods_total_charged_amount * lc_to_usd_rate as charged_amt_usd
       from edco
       left join charges
       on co_uuid = order_header_uuid
     )
group by 1,2
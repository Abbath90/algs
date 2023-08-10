select
    order_year_month,
    tender_type_nm,
    sum(charged_amt_usd)
from (with
        edco as
            (select
                distinct co_uuid,
                lc_to_usd_rate,
                concat (calendar_year_nbr, '-', calendar_month_of_year_nbr) as order_year_month
            from emea_direct_sales_prod.emea_direct_consumer_order
            where marketplace_type_cd = 'B&M'
                and transaction_type_desc = 'SALES_ORDER'
                and calendar_year_nbr >= 2021
            ),
           charges as
           (select
                order_id,
                tender_type_nm,
                sum (case when tender_event_type_nm in ('Refund', 'CashRoundingDown')
                        then tender_local_currency_amt*(-1)
                        else tender_local_currency_amt end) as payment_methods_total_charged_amount
           from consumption_secure.bm_consumer_order_tender
           group by 1,2
           )
       select
            co_uuid,
            order_year_month,
            tender_type_nm,
            payment_methods_total_charged_amount * lc_to_usd_rate as charged_amt_usd
       from edco
       left join charges
       on co_uuid = order_id
     )
group by 1,2

    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

with all_values as (

    select
        refund_reason as value_field,
        count(*) as n_records

    from "shoesBR"."staging"."stg_estorno"
    group by refund_reason

)

select *
from all_values
where value_field not in (
    'Produto com defeito','Arrependimento','Entrega Atrasada','Produto Incorreto'
)



  
  
      
    ) dbt_internal_test
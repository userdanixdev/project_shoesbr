WITH source AS ( 
    SELECT * FROM {{source("landing","produtos")}}
),
renamed AS (
    SELECT
    CAST(product_id AS {{ dbt.type_string() }}) AS product_id,
    name as name_product,
    price as price_product
    FROM source
)

SELECT * FROM renamed
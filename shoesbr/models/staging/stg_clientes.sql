WITH source AS (
    SELECT * FROM {{source("landing", "clientes")}}
),

renamed as (
    SELECT CAST(customer_id AS {{ dbt.type_string() }}) AS customer_id,
    name AS customer_name,
    address AS customer_address,
    phone AS customer_phone,
    email AS customer_email
    FROM source
)
SELECT * FROM renamed
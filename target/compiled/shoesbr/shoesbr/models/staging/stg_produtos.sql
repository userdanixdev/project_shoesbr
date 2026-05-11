WITH source AS ( 
    SELECT * FROM "shoesBR"."landing"."produtos"
),
renamed AS (
    SELECT
    CAST(product_id AS TEXT) AS product_id,
    name as name_product,
    price as price_product
    FROM source
)

SELECT * FROM renamed
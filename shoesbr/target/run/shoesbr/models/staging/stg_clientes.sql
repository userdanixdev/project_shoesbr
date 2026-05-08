
  create view "shoesBR"."staging"."stg_clientes__dbt_tmp"
    
    
  as (
    WITH source AS (
    SELECT * FROM "shoesBR"."landing"."clientes"
),

renamed as (
    SELECT CAST(customer_id AS TEXT) AS customer_id,
    name AS customer_name,
    address AS customer_address,
    phone AS customer_phone,
    email AS customer_email
    FROM source
)
SELECT * FROM renamed
  );

  create view "shoesBR"."intermediate"."int_estorno__dbt_tmp"
    
    
  as (
    WITH source AS (
    SELECT *
    FROM "shoesBR"."staging"."stg_estorno"
)

SELECT * FROM source
  );
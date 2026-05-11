WITH source AS (

    SELECT * FROM "shoesBR"."landing"."estorno"

),

renamed AS (

    SELECT
        -- chaves
        CAST(purchase_id AS TEXT)   AS purchase_id,
        CAST(customer_id AS TEXT)   AS customer_id,
        CAST(product_id AS TEXT)    AS product_id,

        -- métricas
        CAST(refund_amount AS numeric(28,6)) AS refund_amount,

        -- dimensões
        CAST(refund_reason AS TEXT)  AS refund_reason,

        -- datas
        CAST(refund_date AS timestamp) AS refund_date,

        -- controle
        now() AS _loaded_at

    FROM source

)

SELECT * FROM renamed
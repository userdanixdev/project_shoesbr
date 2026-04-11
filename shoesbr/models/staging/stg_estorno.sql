WITH source AS (

    SELECT * FROM {{ ref('estorno') }}

),

renamed AS (

    SELECT
        -- chaves
        CAST(purchase_id AS {{ dbt.type_string() }})   AS purchase_id,
        CAST(customer_id AS {{ dbt.type_string() }})   AS customer_id,
        CAST(product_id AS {{ dbt.type_string() }})    AS product_id,

        -- métricas
        CAST(refund_amount AS {{ dbt.type_numeric() }}) AS refund_amount,

        -- dimensões
        CAST(refund_reason AS {{ dbt.type_string() }})  AS refund_reason,

        -- datas
        CAST(refund_date AS {{ dbt.type_timestamp() }}) AS refund_date,

        -- controle
        {{ dbt.current_timestamp() }} AS _loaded_at

    FROM source

)

SELECT * FROM renamed
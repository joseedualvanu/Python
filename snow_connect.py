def snow_connect(CONFIG, file_keyP8):

    from snowflake import connector
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization

    print('Connect to Snow')

    with open(file_keyP8, "rb") as key:
        p_key = serialization.load_pem_private_key(
            key.read(),
            password=None,
            backend=default_backend()
        )

    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    conn = connector.connect(
        user=CONFIG['snowflake']['user'],
        account=CONFIG['snowflake']['account'],
        private_key=pkb,
        warehouse=CONFIG['snowflake']['wh'],
        database=CONFIG['snowflake']['db'],
        schema=CONFIG['snowflake']['schema']
    )

    cur = conn.cursor()
    return cur

def upload_file_snow(cur, file_name, stage_name, table_name):
    print('Upload file to Snowflake')
    
    cur.execute(f'DELETE FROM ODS.AWS.{table_name}')
    cur.execute(f'CREATE TEMPORARY STAGE {stage_name}')
    cur.execute(f'PUT file://{file_name} @{stage_name}')
    cur.execute(f'COPY INTO {table_name} FROM @{stage_name}/stage_file.csv.gz ON_ERROR = "CONTINUE"')
    cur.execute('COMMIT')
    cur.close()
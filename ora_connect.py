def oracle_connect(CONFIG, ora_lib):
    import cx_Oracle
    from sqlalchemy import create_engine

    print('Connect to Oracle')
    try:
        cx_Oracle.init_oracle_client(lib_dir=ora_lib)
    except cx_Oracle.ProgrammingError:
        print('Oracle Client library has already been initialized')

    engine = create_engine('oracle://{}:{}@{}:{}/{}'.format(
        CONFIG['oracle']['username'],
        CONFIG['oracle']['password'],
        CONFIG['oracle']['hostname'],
        CONFIG['oracle']['port'],
        CONFIG['oracle']['service_name']
    ))

    return engine
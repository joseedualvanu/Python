
def c_aws_put(direction,log_name,file_name,bucket_name,s3_key):
    
    print('AWS put s3')
    import os
    import boto3
    from datetime import date
    
    access_key_id ='access_key_id'
    secret_access_key = 'secret_access_key'
    
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key
    )
    
    file_name = 'file.csv'
    
    # Specify the S3 bucket name
    bucket_name = 'bucket_name'
    

    try:
        s3.upload_file(file_name, bucket_name, s3_key)
        print(f"File '{file_name}' uploaded successfully to S3 bucket '{bucket_name}' with key '{s3_key}'.")
    except Exception as e:
        print(f"Error uploading file to S3: {str(e)}")
#!/usr/bin/env python
"""
    set_s3_cache_headers
    
    :copyright: by trips45.com
    :license: MIT
"""


from boto.s3.connection import S3Connection

#--- AWS credentials ----------------------------------------------
AWS_KEY = '...'
AWS_SECRET = '...'
AWS_BUCKET_NAME = '...'

#--- Main function ----------------------------------------------
def main():
    s3_conn = S3Connection(AWS_KEY, AWS_SECRET)

    bucket = s3_conn.get_bucket(AWS_BUCKET_NAME)

    bucket.make_public()

    for key in bucket.list():
        
        key = bucket.get_key(key.name)
        key.cache_control = 'max-age=%d, public' % (3600 * 24 * 360 * 2)
        print key.name + ' ' +  key.cache_control

if __name__ == '__main__':
    main()

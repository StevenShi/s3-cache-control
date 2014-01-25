#!/usr/bin/env python
"""
    set_s3_cache_headers
    
    :copyright: by trips45.com
    :license: MIT
"""


from boto.s3.connection import S3Connection
from boto.cloudfront import CloudFrontConnection


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
        
        print key.name

        aggressive_headers = _get_aggressive_cache_headers(key)

        key.copy(AWS_BUCKET_NAME, key, metadata=aggressive_headers, preserve_acl=True)


#--- Helpers ----------------------------------------------
def _get_aggressive_cache_headers(key):
    metadata = key.metadata

    metadata['Content-Type'] = key.content_type

    metadata['Cache-Control'] = 'max-age=%d, public' % (3600 * 24 * 360)

    return metadata


if __name__ == '__main__':
    main()
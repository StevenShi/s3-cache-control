s3-cache-control
================
S3 does not set a default cache-control header, which means files you upload won’t be cached in the browser by default.

It is amazingly obscure how to do something as simple as setting the cache-control key in Amazon S3. The [boto document](http://boto.s3.amazonaws.com/ref/s3.html) seems to imply you could do this via key.set_metadata, but no, that won’t work because that method only updates an existing meta key.

To add a new metadata key value pair to an S3 object, the correct way is to use key.copy. I wrote the following program to do that.

First, you need to install boto.

<code>pip install boto </code>

Next, download set_s3_cache_header.py, modified the script to add in your AWS credential and bucket name, then run it:

<code>python set_s3_cache_header.py</code>


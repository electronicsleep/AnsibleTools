#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 07/20/2017
# Purpose: Get all s3 buckets
# Released under the BSD license

import boto3

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

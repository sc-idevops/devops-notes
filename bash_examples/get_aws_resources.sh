#!/bin/bash
aws resourcegroupstaggingapi get-resources | jq -r '.ResourceTagMappingList[].ResourceARN'
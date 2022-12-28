#!/bin/bash
#replace a formatted configuration file. note the file must contain \n on the front of each line to properly format the output in this example
echo -e $(envsubst < test.conf) > test.conf && cat test.conf
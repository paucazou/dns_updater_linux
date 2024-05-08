#!/bin/zsh

# get current ipv6 addr
ip=$(ip r get to 2001:4860:4860::8888 | perl -ne '/src ([\w:]+)/ && print "$1\n"')
print Current ip: $ip

# update
python3 dns_updater.py $ip

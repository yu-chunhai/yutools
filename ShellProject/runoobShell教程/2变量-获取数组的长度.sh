#!/bin/bash
#失败
#定义数组
array_name=(1 2 3 3)
#读取数组
echo ${array_name[0]}
length=${#array_name[@]}
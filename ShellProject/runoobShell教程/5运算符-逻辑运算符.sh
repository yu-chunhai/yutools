#!/bin/bash
#&&	�߼��� AND	[[ $a -lt 100 && $b -gt 100 ]] ���� false
#||	�߼��� OR	[[ $a -lt 100 || $b -gt 100 ]] ���� true

a=10
b=20

if [[ $a -lt 100 && $b -gt 100 ]]
then
   echo "���� true"
else
   echo "���� false"
fi

if [[ $a -lt 100 || $b -gt 100 ]]
then
   echo "���� true"
else
   echo "���� false"
fi
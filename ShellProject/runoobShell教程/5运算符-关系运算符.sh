#!/bin/bash
#-eq	����������Ƿ���ȣ���ȷ��� true��	[ $a -eq $b ] ���� false��
#-ne	����������Ƿ���ȣ�����ȷ��� true��	[ $a -ne $b ] ���� true��
#-gt	�����ߵ����Ƿ�����ұߵģ�����ǣ��򷵻� true��	[ $a -gt $b ] ���� false��
#-lt	�����ߵ����Ƿ�С���ұߵģ�����ǣ��򷵻� true��	[ $a -lt $b ] ���� true��
#-ge	�����ߵ����Ƿ���ڵ����ұߵģ�����ǣ��򷵻� true��	[ $a -ge $b ] ���� false��
#-le	�����ߵ����Ƿ�С�ڵ����ұߵģ�����ǣ��򷵻� true��	[ $a -le $b ] ���� true��

a=10
b=20

if [ $a -eq $b ]
then
   echo "$a -eq $b : a ���� b"
else
   echo "$a -eq $b: a ������ b"
fi

if [ $a -ne $b ]
then
   echo "$a -ne $b: a ������ b"
else
   echo "$a -ne $b : a ���� b"
fi

if [ $a -gt $b ]
then
   echo "$a -gt $b: a ���� b"
else
   echo "$a -gt $b: a ������ b"
fi

if [ $a -lt $b ]
then
   echo "$a -lt $b: a С�� b"
else
	echo "$a -lt $b: a ��С�� b"
fi

if [ $a -ge $b ]
then
   echo "$a -ge $b: a ���ڻ���� b"
else
   echo "$a -ge $b: a С�� b"
fi

if [ $a -le $b ]
then
   echo "$a -le $b: a С�ڻ���� b"
else
   echo "$a -le $b: a ���� b"
fi
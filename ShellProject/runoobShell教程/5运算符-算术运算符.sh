#!/bin/bash
#+	�ӷ�	`expr $a + $b` ���Ϊ 30��
#-	����	`expr $a - $b` ���Ϊ -10��
#*	�˷�	`expr $a \* $b` ���Ϊ  200��
#/	����	`expr $b / $a` ���Ϊ 2��
#%	ȡ��	`expr $b % $a` ���Ϊ 0��
#=	��ֵ	a=$b ���ѱ��� b ��ֵ���� a��
#==	��ȡ����ڱȽ��������֣���ͬ�򷵻� true��	[ $a == $b ] ���� false��
#!=	����ȡ����ڱȽ��������֣�����ͬ�򷵻� true��	[ $a != $b ] ���� true��

a=10
b=20
val=`expr $a + $b`;echo "a + b : $val"
val=`expr $a - $b`;echo "a - b : $val"
val=`expr $a \* $b`;echo "a * b : $val"
val=`expr $b / $a`;echo "b / a : $val"
val=`expr $b % $a`;echo "b % a : $val"
if [ $a == $b ]
then
   echo "a ���� b"
fi

if [ $a != $b ]
then
   echo "a ������ b"
fi
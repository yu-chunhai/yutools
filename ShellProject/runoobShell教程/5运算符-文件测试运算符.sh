#!/bin/bash
#-b file	����ļ��Ƿ��ǿ��豸�ļ�������ǣ��򷵻� true��	[ -b $file ] ���� false��
#-c file	����ļ��Ƿ����ַ��豸�ļ�������ǣ��򷵻� true��	[ -c $file ] ���� false��
#-d file	����ļ��Ƿ���Ŀ¼������ǣ��򷵻� true��	[ -d $file ] ���� false��
#-f file	����ļ��Ƿ�����ͨ�ļ����Ȳ���Ŀ¼��Ҳ�����豸�ļ���������ǣ��򷵻� true��	[ -f $file ] ���� true��
#-g file	����ļ��Ƿ������� SGID λ������ǣ��򷵻� true��	[ -g $file ] ���� false��
#-k file	����ļ��Ƿ�������ճ��λ(Sticky Bit)������ǣ��򷵻� true��	[ -k $file ] ���� false��
#-p file	����ļ��Ƿ��������ܵ�������ǣ��򷵻� true��	[ -p $file ] ���� false��
#-u file	����ļ��Ƿ������� SUID λ������ǣ��򷵻� true��	[ -u $file ] ���� false��
#-r file	����ļ��Ƿ�ɶ�������ǣ��򷵻� true��	[ -r $file ] ���� true��
#-w file	����ļ��Ƿ��д������ǣ��򷵻� true��	[ -w $file ] ���� true��
#-x file	����ļ��Ƿ��ִ�У�����ǣ��򷵻� true��	[ -x $file ] ���� true��
#-s file	����ļ��Ƿ�Ϊ�գ��ļ���С�Ƿ����0������Ϊ�շ��� true��	[ -s $file ] ���� true��
#-e file	����ļ�������Ŀ¼���Ƿ���ڣ�����ǣ��򷵻� true��	[ -e $file ] ���� true��

file="/var/www/runoob/test.sh"
if [ -r $file ]
then
   echo "�ļ��ɶ�"
else
   echo "�ļ����ɶ�"
fi
if [ -w $file ]
then
   echo "�ļ���д"
else
   echo "�ļ�����д"
fi
if [ -x $file ]
then
   echo "�ļ���ִ��"
else
   echo "�ļ�����ִ��"
fi
if [ -f $file ]
then
   echo "�ļ�Ϊ��ͨ�ļ�"
else
   echo "�ļ�Ϊ�����ļ�"
fi
if [ -d $file ]
then
   echo "�ļ��Ǹ�Ŀ¼"
else
   echo "�ļ����Ǹ�Ŀ¼"
fi
if [ -s $file ]
then
	echo "�ļ���Ϊ��"
else
   echo "�ļ�Ϊ��"
fi
if [ -e $file ]
then
   echo "�ļ�����"
else
   echo "�ļ�������"
fi

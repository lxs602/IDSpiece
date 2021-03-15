#! /bin/sh
TMP=/tmp/makecjk$$
trap "rm -f $TMP ; exit 2" 1 2 3 15
echo 'cjk3={}' > cjk3.py
echo 'cjk2={}' > cjk2.py
echo 'cjk1={}' > cjk1.py
echo 'cjk0={}' > cjk0.py

for N in 1 2 3
do ( echo '# coding=utf-8' ; echo 'cjk3={' ) > $TMP
   cat IDS-UCS-Ext-G.txt | python3 txt2py.py >> $TMP
   echo '} # end' >> $TMP
   mv $TMP cjk3.py

   ( echo '# coding=utf-8' ; echo 'cjk2={' ) > $TMP
   cat IDS-UCS-Ext-[BCDEF]*.txt IDS-UCS-Compat-Supplement.txt | python3 txt2py.py >> $TMP
   echo '} # end' >> $TMP
   mv $TMP cjk2.py

   ( echo '# coding=utf-8' ; echo 'cjk1={' ) > $TMP
   cat IDS-UCS-Ext-A.txt IDS-UCS-Compat.txt | python3 txt2py.py >> $TMP
   echo '} # end' >> $TMP
   mv $TMP cjk1.py

   ( echo '# coding=utf-8' ; echo 'cjk0={' ) > $TMP
   cat IDS-UCS-Basic.txt | python3 txt2py.py >> $TMP
   echo '} # end' >> $TMP
   mv $TMP cjk0.py
done

exit 0

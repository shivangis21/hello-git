import re
#Q1
emails="zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
k=re.findall(r'([a-z]+\d+)@([a-z]+).([a-z]+m)',emails)
print(k)

#q2
aa = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
l=re.findall(r'[bB]\w+',aa)
print(l)

bb=",;_"
s = "A, very very; irregular_sentence"
for c in bb:
 s=s.replace(c,' ')
 s.split()
print(s)
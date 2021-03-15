#! /usr/bin/python3
# coding=utf-8
rev={}
from cjk3 import cjk3
for c in reversed(cjk3):
  rev[cjk3[c]]=c
from cjk2 import cjk2
for c in reversed(cjk2):
  rev[cjk2[c]]=c
from cjk1 import cjk1
for c in reversed(cjk1):
  rev[cjk1[c]]=c
from cjk0 import cjk0
for c in reversed(cjk0):
  rev[cjk0[c]]=c
ids=["⿰","⿱","⿴","⿵","⿶","⿷","⿸","⿹","⿺"]
rad={}
with open("radicals.txt","r",encoding="utf-8") as f:
  r=f.read()
for s in r.split("\n"):
  t=s.split()
  if len(t)==3:
    rad[t[2]+t[1]]=t[2]+t[0]
  elif len(t)==2:
    if "⿰"+t[1] not in rad:
      for i in ids:
        rad[i+t[1]]=i+t[0]
samechar={}
with open("samechar.txt","r",encoding="utf-8") as f:
  r=f.read()
for s in r.split("\n"):
  t=s.split()
  if len(t)==2:
    samechar[t[0]]=t[1]
ampersand={}
with open("ampersand.txt","r",encoding="utf-8") as f:
  r=f.read()
for s in r.split("\n"):
  t=s.split()
  if len(t)==2:
    ampersand[t[0]]=t[1]
while True:
  try:
    s=input()
  except:
    quit()
  if not s.startswith(";;"):
    i=s.find("&")
    while i>=0:
      j=s.find(";",i)
      t=s[i:j+1]
      if t in ampersand:
        s=s.replace(t,ampersand[t])
      else:
        i=j
      i=s.find("&",i)
    t=s.strip().split()
    m=t[2]
    for r in samechar:
      m=m.replace(r,samechar[r])
    if m.startswith("⿲") and len(m)==4:
      m="⿰"+m[1]+"⿰"+m[2:]
    if m.startswith("⿳") and len(m)==4:
      m="⿱"+m[1]+"⿱"+m[2:]
    for r in rad:
      m=m.replace(r,rad[r])
    c=False
    if len(m)==1 and m!=t[1]:
      if ord(m)<65536:
        if m in cjk0:
          m=cjk0[m]
        elif m in cjk1:
          m=cjk1[m]
      elif m in cjk2:
        m=cjk2[m]
      elif m in cjk3:
        m=cjk3[m]
    if len(m)==3:
      if m[0] in ids:
        if ord(m[1])<40960:
          if ord(m[2])>13311 and ord(m[2])<40960:
            c=True
          elif m[2] in cjk2:
            c=True
          elif m[2] in cjk3:
            c=True
    elif len(m)==5:
      if m[0] in ids and ord(m[1])<40960:
        if m[2:] in rev:
          m=m[0:2]+rev[m[2:]]
          c=True
    if c:
      print("  \""+t[1]+"\":\""+m+"\", # "+t[0].replace("U-000","U+"))
    else:
      print("  #\""+t[1]+"\":\""+m+"\", # "+t[0].replace("U-000","U+"))


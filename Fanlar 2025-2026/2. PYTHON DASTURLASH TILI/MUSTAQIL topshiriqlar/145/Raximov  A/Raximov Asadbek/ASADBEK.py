# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:00:38 2024

@author: User
"""

n,k=map(int,input().split())
a=list(map(int,input().split()))
a=a[k:]
for i in range(k,n+1):
    a.append(0)
    
print(a)

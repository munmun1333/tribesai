{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 class Solution(object):\
\'a0 \'a0 def isMatch(self, s, p):\
\'a0 \'a0 \'a0 \'a0 \'a0 WC = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]\
\'a0 \'a0 \'a0 \'a0 \'a0 WC[-1][-1] = True\
\'a0 \'a0 \'a0 \'a0 \'a0 for i in range(len(s), -1, -1):\
			\'a0 for j in range(len(p) - 1, -1, -1):\
				\'a0 if i<len(s) and p[j] == '*':\
					WC[i][j] = WC[i+1][j] or WC[i][j+1]\
				\'a0 elif i<len(s) and p[j] == '?':\
					\'a0 \'a0 WC[i][j] = WC[i+1][j+1]\
				\'a0 elif i<len(s) and j<len(p):\
					\'a0 \'a0 \'a0WC[i][j] = s[i] == p[j] and WC[i+1][j+1]\
				\'a0 else:\'a0\
					\'a0 \'a0 WC[i][j] = p[j] == '*' and WC[i][j+1]\
\'a0 \'a0 \'a0 \'a0 \'a0 return WC[0][0]\
}
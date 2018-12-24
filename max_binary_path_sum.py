{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 ArialMT;}
{\colortbl;\red255\green255\blue255;\red26\green26\blue26;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28300\viewh14680\viewkind0
\deftab720
\pard\pardeftab720\sl220\partightenfactor0

\f0\fs20 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Definition for a binary tree node.\
# class TreeNode(object):\
#\'a0 \'a0 \'a0def __init__(self, x):\
#\'a0 \'a0 \'a0 \'a0 \'a0self.val = x\
#\'a0 \'a0 \'a0 \'a0 \'a0self.left = None\
#\'a0 \'a0 \'a0 \'a0 \'a0self.right = None\
\pard\pardeftab720\sl220\partightenfactor0
\cf2 \cb1 \
\pard\pardeftab720\sl220\partightenfactor0
\cf2 \cb3 class Solution(object):\
\'a0 \'a0 \'a0 \'a0 def maxPathSum(self, root):\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 """\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0:type root: TreeNode\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0:rtype: int\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 """\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 self.result = float("-inf")\'a0\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 self.findMaxPathUtil(root)\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 return self.result\
\pard\pardeftab720\sl220\partightenfactor0
\cf2 \cb1 \
\pard\pardeftab720\sl220\partightenfactor0
\cf2 \cb3 \'a0 \'a0 \'a0 \'a0 def findMaxPathUtil(self,root):\'a0\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 if root is None:\'a0\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 \'a0 return 0\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 #root_val=root.val\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 sum_left = self.findMaxPathUtil(root.left)\'a0\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 sum_right= self.findMaxPathUtil(root.right)\'a0\
\'a0 \'a0 \'a0 \'a0\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 single_max = max(sum_left+root_data,sum_right+root_data, root_data)\'a0\
\'a0 \'a0\'a0\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 self.result = max(self.result, single_max, sum_left+sum_right+ root_data)\
\'a0 \'a0 \'a0 \'a0 \'a0 \'a0 return single_max\
}
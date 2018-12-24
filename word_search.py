{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28300\viewh14680\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution(object):\
    def findWords(self, board, words):\
        """\
        :type board: List[List[str]]\
        :type words: List[str]\
        :rtype: List[str]\
        """\
        trie = self.Trie(words)\
        self.res = []\
        for i in range(len(board)):\
            for j in range(len(board[0])):\
                self.DFS(board, i, j, trie)\
        return self.res\
    \
    def DFS(self, board, i, j, trie):\
        # found one\
        if trie.get('word'):\
            self.res.append(trie['word'])\
            # de-duplicate\
            trie['word'] = None\
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] not in trie:\
            return\
        c, board[i][j] = board[i][j], '#'\
        self.DFS(board, i-1, j, trie[c])\
        self.DFS(board, i+1, j, trie[c])\
        self.DFS(board, i, j-1, trie[c])\
        self.DFS(board, i, j+1, trie[c])\
        board[i][j] = c\
    \
    def Trie(self, words):\
        trie = \{\}\
        for word in words:\
            cur = trie\
            for char in word:\
                cur = cur.setdefault(char, \{\})\
            cur['word'] = word\
        return trie}
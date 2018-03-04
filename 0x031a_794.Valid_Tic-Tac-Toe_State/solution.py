import numpy as np

def count(arr, ele):
    return np.sum(arr == ele)    

def threes(arr, ele):
    c = 0
    for row in arr:
        if filled(row, ele):
            c+=1
    for col in arr.T:
        if filled(col, ele):
            c+=1
    if all(arr[i, i] == ele for i in range(3)): c += 1
    if all(arr[i, 2-i] == ele for i in range(3)): c += 1
    return c

def filled(arr, ele):
    return len(arr) == int(np.sum(arr == ele))

class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        d = {' ': 0, 'X': 1, 'O': 2}
        board_arr = np.array([[d[ele] for ele in row] for row in board])
        Xs = count(board_arr, 1)
        Os = count(board_arr, 2)
        
        if Xs - Os not in [0, 1]: return False
        
        Xwins = threes(board_arr, 1) 
        Owins = threes(board_arr, 2)
        
        if Xwins > 1 or Owins > 1: return False
        if Xwins * Owins > 0: return False
        
        if Xwins == 1:
            if Xs - Os == 1: return True
            else: return False
        if Owins == 1:
            if Xs - Os == 0: return True
            else: return False
        return True
        
        
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def stairs(n,memo={}):
    if n==1:
        memo[n]=1
        return 1
    

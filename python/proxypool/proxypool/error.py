class PoolEmptyError(Exception):
    def __init__(self):
        super(PoolEmptyError, self).__init__()
    
    def __str__(self):
        return ('代理池已枯竭！')
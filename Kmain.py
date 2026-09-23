class Kmean:
    def __init__(self, nb_cluster, nb_iter):
        self.nb_cluster = nb_cluster
        self.nb_iter = nb_iter
    def fit (self,data) #data = [[x,,y],[x,,y],]
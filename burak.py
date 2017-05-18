import sys, math, operator, pandas

def oklit(a, b):
    uzaklik = [(x - y)**2 for x, y in zip(a, b)]
    uzaklik = math.sqrt( sum( uzaklik ) )
    return uzaklik

class burakKNN():
    def fit(self, X, y):
        self.X = X
        self.y = y
    def tahmin(self, X_test, k = 3):
        tahminler = []
        for uzaklik in X_test:
            tahmin = self.enYakin( uzaklik, k )
            tahminler.append( tahmin )
        return tahminler
    def enYakin(self, row, k):
        uzakliklar = []
        for i in range(0, len(self.X)):
            uzaklik = oklit(row, self.X[i])
            uzakliklar.append((uzaklik, i))
        uzakliklar.sort(key = operator.itemgetter(0))
        # print uzakliklar
        if k > 1:
            k_list = []
            for j in range(0, k):
                k_list.append(self.y[uzakliklar[j][1]])
            k_list = pandas.DataFrame(k_list)
            return k_list.mode()[0][0]
            # return k_list
        else:
            enIyiUzaklik            = oklit(row, self.X[ 0 ])
            enIyi_index             = 0
            for i in range(1, len( self.X ) ):
                uzaklik             = oklit(row, self.X[ i ])
                if uzaklik < enIyiUzaklik:
                    enIyiUzaklik    = uzaklik
                    enIyi_index     = i
            return self.y[ enIyi_index ]

veri = pandas.read_csv("hava.txt", header = None)
X, y = veri[[0, 1]], veri[2]
X, y = X.values, y.values

X_test = [[78,73],[75,89]]
siniflandirma = burakKNN()
siniflandirma.fit(X, y)
predictions = siniflandirma.tahmin(X_test, k = 3)
print predictions

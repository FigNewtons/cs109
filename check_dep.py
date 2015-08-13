
if __name__ == '__main__':

    try:
        import IPython
        import numpy as np, scipy as sp, pandas as pd
        import matplotlib, sklearn
        import requests, networkx as nx
        import bs4, mrjob, pattern, seaborn

        check = [ IPython.__version__ >= '1.0' , 
                  np.__version__ >= '1.7.1',
                  sp.__version__ >= '0.12.0',
                  pd.__version__ >= '0.11.0',
                  matplotlib.__version__ >= '1.2.1',
                  requests.__version__ >= '1.2.3',
                  nx.__version__ >= '1.7',
                  bs4.__version__ >= '4.0',
                  mrjob.__version__ >= '0.4',
                  pattern.__version__ >= '2.6',
                  seaborn.__version__ >= '0.3.1' ]

        print('IPython version >= 1.0 : ' + check[0])
        print('Numpy version >= 1.7.1 : ' + check[1])
        print('Scipy version >= 0.12.0 : ' + check[2])
        print('Pandas version >= 0.11.0 : ' + check[3])
        print('Matplotlib version >= 1.2.1 : ' + check[4])
        print('requests version >= 1.2.3 : ' + check[5])
        print('networkx version >= 1.7 : ' + check[6])
        print('Beautiful soup version >= 4.0 : ' + check[7])
        print('mrjob version >= 0.4 : ' + check[8])
        print('pattern version >= 2.6 : ' + check[9])
        print('seaborn version >= 0.3.1 : ' + check[10])

        if all(check):
            print('All of your packages are up-to-date!')
        else:
            print('Update all packages marked "False" to the correct version.')

    except ImportError as e:
        print('Package not installed: ', e)

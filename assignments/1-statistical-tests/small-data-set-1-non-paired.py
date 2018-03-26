import matplotlib
import pandas as pd
import scipy.stats
from sacred import Experiment

matplotlib.use('agg')

from matplotlib import pyplot


ex = Experiment('small-data-set-1-non-paired')


@ex.config
def my_config():
    datasets = ['data/a1.csv', 'data/b1.csv']


@ex.automain
def main(datasets):
    a1, b1 = (pd.read_csv(d, header=None, names=['measure']) for d in datasets)

    s, p = (e[0] for e in scipy.stats.ttest_ind(a1, b1, equal_var=False))
    print('p-value from t-test:', p)

    s, p = scipy.stats.ranksums(a1, b1)
    print('p-value from Wilcoxon rank sum test:', p)

    pa1, = pyplot.plot(a1, label='A1')
    pb1, = pyplot.plot(b1, label='B1')
    pyplot.legend(handles=[pa1, pb1])
    pyplot.tight_layout()
    pyplot.savefig('a1-b1.png')

import matplotlib
import pandas as pd
import scipy.stats
from sacred import Experiment

matplotlib.use('agg')

from matplotlib import pyplot


ex = Experiment('small-data-set-2-paired')


@ex.config
def my_config():
    dataset = 'data/paired.csv'


@ex.automain
def main(dataset):
    d = pd.read_csv(dataset, header=None, names=['a', 'b'])
    s, p = scipy.stats.ttest_rel(d['a'], d['b'])
    print('p-value from paired t-test:', p)

    s, p = scipy.stats.ttest_ind(d['a'], d['b'], equal_var=False)
    print('p-value from t-test:', p)

    s, p = scipy.stats.wilcoxon(d['a'], d['b'])
    print('p-value from Wilcoxon signed rank-test:', p)

    s, p = scipy.stats.ranksums(d['a'], d['b'])
    print('p-value from Wilcoxon rank sums test:', p)

    pa1, = pyplot.plot(d['a'], label='A')
    pb1, = pyplot.plot(d['b'], label='B')
    pyplot.legend(handles=[pa1, pb1])
    pyplot.tight_layout()
    pyplot.savefig('paired.png')

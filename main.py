import matplotlib
matplotlib.use('TkAgg')
from runs import KNNRuns,DMCRuns,BayesianGaussianDiscriminantRuns


def main():
    for i in range(5):
        BayesianGaussianDiscriminantRuns(i)
if __name__ == "__main__":
    main()

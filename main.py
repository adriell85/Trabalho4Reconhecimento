import matplotlib
matplotlib.use('TkAgg')
from runs import KNNRuns,DMCRuns,BayesianGaussianDiscriminantRuns


def main():
    BayesianGaussianDiscriminantRuns(0)
    # for i in range(5):
    #     BayesianGaussianDiscriminantRuns(i)
if __name__ == "__main__":
    main()

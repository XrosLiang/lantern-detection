# Import the required modules
# coding:utf-8
from skimage.feature import local_binary_pattern
from sklearn import cross_validation
from sklearn.decomposition import pca
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.calibration import CalibratedClassifierCV
import argparse as ap
import glob
import os
from config import *
import numpy as np

if __name__ == "__main__":
    # Parse the command line arguments
    parser = ap.ArgumentParser()
    parser.add_argument('-p', "--posfeat", help="Path to the positive features directory",
                        default='/home/gongxijun/data/features/pos')
    parser.add_argument('-n', "--negfeat", help="Path to the negative features directory",
                        default='/home/gongxijun/data/features/neg')
    parser.add_argument('-c', "--classifier", help="Classifier to be used", default="LIN_SVM")
    args = vars(parser.parse_args())

    pos_feat_path = args["posfeat"]
    neg_feat_path = args["negfeat"]

    # Classifiers supported
    clf_type = args['classifier']

    fds = []
    labels = []
    # Load the positive features
    for feat_path in glob.glob(os.path.join(pos_feat_path, "*.feat")):
        print feat_path
        fd = joblib.load(feat_path)
        fds.append(fd)
        labels.append(1)
        # print np.array(fds).shape, len(labels)

    for feat_path in glob.glob(os.path.join(neg_feat_path, "*.feat")):
        print feat_path
        fd = joblib.load(feat_path)
        fds.append(fd)
        labels.append(0)
        # print np.array(fds).shape, len(labels)

    print np.array(fds).shape, len(labels)
    if __name__ == '__main__':
        if clf_type is "LIN_SVM":
            svm = LinearSVC(C=300, max_iter=50000)
            clf = CalibratedClassifierCV(svm)
            print "Training a Linear SVM Classifier"
            # pca_class = pca.PCA(n_components='mle', copy=False)
            # fds = pca_class.fit_transform(fds)  # 增加pca主成分分析
            print np.array(fds).shape, len(labels)
            clf.fit(fds, labels)
            # If feature directories don't exist, create them
            if not os.path.isdir(os.path.split(model_path)[0]):
                os.makedirs(os.path.split(model_path)[0])
            joblib.dump(clf, model_path)
            print "Classifier saved to {}".format(model_path)
            # 交叉验证
            scores = cross_validation.cross_val_score(clf, fds, labels, cv=10)
            print scores

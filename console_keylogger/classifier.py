import numpy as np
import pandas as pd
import os

from sklearn.metrics import matthews_corrcoef
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier


def uni_parse():
    df_list = []

    cols = ['.', 't', 'i', 'e', '5', 'Key.shift', 'R', 'o', 'a', 'n', 'l', 'Key.enter']

    for file_name in os.listdir("data/uni"):
        temp = pd.read_csv("data/uni/" + file_name)
        n = len(temp.columns) - len(cols)
        temp.drop(temp.columns[:n], axis=1, inplace=True)
        temp.columns = cols
        temp.reset_index(drop=True, inplace=True)
        df_list.append(temp)
        print(temp)

    df_uni = pd.concat(df_list)
    df_uni["Target"] = np.ones(df_uni.shape[0], dtype=np.int)
    my_df = pd.read_csv("self_data/Olshanyy_uni.csv")
    my_df.drop(my_df.columns[:1], inplace=True, axis=1)
    my_df["Target"] = np.zeros(my_df.shape[0], dtype=np.int)
    unigram = pd.concat([my_df, df_uni])
    unigram.index = np.arange(1, unigram.shape[0]+1)
    print("uni")
    print(unigram)
    print()
    return unigram


def bio_parse():
    df_list = []

    col = ['.', 't', 'i', 'e', '5', 'Key.shift', 'R', 'o', 'a', 'n', 'l', 'Key.enter']
    cols = []

    for i in range(len(col) - 1):
        cols.append(f"{col[i]}-{col[i+1]}")

    for file_name in os.listdir("data/bio"):
        temp = pd.read_csv("data/bio/" + file_name)
        n = len(temp.columns) - len(cols)
        temp.drop(temp.columns[:n], axis=1, inplace=True)
        temp.columns = cols
        temp.reset_index(drop=True, inplace=True)
        df_list.append(temp)

    df_bi = pd.concat(df_list)
    df_bi["Target"] = np.ones(df_bi.shape[0], dtype=np.int)
    my_df = pd.read_csv("self_data/Olshanyy_bio.csv")
    my_df.drop(my_df.columns[:1], inplace=True, axis=1)
    my_df["Target"] = np.zeros(my_df.shape[0], dtype=np.int)
    bigram = pd.concat([my_df, df_bi])
    bigram.index = np.arange(1, bigram.shape[0] + 1)
    print("data/bio")
    print(bigram)
    print()
    return bigram


def trio_parse():
    df_list = []

    col = ['.', 't', 'i', 'e', '5', 'Key.shift', 'R', 'o', 'a', 'n', 'l', 'Key.enter']
    cols = []

    for i in range(len(col) - 2):
        cols.append(f"{col[i]}-{col[i + 2]}")

    for file_name in os.listdir("data/trio"):
        temp = pd.read_csv("data/trio/" + file_name)
        n = len(temp.columns) - len(cols)
        temp.drop(temp.columns[:n], axis=1, inplace=True)
        temp.columns = cols
        temp.reset_index(drop=True, inplace=True)
        df_list.append(temp)

    df_tri = pd.concat(df_list)
    df_tri["Target"] = np.ones(df_tri.shape[0], dtype=np.int)
    my_df = pd.read_csv("self_data/Olshanyy_trio.csv")
    my_df.drop(my_df.columns[:1], inplace=True, axis=1)
    my_df["Target"] = np.zeros(my_df.shape[0], dtype=np.int)
    trigoram = pd.concat([my_df, df_tri])
    trigoram.index = np.arange(1, trigoram.shape[0] + 1)
    print("data/trio")
    print(trigoram)
    print()
    return trigoram


def FAR(arr_pred, arr_val):
    arr_val = arr_val.to_numpy()
    count = 0
    for i in range(len(arr_pred)):
        if arr_pred[i] and not arr_val[i]:
            count += 1

    print("FAR on test case: {}".format(count/len(arr_val)))


def FRR(arr_pred, arr_val):
    arr_val = arr_val.to_numpy()
    count = 0

    for i in range(len(arr_pred)):
        if not arr_pred[i] and arr_val[i]:
            count += 1

    print("FRR on test case: {}".format(count/len(arr_val)))


def MCC(arr_pred, arr_val):
    arr_val = arr_val.to_numpy()

    print("MCC on test case: {}".format(matthews_corrcoef(arr_val, arr_pred)))


def apply_tree(data):
    y = data["Target"]
    data = data.drop(["Target"], axis=1)
    x_train, x_valid, y_train, y_valid = train_test_split(data, y, test_size=0.3, random_state=17)

    params = {'max_depth': np.arange(1, 11), 'max_features': np.arange(1, 9)}
    tree = DecisionTreeClassifier()

# считает кросс вал скор - берет наши данные делит на 2-3, на каждом кусочке он считает
# результат алгоритма, для этого реза запускается метрика качества и потом усредняем результаты метрики на каждом кусочке

    print(f"Without hyper params traversal result on train set is : {np.mean(cross_val_score(tree, x_train, y_train, cv = 3))}")

    tree_grid = GridSearchCV(tree, params, cv=3, n_jobs=-1)

    tree_grid.fit(x_train, y_train)

# выводит качество на train dataset
    print(f"After hyper params choosen properly, result on train set is : {tree_grid.score(x_train, y_train)}")
#выводит качество на данных, которые алгоритм еще не видел
    print(f"After hyper params choosen properly, result on test set is : {tree_grid.score(x_valid, y_valid)}")


def apply_knn(data):
    y = data["Target"]
    data = data.drop(["Target"], axis=1)
    x_train, x_valid, y_train, y_valid = train_test_split(data, y, test_size=0.3, random_state=17)

    params = {'n_neighbors': np.arange(1, 11), 'leaf_size': np.arange(20, 40)}
    knn = KNeighborsClassifier()

    print(f"Without hyper params traversal result on train set is : "
          f"{np.mean(cross_val_score(knn, x_train, y_train, cv=3))}")

    knn_grid = GridSearchCV(knn, params, cv=3, n_jobs=-1)

    knn_grid.fit(x_train, y_train)

    FAR(knn_grid.predict(x_valid), y_valid)

    FRR(knn_grid.predict(x_valid), y_valid)

    MCC(knn_grid.predict(x_valid), y_valid)

    print(f"After hyper params choosen properly, result on train set is : {knn_grid.score(x_train, y_train)}")

    print(f"After hyper params choosen properly, result on test set is : {knn_grid.score(x_valid, y_valid)}")


def apply_MLP(data):
    y = data["Target"]
    data = data.drop(["Target"], axis=1)
    x_train, x_valid, y_train, y_valid = train_test_split(data, y, test_size=0.3, random_state=17)

    params = {'alpha': np.linspace(0.001, 0.01, 10), 'learning_rate_init': np.linspace(0.001, 0.01, 10)}
    mlp = MLPClassifier(max_iter=10 ** 3)

    print(f"Without hyper params traversal result on train set is : "
          f"{np.mean(cross_val_score(mlp, x_train, y_train, cv=3))}")

    mlp_grid = GridSearchCV(mlp, params, cv=3, n_jobs=-1)

    mlp_grid.fit(x_train, y_train)

    print(f"After hyper params choosen properly, result on train set is : {mlp_grid.score(x_train, y_train)}")

    print(f"After hyper params choosen properly, result on test set is : {mlp_grid.score(x_valid, y_valid)}")


uni = uni_parse()
bio = bio_parse()
trio = trio_parse()


apply_tree(uni)
apply_tree(bio)
apply_tree(trio)

apply_knn(uni)
apply_knn(bio)
apply_knn(trio)

apply_MLP(uni)
apply_MLP(bio)
apply_MLP(trio)

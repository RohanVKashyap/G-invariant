# Neural Discovery of Permutation Subgroups

This repository contains the code associated with the paper **"Neural Discovery of Permutation Subgroups"** accepted as contributed talk (extended oral presentation) at [AISTATS 2023](http://aistats.org/aistats2023/).

### Short description
We consider the problem of discovering subgroup $H$ of permutation group $S_n$. Unlike the traditional $H$-invariant networks wherein $H$ is assumed to be known, we present a method to discover the underlying subgroup, given that it satisfies certain conditions. Our results show that one could discover any subgroup of type $S_k (k \leq n)$ by learning an $S_n$-invariant function and a linear transformation. We also prove similar results for cyclic and dihedral subgroups. Finally, we provide a general theorem that can be extended to discover other subgroups of $S_n$. We also demonstrate the applicability of our results through numerical experiments on image-digit sum and symmetric polynomial regression tasks.

### Repository structure

#### Main structure
* [dataset/](dataset/) - contains files associated with preparation and loading the dataset of convex quadrangles
* [experiments/](experiments/) - contains the code to perform neural networks training and evaluation of the models
* [models/](models/) - contains model of the proposed G-invariant neural network and other models used for the comparison
* [utils/](utils/) - contains a bunch of utilities, such as: polynomials definitions, predefined permutation groups, etc.
* [data_inv/](data_inv/) - contains a dataset used in the experiments (convex quadrangle estimation only)


### Dependencies
* Tensorflow 1.14
* Keras 2.2.5
* NumPy 1.16.4
* cudatoolkit 10.1.168
* Matplotlib 3.1.1


### Citation
```
...
```



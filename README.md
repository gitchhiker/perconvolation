# Addressing the Percolation Problem with Convolutional Neural Networks

In this repository, you can find python scripts to generate percolation matrices.

After generating a slab of matrices, a program by the [Robert Sedgewick, Kevin Wayne, and Robert Dondero from Princeton University](https://introcs.cs.princeton.edu/python/24percolation/) will be imployed to evaluate whether or not each matrix does percolate from top to bottom or not. These files are also uploaded to this repository.

Next, the matrices are labeled with the boolean (percolates/does not percolate) and this labeled data is used to train a convolutional neural network (CNN) to predict the percolation.

At the end, a smaller set of matrices, that was held back from training, is fed into the network and the individual results (percolates yes/no) are verified against the results from the Princeton algorithm to test the networks acuracy.

A description of the percolation problem will be added soon.

# Python implementation of SinkSource
import time
#from tqdm import trange, tqdm
#import networkx as nx
import alg_utils
import numpy as np
#mport gc
from scipy.sparse import csr_matrix, eye
from scipy.sparse.linalg import spsolve
#import pdb


# this is supposed to match the original implementation
def SinkSource_scipy(P, f, max_iters=1000, delta=0.0001, a=0.8, scores={}, verbose=False):
    """ Iterate over the graph until all of the scores of the unknowns have converged
    *max_iters*: maximum number of iterations
    *delta*: Epsilon convergence cutoff. If all nodes scores changed by < *delta* after an iteration, then stop
    *a*: alpha converted from lambda
    *scores*: rather than start from scratch, we can start from a previous run's (or different GO term's) scores
    """
    # total number of computations performed during the update function
    total_comp = 0
    s = f.copy()
    prev_s = s.copy()

    start_time = time.time()
    #for iters in trange(max_iters):
    for iters in range(1,max_iters+1):
        # this uses way too much ram
        #s = a*np.dot(A,prev_s) + f
        s = a*csr_matrix.dot(P, prev_s) + f

        # TODO store this in a list and return it
        max_d = (s - prev_s).max()
        if verbose:
            print("\t\tmax score change: %0.6f" % (max_d))
        #tqdm.write("\t\tmax score change: %0.6f" % (max_d))
        if max_d < delta:
            # converged!
            break
        prev_s = s.copy()

    total_time = time.time() - start_time
    total_comp += len(P.data)*iters
    if verbose:
        print("SinkSource converged after %d iterations (%0.2f sec)" % (iters, total_time))
    #print("Scores of the top k nodes:")
    #print("\t%s" % (', '.join(["%s: %s" % (u, G.node[u]['s']) for u in list(unknowns)[:15]])))
    # convet s back to a dictionary
    #scores = {n:s[n] for n in range(len(s))}

    return s, total_time, iters, total_comp


def runSinkSource(P, positives, negatives=None, max_iters=1000, delta=0.0001, a=0.8, scores={}):
    """
    *G*: Should already be normalized
    *positives*: set of positive nodes
    *negeatives*: set of negative nodes
    *max_iters*: max # of iterations to run SinkSource. 
        If 0, use spsolve to solve the equation directly 
    *k*: Run with upper and lower bounds to prune unnecessary nodes
    """
    num_nodes = P.shape[0]
    # TODO this should be done once before all predictions are being made
    # check to make sure the graph is normalized because making a copy can take a long time
    #G = alg_utils.normalizeGraphEdgeWeights(G)
    P, f, node2idx, idx2node = alg_utils.setupScores(P, positives, negatives, a=a, remove_nonreachable=False)

    if max_iters > 0:
        s, total_time, iters, comp = SinkSource_scipy(P, f, max_iters=max_iters, delta=delta, a=a, scores=scores)
    else:
        start_time = time.process_time()
        # try solving for s directly
        A = eye(P.shape[0]) - a*P
        s = spsolve(A, f)
        total_time = time.process_time() - start_time
        print("Solved SS using sparse linear system (%0.2f sec)" % (total_time))
        iters = 0
        comp = 0

    # map back from the indices after deleting pos/neg to the original indices
    #s = {idx2node[n]:s[n] for n in range(len(s))}
    scores_arr = np.zeros(num_nodes)
    indices = [idx2node[n] for n in range(len(s))]
    scores_arr[indices] = s

    return scores_arr, total_time, iters, comp


def runLocal(P, positives, negatives=None):
    unknowns = set(range(P.shape[0])) - set(list(positives))
    f = np.zeros(P.shape[0])
    f[positives] = 1
    if negatives is not None:
        unknowns = unknowns - set(list(negatives))
        f[negatives] = -1

    start_time = time.process_time()
    s = csr_matrix.dot(P, f)
    total_time = time.process_time() - start_time

    #s = {n: s[n] for n in unknowns}

    return s, total_time

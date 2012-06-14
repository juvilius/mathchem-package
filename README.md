##Features
###Calculates the following matrices:
* Adjacency
* Laplacian
* Signless Laplacian
* Normalized Laplacian
* Distance
* Resistance Distance
* Reciprocal Distance
    
###Calculates the following topological indices:
* Spectrum of the all matrices above
* Spectral moments
* Energy
* Zagreb M1 Index
* Zagreb M2 Index
* Connectivity index (R)
* Eccentric Connectivity Index
* Randic Index
* Atom-Bond Connectivity Index (ABC)
* Estrada Index (EE) for all matrices
* Distance Estrada Index (DEE)
* Distance Degree (DD)
* Reverse Distance Degree (rDD)
* (Schultz) Molecular Topological Index (MTI)
* Distance Sum
* Balaban J index
* Kirchhoff Index (Kf) or Resistance
* Wiener Index (W)
* Reverse Wiener Index (RW)
* Hyper-Wiener Index (WW)
* Harary Index (H)
    
###Calculates the following graph properties:

* Order
* Diameter
* Degree
* Eccentricity
* Connectedness

##Installation

###As Python module

    pip install matchem    

####Depends on:
numpy

###As Sage module

Download *spkg* file from <https://github.com/downloads/hamster3d/mathchem-package/mathchem-0.1.0.spkg>

Save it into your *sage* directory

Run sage with command to install a new package:


    sage -f mathchem-0.1.0.spkg


After that you can use *matchem* in your sage programs:

    import mathchem as mc
    m = mc.Mol('GhCH?_')
    s = m.sage_graph()
    s.show()

##Usage
After successfull installation you can immediately use *mathchem* in Python or Sage
    
    python
    >>> import mathchem as mc
    >>> m = mc.Mol('GhCH?_')
    >>> m
    
    Molecular graph on 8 vertices
    
    >>> m.laplacian_matrix()
    
    matrix([[ 1, -1,  0,  0,  0,  0,  0,  0],
            [-1,  2, -1,  0,  0,  0,  0,  0],
            [ 0, -1,  3, -1,  0,  0, -1,  0],
            [ 0,  0, -1,  3, -1,  0,  0, -1],
            [ 0,  0,  0, -1,  2, -1,  0,  0],
            [ 0,  0,  0,  0, -1,  1,  0,  0],
            [ 0,  0, -1,  0,  0,  0,  1,  0],
            [ 0,  0,  0, -1,  0,  0,  0,  1]])
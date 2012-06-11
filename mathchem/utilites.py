from mathchem import *
from sage.matrix.constructor import *
    
def read_molecules_from_directory( path, mask="*.sdf"):

    import os
    import glob

    s = []

    for infile in glob.glob( os.path.join(path, mask) ):
        print infile
        m = Molecule()
        m.load_from_file(infile)
        s.append(m)

    return s
    
# ----------------------------------------  
    
def batch_process(infile, outfile, function) :

    fout = open(outfile, 'w')
    fin = open(infile, 'r')
    
    lines = fin.readlines()    
    fin.close()
        
    for line in lines:
        fout.writelines(function(line))

    fout.close()

# ----------------------------------------
    
def do_nothing(line):
    return line  + "\n"
    


def do_init_Molecule(g6str):
    m = Molecule(g6str)
    return g6str + "\n"


def do_calculs_Molecule(g6str):
    m = Molecule(g6str)
    return g6str + ' ' + str(m.zagreb_m1_index()) + ' ' + str(m.zagreb_m2_index()) + "\n"

def do_init_Mol(g6str):
    m = Mol(g6str)
    return g6str  + "\n"

def do_calculs_Mol(g6str):
    m = Mol(g6str)
    return g6str  + ' ' + str(m.zagreb_m1_index()) + ' ' + str(m.zagreb_m2_index()) + "\n"    

def do_test2_Mol(g6str):
    m = Mol(g6str)
    return g6str  + ' ' + str(m.molecular_topological_index()) + ' ' + str(m.degree_distance())+ ' ' + str(m.reverse_degree_distance()) + "\n"    

def do_test2_Molecule(g6str):
    m = Molecule(g6str)
    return g6str  + ' ' + str(m.molecular_topological_index()) + ' ' + str(m.degree_distance())+ ' ' + str(m.reverse_degree_distance()) + "\n"    

def do_test_Mol_balaban(g6str):
    m = Mol(g6str)
    return g6str  + ' ' + str(m.balaban_j_index()) + ' ' + str(m.eccentric_distance_sum()) + "\n"    

def do_test_Molecule_balaban(g6str):
    m = Molecule(g6str)
    return g6str  + ' ' + str(m.balaban_j_index()) + ' ' + str(m.eccentric_distance_sum()) + "\n"    


# ----------------------------------------

def read_g6( s):
    
    def graph_bit(pos):
        return ( (ord(s[1+ pos/6]) - 63) & (2**(5-pos%6)) ) != 0

    # this reads only small graphs !!!!!!!!!!!!!!
    n = ord(s[0]) - 63
    # add here if n==63 then n is the next 4 bytes
    
    #print n

    A = [[0 for col in range(n)] for row in range(n)]

    i=0; j=1

    for x in range(n*(n-1)/2):
        if graph_bit(x):
            A[i][j] = 1
            A[j][i] = 1
        if j-i == 1:
            i=0
            j+=1
        else: i+=1
        
    #for row in A: print row
    return A


def zagreb_m1(A):
    m1 = 0
    for row in A:
        m1 += sum(row)**2
    return m1

def zagreb_m2(A):
    m2 = 0
    n = len(A)
    for j in range(n):
        drow = sum(A[j])
        for i in range(j+1, n):
            if A[j][i] == 1:
                m2 += drow * sum(A[i])

    return m2


# utilites



def do_my_calculs(g6str):
    A = read_g6(g6str)
    return g6str + ' ' + str(zagreb_m1(A)) + ' ' + str(zagreb_m2(A)) + "\n"


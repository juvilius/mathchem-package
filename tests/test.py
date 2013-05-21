from mathchem import *
# retreive compounds with NSC number from 1 to 10000
mols = read_from_NCI_by_NSC('1-10000')

# some of the numbers does not refer to any compound

# some of the compounds are not connected
# let's filter them by calling is_connected method of each instance
mols_c = filter(lambda x: x.is_connected(), mols)

# all theses compounds will not contain infinity in their distance matrix



methods = ['order','diameter', 'energy', 'incidence_energy', 'zagreb_m1_index', 'zagreb_m2_index', 'eccentric_connectivity_index', 'randic_index', 'atom_bond_connectivity_index', 'estrada_index', 'degree_distance', 'reverse_degree_distance', 'molecular_topological_index', 'eccentric_distance_sum', 'balaban_j_index', 'kirchhoff_index', 'wiener_index', 'terminal_wiener_index', 'reverse_wiener_index', 'hyper_wiener_index', 'harary_index', 'LEL', 'randic_type_lodeg_index', 'randic_type_sdi_index', 'randic_type_hadi_index', 'sum_lordeg_index', 'inverse_sum_lordeg_index', 'inverse_sum_indeg_index', 'misbalance_lodeg_index', 'misbalance_losdeg_index', 'misbalance_irdeg_index', 'misbalance_rodeg_index', 'misbalance_deg_index', 'misbalance_hadeg_index','misbalance_indi_index', 'min_max_rodeg_index', 'min_max_sdi_index', 'max_min_deg_index', 'max_min_sdeg_index', 'symmetric_division_deg_index']






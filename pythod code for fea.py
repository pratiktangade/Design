for e in range(nel): #(e loops for the number of elements)
ke=youngs*area[e]/le*np.array([[1,-1],[-1, 1]]) # build element stiffness matrix
# gather nodel data for element
n1 = element_nodes[e,0]
n2 = element_nodes[e,1]
x1 = x[n1]
x2 = x[n2]
# assembly (i loops for the nodes)
for i in range(nne):
I = element_nodes[e,i] # assemble force vector
for j in range(nne):
J = element_nodes[e,j]
K[I,J] += ke[i,j] # scatter element stiffness to global stiffness matrix

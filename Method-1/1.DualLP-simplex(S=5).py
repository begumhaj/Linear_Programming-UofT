#!/usr/bin/env python
# coding: utf-8

# In[52]:


from gurobipy import*
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
import copy
#Data of th Farmer ted#
C=[-200,-240,0,6000] 
M=1000000000
I=range(0,3)
S=range(1,6)       #Total 5 scenarios#
b=[150,230,260]     #cost of set I#
#matrix E#
E=np.array([[3.5,3.0,2.5,2,1.5],[4.2,3.6,3.0,2.4,1.8],[28,24,20,16,12]])


# In[53]:


#Model for Farmers ted #
m= Model("Farming Ted-Dual")  # name of the model and variable LP#
#Decision variables for acres of land  devoted to I#
x=m.addVar(vtype=GRB.CONTINUOUS,name='x')
#Decision variables for purchase#
y1=m.addVars(S,vtype=GRB.CONTINUOUS,name='y1')
y2=m.addVars(S,vtype=GRB.CONTINUOUS,name='y2')
y3=m.addVars(S,vtype=GRB.CONTINUOUS,name='y3')
y4=m.addVars(S,vtype=GRB.CONTINUOUS,name='y4')
#slack variables
l=m.addVars(I,vtype=GRB.CONTINUOUS,name='l')
s1=m.addVars(S,vtype=GRB.CONTINUOUS,name='s1')
s2=m.addVars(S,vtype=GRB.CONTINUOUS,name='s2')
s3=m.addVars(S,vtype=GRB.CONTINUOUS,name='s3')
s4=m.addVars(S,vtype=GRB.CONTINUOUS,name='s4')
s5=m.addVars(S,vtype=GRB.CONTINUOUS,name='s5')
s6=m.addVars(S,vtype=GRB.CONTINUOUS,name='s6')

#artificial variables
la=m.addVars(I,vtype=GRB.CONTINUOUS,name='la')
a1=m.addVars(S,vtype=GRB.CONTINUOUS,name='a1')
a2=m.addVars(S,vtype=GRB.CONTINUOUS,name='a2')
a3=m.addVars(S,vtype=GRB.CONTINUOUS,name='a3')
a4=m.addVars(S,vtype=GRB.CONTINUOUS,name='a4')
a5=m.addVars(S,vtype=GRB.CONTINUOUS,name='a5')
a6=m.addVars(S,vtype=GRB.CONTINUOUS,name='a6')


# In[54]:


#Adding constraints for Farmers ted#
# (linking constraint)#


m.addConstr(-x+E[0][0]*y1[1]+E[0][1]*y1[2]+E[0][2]*y1[3]+E[0][3]*y1[4]+E[0][4]*y1[5]+l[0]+la[0] == b[0],name="linkingconstraints")
m.addConstr(-x+E[1][0]*y2[1]+E[1][1]*y2[2]+E[1][2]*y2[3]+E[1][3]*y2[4]+E[1][4]*y2[5]+l[1]+la[1] == b[1],name="linkingconstraints")
m.addConstr(-x+E[2][0]*y3[1]+E[2][1]*y3[2]+E[2][2]*y3[3]+E[2][3]*y3[4]+E[2][4]*y3[5]+l[2]+la[2] <= b[2],name="linkingconstraints")

for s in S:
    m.addConstr(y1[s]+s1[s]+a1[s]==238/5,name="sub1")
    m.addConstr(y1[s]-s2[s]+a2[s]==170/5,name="sub2")
    m.addConstr(y2[s]+s3[s]+a3[s]==210/5,name="sub3")
    m.addConstr(y2[s]-s4[s]+a4[s]==150/5,name="sub4")
    m.addConstr(y3[s]+y4[s]-s5[s]+a5[s]==36/5,name="sub5")
    m.addConstr(y3[s]-s6[s]+a6[s]==10/5,name="sub6")
    
m.write("1.DualLP-simplex(S=5).lp")
v=[]
for s in S:
    q=-200*y1[s]-240*y2[s]+6000*y4[s]
    v.append(q)
Q=la[0]+la[1]+la[2]
N=[]
for s in S:
    a=(M*(a1[s]+a2[s]+a3[s]+a4[s]+a5[s]+a6[s]))
    N.append(a)
m.setObjective(500*x+v[0]+v[1]+v[2]+v[3]+v[4]+Q*M+N[0]+N[1]+N[2]+N[3]+N[4])
m.write("3.Dual(S=5).lp")
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[55]:


dvars=m.getVars()
constrs=m.getConstrs()
obj_coeffs=m.getAttr("obj",dvars)

var_index={v:i for i,v in enumerate(dvars)}
constr_index={c:i for i,c in enumerate(constrs)}
def get_expr_coos(expr, var_indices):
    for i in range(expr.size()):
        dvar=expr.getVar(i)
        yield expr.getCoeff(i), var_indices[dvar]
def get_matrix_coo(m):
    dvars=m.getVars()
    constrs=m.getConstrs()
    var_indices={v: i for i,v in enumerate(dvars)}
    for row_idx,constr in enumerate(constrs):
        for coeff, col_idx in get_expr_coos(m.getRow(constr),var_indices):
            yield row_idx,col_idx,coeff
nzs=pd.DataFrame(get_matrix_coo(m),columns=['row_idx','col_idx','coeff'])


# In[56]:


#rows index from the model for A matrix#
row=[]
row=nzs.iloc[:, 0].tolist()
print("row=",row)


# In[57]:


#column index for the modelto get A matrix#
column=[]
column=nzs.iloc[:,1].tolist()
print("column=",column)


# In[58]:


#coefficients in the A matrix#
data=[]
data=nzs.iloc[:,2].tolist()
print("data=",data)


# In[59]:


#Forming A matrix from the model#
rows=np.array(row)
columns=np.array(column)
datas=np.array(data)
A1=coo_matrix((datas, (rows, columns)),shape=(33,87)).toarray()


# In[60]:


print(A1)
b1=[150,230,260,238/3,170/3,210/3,150/3,36/3,10/3,238/3,170/3,210/3,150/3,36/3,10/3,238/3,170/3,210/3,150/3,36/3,10/3,238/3,170/3,210/3,150/3,36/3,10/3,238/3,170/3,210/3,150/3,36/3,10/3]


# In[61]:


#Simplex method#

#input for simplex method= A,b,c vectors#
A=np.array(A1)
b=np.array(b1)
c=np.array(obj_coeffs)
print("A=",A)
print("b=",b)
print("c=",c)
def Simplex(A, b, c):
    '''Takes input vars, computs corresponding values,
    then uses while loop to iterate until a basic optimal solution is reached.
    RETURNS: cbT, cbIndx, cnT, cnIndx, bHat, cnHat.
    cbT, cbIndex is final basic variable values, and indices
    cnT, cnIndex is final nonbasic variable values and indices
    bHat is final solution values, 
    cnHat is optimality condition'''
    
    #sizes of basic and nonbasic vectors
    basicSize = A.shape[0] # number of constraints, m
    nonbasicSize = A.shape[1] - basicSize #n-m, number of variables
    # global index tracker of variables of basic and nonbasic variables (objective)
    # that is, index 0 corresponds with x_0, 1 with x_1 and so on.  So each index corresponds with a variable
    cindx = [i for i in range(0, len(c))]
    #basic variable coefficients
    cbT = np.array(c[nonbasicSize:])
    #nonbasic variable coefficients
    cnT = np.array(c[:nonbasicSize])
    # run core simplex method until reach the optimal solution
    while True:
        
        # keep track of current indices of basic and non-basic variables
        cbIndx = cindx[nonbasicSize:]
        print("cbIndx=",cbIndx)
        cnIndx = cindx[:nonbasicSize]
        print("cnIndx=",cnIndx)
        # basis matrix
        B = A[:, cbIndx]
        Binv = np.linalg.inv(B)
        
        # nonbasic variable matrix
        N = A[:, cnIndx]
        # bHat, the values of the basic variables
        # recall that at the start the basic variables are the slack variables, and 
        # have values equal the vector b (as primary variables are set to 0 at the start)
        bHat = Binv @ b
        yT = cbT @ Binv
        
        # use to check for optimality, determine variable to enter basis
        cnHat = cnT - (yT @ N)
        
        # find indx of minimum value of cnhat, this is the variable to enter the basis
        cnMinIndx = np.argmin(cnHat)
        # break out of loop, returning values if all values of cnhat are above 0
        if(all(i>=0 for i in cnHat)):
            # use cbIndx to get index values of variables in bHat, and the corresponding index
            # values in bHat are the final solution values for each of the corresponding variables
            # ie value 0 in dbIndx corresponds with first variable, so whatever the index for the 0 is
            # is the index in bHat that has the solution value for that variable.
            return cbT, cbIndx, cnT, cnIndx, bHat, cnHat
        
        # this is the index for the column of coeffs in a for the given variable
        indx = cindx[cnMinIndx]
        Ahat = Binv @ A[:, indx]
        # now we want to iterate through Ahat and bHat and pick the minimum ratios
        # only take ratios of variables with Ahat_i values greater than 0
        # pick smallest ratio to get variable that will become nonbasic.
        ratios = []
        for i in range(0, len(bHat)):
            Aval = Ahat[i]
            Bval = bHat[i]

            # don't look at ratios with val less then or eqaul to 0, append to keep index
            if(Aval <= 0):
                ratios.append(10000000)
                continue
            ratios.append(Bval / Aval)

        ratioMinIndx = np.argmin(ratios)
        
        #switch basic and nonbasic variables using the indices.
        cnT[cnMinIndx], cbT[ratioMinIndx] = cbT[ratioMinIndx], cnT[cnMinIndx]
        # switch global index tracker indices
        cindx[cnMinIndx], cindx[ratioMinIndx + nonbasicSize] = cindx[ratioMinIndx + nonbasicSize], cindx[cnMinIndx]
        # now repeat the loop
z=Simplex(A, b, c)


# In[62]:


CB=np.transpose(z[0])
CN=np.transpose(z[2])
XB=z[4]
XN=z[5]
print("CB=",CB)
print("CN=",CN)
print("XB=",XB)
print("XN=",XN)
cost1=np.multiply(CB,XB)
c=list(cost1)
print("Z1=",sum(c))
cost2=np.multiply(CN,XN)
d=list(cost2)
print("Z2",sum(d))


# In[ ]:





# In[ ]:





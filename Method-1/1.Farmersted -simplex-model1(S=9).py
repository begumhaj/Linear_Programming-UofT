#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gurobipy import*
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
import copy

#Data of th Farmer ted#
A=500                 #acres available#
M=100000
I=range(0,3)          # Set of Products wheat=1, corn=2, beans=3#
Scenarios=range(0,9)       #Total 9 scenarios#
P=1/9                     #Probability of each scenario#
CI=[150,230,260]         #cost of set I#
#matrix E[s][i]#
E=np.array([[4.5,5.4,36],[4,4.8,32],[3.5,4.2,28],[3.0,3.6,24],[2.5,3.0,20],[2.0,2.4,16],[1.5,1.8,12],[1,1.2,8],[0.5,0.6,4]])


# In[2]:


#Model for Farmers ted #
m= Model("Farming Ted")  # name of the model and variable LP#
#Decision variables for acres of land  devoted to I#
x=m.addVars(I,vtype=GRB.CONTINUOUS,name='x')
#Decision variables for purchase#
yw=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,name='yw')
yc=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,name='yc')
#Decision variables for beans sold
zw=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name='zw')
zc=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name='zc')
zb=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name='zb')
zbb=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name='zbb')
#slack variables#
ux=m.addVar(vtype=GRB.CONTINUOUS,lb=0,name="ux")
uw=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name="uw")
uc=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name="uc")
ub=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name="ub")
ubb=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name="ubb")
#big M variables#
vx=m.addVar(vtype=GRB.CONTINUOUS,lb=0,name="v")
vw=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name="vw")
vc=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name="vc")
vb=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name="vb")
vbb=m.addVars(Scenarios,vtype=GRB.CONTINUOUS,lb=0,name="vbb")


# In[3]:


#Adding constraints for Farmers ted#
#Constraint-1 (for total acres available)#
m.addConstr(quicksum(x[i] for i in I)+ ux+vx  == A,name="Surfaceacres")

#contraint-2(for wheat requirement)#
for s in Scenarios:
  m.addConstr(x[0]*E[s][0]+yw[s]-zw[s]-uw[s]+vw[s]==200,name="wheatrequirement[%d]"%(s))


#constraint -3 (for corn requirement)#
for s  in Scenarios:
 m.addConstr(E[s][1]*x[1]+yc[s]-zc[s]-uc[s]+vc[s]==240,name="cornrequirement[%d]"%(s))

#constraint-4(for bean )#
for s in Scenarios:
 m.addConstr(zb[s]+zbb[s]- E[s][2]* x[2]+ub[s]+vb[s]==0,name="beansold[%d]" %(s))

#contraint-5(for bean)#
for s in Scenarios:
 m.addConstr(zb[s]+ubb[s]+vbb[s]==6000,name="beansoldlimit[%d]"%(s))

#objective function#
ob1=[]
for s in Scenarios:
    ob1.append(P*(238*yw[s]+210*yc[s]-170*zw[s]-150*zc[s]-36*zb[s]-10*zbb[s]))

obb=[]
for s in Scenarios:
    obb.append(M*(vw[s]+vc[s]+vb[s]+vbb[s]))
  
m.setObjective(CI[0]*x[0]+CI[1]*x[1]+CI[2]*x[2]+quicksum(ob1[s]for s in Scenarios)+quicksum(obb[s]for s in Scenarios))                                                       

m.write("1.Farmer_model(S=9).lp")
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))
    


# In[4]:


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

            


# In[5]:


#rows index from the model for A matrix#
row=[]
row=nzs.iloc[:, 0].tolist()
print("row=",row)


# In[6]:


#column index for the modelto get A matrix#
column=[]
column=nzs.iloc[:,1].tolist()
print("column=",column)


# In[7]:


#coefficients in the A matrix#
data=[]
data=nzs.iloc[:,2].tolist()
print("data=",data)


# In[8]:


#Forming A matrix from the model#
rows=np.array(row)
columns=np.array(column)
datas=np.array(data)
A1=coo_matrix((datas, (rows, columns)),shape=(37,131)).toarray()


# In[9]:


#Forming the b vector in the std form LP#
b1=[500,200,200,200,200,200,200,200,200,200,240,240,240,240,240,240,240,240,240,0,0,0,0,0,0,0,0,0,6000,6000,6000,6000,6000,6000,6000,6000,6000]


# In[10]:


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


# In[11]:


CB=np.transpose(z[0])
CN=np.transpose(z[2])
XB=z[4]
XN=z[5]
print("CB=",CB)
print("CN=",CN)
print("XB=",XB)
print("XN=",XN)


# In[12]:


cost1=np.multiply(CB,XB)
c=list(cost1)
print("Z=",sum(c))


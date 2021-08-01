#!/usr/bin/env python
# coding: utf-8

# In[5]:


#iteration1#
#subproblems1#
from gurobipy import*
m=Model("subproblems")

x=m.addVar(vtype=GRB.CONTINUOUS,name='x')
y1=m.addVar(vtype=GRB.CONTINUOUS,name='y1')
y2=m.addVar(vtype=GRB.CONTINUOUS,name='y2')
y3=m.addVar(vtype=GRB.CONTINUOUS,name='y3')
y4=m.addVar(vtype=GRB.CONTINUOUS,name='y4')
m.addConstr(y1<=238/3,name="sub1")
m.addConstr(-y1<=-170/3,name="sub2")
m.addConstr(y2<=210/3,name="sub3")
m.addConstr(-y2<=-150/3,name="sub4")
m.addConstr(-y3-y4<=-36/3,name="sub5")
m.addConstr(-y3<=-10/3,name="sub6")
m.setObjective(500*x-200*y1-240*y2+6000*y4)
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[7]:


#iteration1#
#subproblems2 and 3#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]

y1=m.addVar(vtype=GRB.CONTINUOUS,name='y1')
y2=m.addVar(vtype=GRB.CONTINUOUS,name='y2')
y3=m.addVar(vtype=GRB.CONTINUOUS,name='y3')
y4=m.addVar(vtype=GRB.CONTINUOUS,name='y4')
m.addConstr(y1<=238/3,name="sub1")
m.addConstr(-y1<=-170/3,name="sub2")
m.addConstr(y2<=210/3,name="sub3")
m.addConstr(-y2<=-150/3,name="sub4")
m.addConstr(-y3-y4<=-36/3,name="sub5")
m.addConstr(-y3<=-10/3,name="sub6")
m.setObjective(-200*y1-240*y2+6000*y4)
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[20]:


#iteration2#
#subproblems1,#
from gurobipy import*
m=Model("subproblems")
m.params.Method=2
m.params.InfUnbdInfo=1

x=m.addVar(vtype=GRB.CONTINUOUS,name='x')
y1=m.addVar(vtype=GRB.CONTINUOUS,name='y1')
y2=m.addVar(vtype=GRB.CONTINUOUS,name='y2')
y3=m.addVar(vtype=GRB.CONTINUOUS,name='y3')
y4=m.addVar(vtype=GRB.CONTINUOUS,name='y4')
m.addConstr(y1<=238/3,name="sub1")
m.addConstr(-y1<=-170/3,name="sub2")
m.addConstr(y2<=210/3,name="sub3")
m.addConstr(-y2<=-150/3,name="sub4")
m.addConstr(-y3-y4<=-36/3,name="sub5")
m.addConstr(-y3<=-10/3,name="sub6")
m.setObjective(-200*y1-240*y2+6000*y4)
m.optimize()
m.setObjective(x*74450.8-y1*611.6-y2*124707-948326.4*y3+6000*y4)
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[90]:


#iteration2#
#subproblems2#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]
S=range(1,5)

m.params.Method=2
m.params.InfUnbdInfo=1
x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(x[1] <=q[0])
m.addConstr(-x[1]<=q[1])
m.addConstr(x[2]<=q[2])
m.addConstr(-x[2]<=q[3])
m.addConstr(-x[3]-x[4]<=q[4])
m.addConstr(-x[3]<=q[5])
m.setObjective(143*x[1]-103963.2*x[2]-790272*x[3]+6000*x[4])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[ ]:





# In[93]:


#iteration2#
#subproblems3#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]
S=range(1,5)

m.params.Method=2
m.params.InfUnbdInfo=1
x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(x[1] <=q[0])
m.addConstr(-x[1]<=q[1])
m.addConstr(x[2]<=q[2])
m.addConstr(-x[2]<=q[3])
m.addConstr(-x[3]-x[4]<=q[4])
m.addConstr(-x[3]<=q[5])
m.setObjective(74.4*x[1]-83218.56*x[2]-632217.6*x[3]+6000*x[4])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[2]:


#ITERATION3#
#subproblem1#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]
S=range(1,5)

m.params.Method=2
m.params.InfUnbdInfo=1
x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(x[1] <=q[0])
m.addConstr(-x[1]<=q[1])
m.addConstr(x[2]<=q[2])
m.addConstr(-x[2]<=q[3])
m.addConstr(-x[3]-x[4]<=q[4])
m.addConstr(-x[3]<=q[5])
m.setObjective(886*x[1]-121260.48*x[2]-5486.4*x[3]+6000*x[4])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[3]:


#ITERATION3#
#subproblem2#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]
S=range(1,5)

m.params.Method=2
m.params.InfUnbdInfo=1
x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(x[1] <=q[0])
m.addConstr(-x[1]<=q[1])
m.addConstr(x[2]<=q[2])
m.addConstr(-x[2]<=q[3])
m.addConstr(-x[3]-x[4]<=q[4])
m.addConstr(-x[3]<=q[5])
m.setObjective(144.5*x[1]-104028.057*x[2]-10*x[3]+6000*x[4])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[5]:


#ITERATION4#
#subproblem3#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]
S=range(1,5)

m.params.Method=1
m.params.InfUnbdInfo=1
x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(x[1] <=q[0])
m.addConstr(-x[1]<=q[1])
m.addConstr(x[2]<=q[2])
m.addConstr(-x[2]<=q[3])
m.addConstr(-x[3]-x[4]<=q[4])
m.addConstr(-x[3]<=q[5])
m.setObjective(-6.798e+19*x[1]+1.29408e+22*x[2]+4.64e+10*x[3]+6000*x[4])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[7]:


#ITERATION4#
#subproblem1#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]
S=range(1,5)

m.params.Method=1
m.params.InfUnbdInfo=1
x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(x[1] <=q[0])
m.addConstr(-x[1]<=q[1])
m.addConstr(x[2]<=q[2])
m.addConstr(-x[2]<=q[3])
m.addConstr(-x[3]-x[4]<=q[4])
m.addConstr(-x[3]<=q[5])
m.setObjective(-1.0197e+20*x[1]+1.94112e+22*x[2]+6.96e+10*x[3]+6000*x[4])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[8]:


#ITERATION4#
#subproblem2#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]
S=range(1,5)

m.params.Method=1
m.params.InfUnbdInfo=1
x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(x[1] <=q[0])
m.addConstr(-x[1]<=q[1])
m.addConstr(x[2]<=q[2])
m.addConstr(-x[2]<=q[3])
m.addConstr(-x[3]-x[4]<=q[4])
m.addConstr(-x[3]<=q[5])
m.setObjective(-8.4975e+19*x[1]+1.6176e+22*x[2]+5.8e+10*x[3]+6000*x[4])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[26]:


#ITERATION5#
#subproblem1#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]
S=range(1,5)

m.params.InfUnbdInfo=1


x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(x[1] <=q[0])
m.addConstr(-x[1]<=q[1])
m.addConstr(x[2]<=q[2])
m.addConstr(-x[2]<=q[3])
m.addConstr(-x[3]-x[4]<=q[4])
m.addConstr(-x[3]<=q[5])
m.setObjective(-2.4e+10*x[1]+7.83e+172*x[2]+0.120936*x[3]+6000*x[4])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[16]:


#ITERATION5#
#subproblem2#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]
S=range(1,5)

m.params.Method=2
m.params.InfUnbdInfo=1
x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(x[1] <=q[0])
m.addConstr(-x[1]<=q[1])
m.addConstr(x[2]<=q[2])
m.addConstr(-x[2]<=q[3])
m.addConstr(-x[3]-x[4]<=q[4])
m.addConstr(-x[3]<=q[5])
m.setObjective(-2e+10*x[1]+2.349e+18*x[2]+0.10078*x[3]+6000*x[4])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[17]:


#ITERATION5#
#subproblem1#
from gurobipy import*
m=Model("subproblems")
q=[238/3,-170/3,210/3,-150/3,-36/3,-10/3]
S=range(1,5)

m.params.Method=2
m.params.InfUnbdInfo=1
x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(x[1] <=q[0])
m.addConstr(-x[1]<=q[1])
m.addConstr(x[2]<=q[2])
m.addConstr(-x[2]<=q[3])
m.addConstr(-x[3]-x[4]<=q[4])
m.addConstr(-x[3]<=q[5])
m.setObjective(-2.4e+10*x[1]+7.83e+172*x[2]+0.120936*x[3]+6000*x[4])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[68]:



from gurobipy import*
p=Model("Phase1")
c=[500,-200,-240,0,6000,-200,-240,0,6000,-200,-240,0,6000]
S=range(1,5)
I=range(1,7)
D=range(1,2)
s=p.addVars(I,vtype=GRB.CONTINUOUS,name='s')
d=p.addVars(D,vtype=GRB.CONTINUOUS,name='d')
d1=p.addVars(S,vtype=GRB.CONTINUOUS,name='d1')
d2=p.addVars(S,vtype=GRB.CONTINUOUS,name='d2')
d3=p.addVars(S,vtype=GRB.CONTINUOUS,name='d3')

p.addConstr(-d[1]+3*d1[1]+2.5*d2[1]+2*d3[1]+s[1]+s[4]==150)
p.addConstr(-d[1]+3*d1[2]+2.5*d2[2]+2*d3[2]+s[2]+s[5]==230)
p.addConstr(-d[1]+3*d1[3]+2.5*d2[3]+2*d3[3]+s[3]+s[6]==260)
p.setObjective(s[1]+s[2]+s[3])
p.optimize()
for v in p.getVars():
        print('%s %g' % (v.varName, v.x))


# In[55]:


for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[88]:


#iteration2#
#subproblems1#
from gurobipy import*
m=Model("subproblems")

S=range(1,3)

m.params.Method=2
m.params.InfUnbdInfo=1
x=m.addVars(S,vtype=GRB.CONTINUOUS,name='x')

m.addConstr(-x[1]+x[2] <=2)
m.addConstr(-x[1]+2*x[2]<=8)

m.setObjective(-2*x[1]-3*x[2])
m.optimize()
for v in m.getVars():
        print('%s %g' % (v.varName, v.x))


# In[ ]:





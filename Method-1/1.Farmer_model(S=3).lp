\ Model Farming Ted
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  150 x[0] + 230 x[1] + 260 x[2] + 79.33333333333333 yw[0]
   + 79.33333333333333 yw[1] + 79.33333333333333 yw[2] + 70 yc[0]
   + 70 yc[1] + 70 yc[2] - 56.66666666666666 zw[0]
   - 56.66666666666666 zw[1] - 56.66666666666666 zw[2] - 50 zc[0]
   - 50 zc[1] - 50 zc[2] - 12 zb[0] - 12 zb[1] - 12 zb[2]
   - 3.333333333333333 zbb[0] - 3.333333333333333 zbb[1]
   - 3.333333333333333 zbb[2] + 100000 vw[0] + 100000 vw[1] + 100000 vw[2]
   + 100000 vc[0] + 100000 vc[1] + 100000 vc[2] + 100000 vb[0]
   + 100000 vb[1] + 100000 vb[2] + 100000 vbb[0] + 100000 vbb[1]
   + 100000 vbb[2]
Subject To
 Surfaceacres: x[0] + x[1] + x[2] + ux + v = 500
 wheatrequirement[0]: 3 x[0] + yw[0] - zw[0] - uw[0] + vw[0] = 200
 wheatrequirement[1]: 2.5 x[0] + yw[1] - zw[1] - uw[1] + vw[1] = 200
 wheatrequirement[2]: 2 x[0] + yw[2] - zw[2] - uw[2] + vw[2] = 200
 cornrequirement[0]: 3.6 x[1] + yc[0] - zc[0] - uc[0] + vc[0] = 240
 cornrequirement[1]: 3 x[1] + yc[1] - zc[1] - uc[1] + vc[1] = 240
 cornrequirement[2]: 2.4 x[1] + yc[2] - zc[2] - uc[2] + vc[2] = 240
 beansold[0]: - 24 x[2] + zb[0] + zbb[0] + ub[0] + vb[0] = 0
 beansold[1]: - 20 x[2] + zb[1] + zbb[1] + ub[1] + vb[1] = 0
 beansold[2]: - 16 x[2] + zb[2] + zbb[2] + ub[2] + vb[2] = 0
 beansoldlimit[0]: zb[0] + ubb[0] + vbb[0] = 6000
 beansoldlimit[1]: zb[1] + ubb[1] + vbb[1] = 6000
 beansoldlimit[2]: zb[2] + ubb[2] + vbb[2] = 6000
Bounds
End

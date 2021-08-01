\ Model Farming Ted
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  150 x[0] + 230 x[1] + 260 x[2] + 47.6 yw[0] + 47.6 yw[1] + 47.6 yw[2]
   + 47.6 yw[3] + 47.6 yw[4] + 42 yc[0] + 42 yc[1] + 42 yc[2] + 42 yc[3]
   + 42 yc[4] - 34 zw[0] - 34 zw[1] - 34 zw[2] - 34 zw[3] - 34 zw[4]
   - 30 zc[0] - 30 zc[1] - 30 zc[2] - 30 zc[3] - 30 zc[4] - 7.2 zb[0]
   - 7.2 zb[1] - 7.2 zb[2] - 7.2 zb[3] - 7.2 zb[4] - 2 zbb[0] - 2 zbb[1]
   - 2 zbb[2] - 2 zbb[3] - 2 zbb[4] + 100000 vw[0] + 100000 vw[1]
   + 100000 vw[2] + 100000 vw[3] + 100000 vw[4] + 100000 vc[0]
   + 100000 vc[1] + 100000 vc[2] + 100000 vc[3] + 100000 vc[4]
   + 100000 vb[0] + 100000 vb[1] + 100000 vb[2] + 100000 vb[3]
   + 100000 vb[4] + 100000 vbb[0] + 100000 vbb[1] + 100000 vbb[2]
   + 100000 vbb[3] + 100000 vbb[4]
Subject To
 Surfaceacres: x[0] + x[1] + x[2] + ux + v = 500
 wheatrequirement[0]: 3.5 x[0] + yw[0] - zw[0] - uw[0] + vw[0] = 200
 wheatrequirement[1]: 3 x[0] + yw[1] - zw[1] - uw[1] + vw[1] = 200
 wheatrequirement[2]: 2.5 x[0] + yw[2] - zw[2] - uw[2] + vw[2] = 200
 wheatrequirement[3]: 2 x[0] + yw[3] - zw[3] - uw[3] + vw[3] = 200
 wheatrequirement[4]: 1.5 x[0] + yw[4] - zw[4] - uw[4] + vw[4] = 200
 cornrequirement[0]: 4.2 x[1] + yc[0] - zc[0] - uc[0] + vc[0] = 240
 cornrequirement[1]: 3.6 x[1] + yc[1] - zc[1] - uc[1] + vc[1] = 240
 cornrequirement[2]: 3 x[1] + yc[2] - zc[2] - uc[2] + vc[2] = 240
 cornrequirement[3]: 2.4 x[1] + yc[3] - zc[3] - uc[3] + vc[3] = 240
 cornrequirement[4]: 1.8 x[1] + yc[4] - zc[4] - uc[4] + vc[4] = 240
 beansold[0]: - 28 x[2] + zb[0] + zbb[0] + ub[0] + vb[0] = 0
 beansold[1]: - 24 x[2] + zb[1] + zbb[1] + ub[1] + vb[1] = 0
 beansold[2]: - 20 x[2] + zb[2] + zbb[2] + ub[2] + vb[2] = 0
 beansold[3]: - 16 x[2] + zb[3] + zbb[3] + ub[3] + vb[3] = 0
 beansold[4]: - 12 x[2] + zb[4] + zbb[4] + ub[4] + vb[4] = 0
 beansoldlimit[0]: zb[0] + ubb[0] + vbb[0] = 6000
 beansoldlimit[1]: zb[1] + ubb[1] + vbb[1] = 6000
 beansoldlimit[2]: zb[2] + ubb[2] + vbb[2] = 6000
 beansoldlimit[3]: zb[3] + ubb[3] + vbb[3] = 6000
 beansoldlimit[4]: zb[4] + ubb[4] + vbb[4] = 6000
Bounds
End

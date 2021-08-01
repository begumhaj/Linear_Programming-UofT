\ Model Farming Ted
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  150 x[0] + 230 x[1] + 260 x[2] + 26.44444444444444 yw[0]
   + 26.44444444444444 yw[1] + 26.44444444444444 yw[2]
   + 26.44444444444444 yw[3] + 26.44444444444444 yw[4]
   + 26.44444444444444 yw[5] + 26.44444444444444 yw[6]
   + 26.44444444444444 yw[7] + 26.44444444444444 yw[8]
   + 23.33333333333333 yc[0] + 23.33333333333333 yc[1]
   + 23.33333333333333 yc[2] + 23.33333333333333 yc[3]
   + 23.33333333333333 yc[4] + 23.33333333333333 yc[5]
   + 23.33333333333333 yc[6] + 23.33333333333333 yc[7]
   + 23.33333333333333 yc[8] - 18.88888888888889 zw[0]
   - 18.88888888888889 zw[1] - 18.88888888888889 zw[2]
   - 18.88888888888889 zw[3] - 18.88888888888889 zw[4]
   - 18.88888888888889 zw[5] - 18.88888888888889 zw[6]
   - 18.88888888888889 zw[7] - 18.88888888888889 zw[8]
   - 16.66666666666666 zc[0] - 16.66666666666666 zc[1]
   - 16.66666666666666 zc[2] - 16.66666666666666 zc[3]
   - 16.66666666666666 zc[4] - 16.66666666666666 zc[5]
   - 16.66666666666666 zc[6] - 16.66666666666666 zc[7]
   - 16.66666666666666 zc[8] - 4 zb[0] - 4 zb[1] - 4 zb[2] - 4 zb[3]
   - 4 zb[4] - 4 zb[5] - 4 zb[6] - 4 zb[7] - 4 zb[8]
   - 1.111111111111111 zbb[0] - 1.111111111111111 zbb[1]
   - 1.111111111111111 zbb[2] - 1.111111111111111 zbb[3]
   - 1.111111111111111 zbb[4] - 1.111111111111111 zbb[5]
   - 1.111111111111111 zbb[6] - 1.111111111111111 zbb[7]
   - 1.111111111111111 zbb[8] + 100000 vw[0] + 100000 vw[1] + 100000 vw[2]
   + 100000 vw[3] + 100000 vw[4] + 100000 vw[5] + 100000 vw[6]
   + 100000 vw[7] + 100000 vw[8] + 100000 vc[0] + 100000 vc[1]
   + 100000 vc[2] + 100000 vc[3] + 100000 vc[4] + 100000 vc[5]
   + 100000 vc[6] + 100000 vc[7] + 100000 vc[8] + 100000 vb[0]
   + 100000 vb[1] + 100000 vb[2] + 100000 vb[3] + 100000 vb[4]
   + 100000 vb[5] + 100000 vb[6] + 100000 vb[7] + 100000 vb[8]
   + 100000 vbb[0] + 100000 vbb[1] + 100000 vbb[2] + 100000 vbb[3]
   + 100000 vbb[4] + 100000 vbb[5] + 100000 vbb[6] + 100000 vbb[7]
   + 100000 vbb[8]
Subject To
 Surfaceacres: x[0] + x[1] + x[2] + ux + v = 500
 wheatrequirement[0]: 4.5 x[0] + yw[0] - zw[0] - uw[0] + vw[0] = 200
 wheatrequirement[1]: 4 x[0] + yw[1] - zw[1] - uw[1] + vw[1] = 200
 wheatrequirement[2]: 3.5 x[0] + yw[2] - zw[2] - uw[2] + vw[2] = 200
 wheatrequirement[3]: 3 x[0] + yw[3] - zw[3] - uw[3] + vw[3] = 200
 wheatrequirement[4]: 2.5 x[0] + yw[4] - zw[4] - uw[4] + vw[4] = 200
 wheatrequirement[5]: 2 x[0] + yw[5] - zw[5] - uw[5] + vw[5] = 200
 wheatrequirement[6]: 1.5 x[0] + yw[6] - zw[6] - uw[6] + vw[6] = 200
 wheatrequirement[7]: x[0] + yw[7] - zw[7] - uw[7] + vw[7] = 200
 wheatrequirement[8]: 0.5 x[0] + yw[8] - zw[8] - uw[8] + vw[8] = 200
 cornrequirement[0]: 5.4 x[1] + yc[0] - zc[0] - uc[0] + vc[0] = 240
 cornrequirement[1]: 4.8 x[1] + yc[1] - zc[1] - uc[1] + vc[1] = 240
 cornrequirement[2]: 4.2 x[1] + yc[2] - zc[2] - uc[2] + vc[2] = 240
 cornrequirement[3]: 3.6 x[1] + yc[3] - zc[3] - uc[3] + vc[3] = 240
 cornrequirement[4]: 3 x[1] + yc[4] - zc[4] - uc[4] + vc[4] = 240
 cornrequirement[5]: 2.4 x[1] + yc[5] - zc[5] - uc[5] + vc[5] = 240
 cornrequirement[6]: 1.8 x[1] + yc[6] - zc[6] - uc[6] + vc[6] = 240
 cornrequirement[7]: 1.2 x[1] + yc[7] - zc[7] - uc[7] + vc[7] = 240
 cornrequirement[8]: 0.6 x[1] + yc[8] - zc[8] - uc[8] + vc[8] = 240
 beansold[0]: - 36 x[2] + zb[0] + zbb[0] + ub[0] + vb[0] = 0
 beansold[1]: - 32 x[2] + zb[1] + zbb[1] + ub[1] + vb[1] = 0
 beansold[2]: - 28 x[2] + zb[2] + zbb[2] + ub[2] + vb[2] = 0
 beansold[3]: - 24 x[2] + zb[3] + zbb[3] + ub[3] + vb[3] = 0
 beansold[4]: - 20 x[2] + zb[4] + zbb[4] + ub[4] + vb[4] = 0
 beansold[5]: - 16 x[2] + zb[5] + zbb[5] + ub[5] + vb[5] = 0
 beansold[6]: - 12 x[2] + zb[6] + zbb[6] + ub[6] + vb[6] = 0
 beansold[7]: - 8 x[2] + zb[7] + zbb[7] + ub[7] + vb[7] = 0
 beansold[8]: - 4 x[2] + zb[8] + zbb[8] + ub[8] + vb[8] = 0
 beansoldlimit[0]: zb[0] + ubb[0] + vbb[0] = 6000
 beansoldlimit[1]: zb[1] + ubb[1] + vbb[1] = 6000
 beansoldlimit[2]: zb[2] + ubb[2] + vbb[2] = 6000
 beansoldlimit[3]: zb[3] + ubb[3] + vbb[3] = 6000
 beansoldlimit[4]: zb[4] + ubb[4] + vbb[4] = 6000
 beansoldlimit[5]: zb[5] + ubb[5] + vbb[5] = 6000
 beansoldlimit[6]: zb[6] + ubb[6] + vbb[6] = 6000
 beansoldlimit[7]: zb[7] + ubb[7] + vbb[7] = 6000
 beansoldlimit[8]: zb[8] + ubb[8] + vbb[8] = 6000
Bounds
End

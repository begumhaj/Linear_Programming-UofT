\ Model Farming Ted-Dual
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
 
Subject To
 linkingconstraints: - x + 3.5 y1[1] + 3 y1[2] + 2.5 y1[3] + 2 y1[4]
   + 1.5 y1[5] + l[0] + la[0] = 150
 linkingconstraints: - x + 4.2 y2[1] + 3.6 y2[2] + 3 y2[3] + 2.4 y2[4]
   + 1.8 y2[5] + l[1] + la[1] = 230
 linkingconstraints: - x + 28 y3[1] + 24 y3[2] + 20 y3[3] + 16 y3[4]
   + 12 y3[5] + l[2] + la[2] = 260
 sub1: y1[1] + s1[1] + a1[1] = 47.6
 sub2: y1[1] - s2[1] + a2[1] = 34
 sub3: y2[1] + s3[1] + a3[1] = 42
 sub4: y2[1] - s4[1] + a4[1] = 30
 sub5: y3[1] + y4[1] - s5[1] + a5[1] = 7.2
 sub6: y3[1] - s6[1] + a6[1] = 2
 sub1: y1[2] + s1[2] + a1[2] = 47.6
 sub2: y1[2] - s2[2] + a2[2] = 34
 sub3: y2[2] + s3[2] + a3[2] = 42
 sub4: y2[2] - s4[2] + a4[2] = 30
 sub5: y3[2] + y4[2] - s5[2] + a5[2] = 7.2
 sub6: y3[2] - s6[2] + a6[2] = 2
 sub1: y1[3] + s1[3] + a1[3] = 47.6
 sub2: y1[3] - s2[3] + a2[3] = 34
 sub3: y2[3] + s3[3] + a3[3] = 42
 sub4: y2[3] - s4[3] + a4[3] = 30
 sub5: y3[3] + y4[3] - s5[3] + a5[3] = 7.2
 sub6: y3[3] - s6[3] + a6[3] = 2
 sub1: y1[4] + s1[4] + a1[4] = 47.6
 sub2: y1[4] - s2[4] + a2[4] = 34
 sub3: y2[4] + s3[4] + a3[4] = 42
 sub4: y2[4] - s4[4] + a4[4] = 30
 sub5: y3[4] + y4[4] - s5[4] + a5[4] = 7.2
 sub6: y3[4] - s6[4] + a6[4] = 2
 sub1: y1[5] + s1[5] + a1[5] = 47.6
 sub2: y1[5] - s2[5] + a2[5] = 34
 sub3: y2[5] + s3[5] + a3[5] = 42
 sub4: y2[5] - s4[5] + a4[5] = 30
 sub5: y3[5] + y4[5] - s5[5] + a5[5] = 7.2
 sub6: y3[5] - s6[5] + a6[5] = 2
Bounds
End

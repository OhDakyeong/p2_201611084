import math
mylocation=[(37.575816, 126.973320)]
locations=[(37.574555, 126.957788),
            (37.576459, 126.986073),
            (37.589141, 126.943762),
            (37.572576, 126.990543)]
distance=list()
for i in locations:
    distance.append(math.sqrt((37.575816-i[0])**2 + (126.973320-i[1])**2))
print distance
print "Minimum distance is ",min(distance)



population=[(74425, 76326),
            (61164, 61636),
            (109688, 115744),
            (144796, 146776),
            (174996, 181676),
            (177841, 177434),
            (204630, 205980),
            (223373, 232245),
            (161055, 166130),
            (171576, 176735),
            (279169, 293772),
            (239450, 251066),
            (148690, 156510),
            (182977, 196992),
            (237792, 242641),
            (283869, 296762),
            (209344, 210282),
            (118965, 114441),
            (186503, 186856),
            (195734, 203014),
            (254381, 249472),
            (212401, 229111),
            (271654, 295354),
            (319197, 335045),
            (229829, 231671)]
m=0.
averageM=0.
for i in range(0,len(population)):
    m=m+population[i][0]
print "The total man is ",m
averageM = m / len(population)
print "The average number of man per area is ",averageM

f=0.
averageF=0.
for i in range(0,len(population)):
    f=f+population[i][1]
print "The total woman is ", f
averageF= f / len(population)
print "The average number of woman per area is ", averageF


import matplotlib
import matplotlib.pyplot as plt
jr=(74425,76326)
jg=(61164 ,61636)
ys=(109688, 115744)
sd=(144796, 146776)
gj=(174996, 181676)
ddm=(177841, 177434)
jl=(204630, 205980)
sb=(223373, 232245)
gb=(161055, 166130)
db=(171576, 176735)
nw=(279169, 293772)
ep=(239450, 251066)
sdm=(148690, 156510)
mp=(182977, 196992)
yc=(237792, 242641)
gs=(283869, 296762)
gr=(209344, 210282)
gc=(118965, 114441)
ydp=(186503, 186856)
dj=(195734, 203014)
ga=(254381, 249472)
sc=(212401, 229111)
gn=(271654, 295354)
sp=(319197, 335045)
gd=(229829, 231671)

seoul={"jongro":jr,
     "joongu":jg,
     "yongsan":ys,
     "sungdong":sd,
     "gwangjin":gj,
     "dongdaemun":ddm,
     "joonglang":jl,
     "sungbuk":sb,
     "gangbuk":gb,
     "dobong":db,
     "nowon":nw,
     "enpyeong":ep,
     "seodaemun":sdm,
     "mapo":mp,
     "yangchub":yc,
     "gangseo":gs,
     "guro":gr,
     "gumchun":gc,
     "yungdeongpo":ydp,
     "dongjak":dj,
     "gwanak":ga,
     "seocho":sc,
     "gangnam":gn,
     "songpa":sp,
     "gangdong":gd}

d=dict()
for i in seoul:
    d[str(i)]=seoul[i][0]+seoul[i][1]
plt.bar(range(len(d)),d.values(), align="center")
plt.xticks(range(len(d)), list(d.keys()))
plt.show()
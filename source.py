def f_3fc2849(a,b,c,d,e,f):
    return (a*b-c*d*e-f)%10
def f_404f934(a,b,c):
    return (a*b*c+f_3fc2849(a,b,c,795,8,396))%10
def f_4829a46(a,b):
    return (a*b+f_404f934(a,b,245)+f_3fc2849(a,b,164,482,679,900))%10
def f_5e65c19(a,b,c):
    return (a-b-c+f_404f934(a,b,c))%10
def f_3e77575(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c*d-e*f-g+h+i+j+f_404f934(a,b,c)+f_404f934(a,b,c))%10
def f_11e6a4f(a,b,c,d,e,f):
    return (a-b-c-d-e+f+f_4829a46(a,b)+f_4829a46(a,b)+f_3fc2849(a,b,c,d,e,f))%10
def f_276f04f(a,b,c,d):
    return (a-b*c*d+f_3fc2849(a,b,c,d,520,699)+f_11e6a4f(a,b,c,d,959,507)+f_4829a46(a,b))%10
def f_44bbc00(a,b,c,d,e,f,g,h,i,j):
    return (a-b+c+d+e-f*g-h-i+j+f_404f934(a,b,c)+f_11e6a4f(a,b,c,d,e,f)+f_276f04f(a,b,c,d))%10
def f_323e173(a,b,c,d,e,f,g,h):
    return (a*b-c*d+e*f-g+h+f_4829a46(a,b)+f_44bbc00(a,b,c,d,e,f,g,h,181,670)+f_276f04f(a,b,c,d))%10
def f_10a1d56(a):
    return (a+f_404f934(a,111,188))%10
def f_1537206(a,b,c,d,e,f):
    return (a+b+c-d*e+f+f_44bbc00(a,b,c,d,e,f,188,162,484,148))%10
def f_1543215(a,b,c):
    return (a*b*c+f_10a1d56(a)+f_44bbc00(a,b,c,818,340,752,392,516,415,260)+f_11e6a4f(a,b,c,238,530,556))%10
def f_70450f(a,b):
    return (a-b+f_4829a46(a,b))%10
def f_21e3b2e(a,b,c,d,e,f,g,h):
    return (a*b-c-d+e*f-g*h+f_276f04f(a,b,c,d)+f_11e6a4f(a,b,c,d,e,f)+f_5e65c19(a,b,c))%10
def f_3179eb1(a,b,c,d,e,f,g,h,i):
    return (a+b+c*d*e+f-g+h+i+f_4829a46(a,b)+f_404f934(a,b,c))%10
def f_5d6c325(a,b,c):
    return (a*b-c+f_3e77575(a,b,c,315,576,486,967,184,2,338)+f_70450f(a,b)+f_323e173(a,b,c,475,446,859,898,485))%10
def f_3baeede(a,b,c,d,e,f,g,h,i):
    return (a*b*c-d+e-f+g+h+i+f_3179eb1(a,b,c,d,e,f,g,h,i)+f_44bbc00(a,b,c,d,e,f,g,h,i,335)+f_3fc2849(a,b,c,d,e,f))%10
def f_60d002(a,b,c):
    return (a+b+c+f_11e6a4f(a,b,c,505,283,95)+f_3e77575(a,b,c,231,536,582,911,319,606,57))%10
def f_982326(a,b):
    return (a-b+f_1543215(a,b,550)+f_3e77575(a,b,48,38,333,831,333,905,226,411))%10
def f_516909d(a,b,c,d):
    return (a*b*c*d+f_276f04f(a,b,c,d)+f_21e3b2e(a,b,c,d,456,891,598,573)+f_5e65c19(a,b,c))%10
def f_434092a(a,b,c,d,e,f,g,h,i,j):
    return (a-b*c+d-e+f+g*h*i+j+f_5e65c19(a,b,c)+f_516909d(a,b,c,d)+f_5d6c325(a,b,c))%10
def f_95c5a4(a,b):
    return (a*b+f_434092a(a,b,565,793,600,255,136,291,472,773)+f_11e6a4f(a,b,155,641,756,593))%10
def f_1c44cb0(a,b,c,d,e,f,g,h,i):
    return (a-b+c-d-e+f-g-h-i+f_3179eb1(a,b,c,d,e,f,g,h,i)+f_3e77575(a,b,c,d,e,f,g,h,i,737)+f_44bbc00(a,b,c,d,e,f,g,h,i,719))%10
def f_1ce677a(a,b,c):
    return (a+b+c+f_323e173(a,b,c,512,416,313,964,3)+f_516909d(a,b,c,633)+f_5e65c19(a,b,c))%10
def f_521625(a,b,c):
    return (a-b-c+f_982326(a,b)+f_516909d(a,b,c,83)+f_3e77575(a,b,c,632,28,367,275,684,109,746))%10
def f_154f682(a,b,c,d,e,f,g):
    return (a-b*c-d+e-f-g+f_404f934(a,b,c)+f_3fc2849(a,b,c,d,e,f)+f_3179eb1(a,b,c,d,e,f,g,163,617))%10
def f_2b14842(a,b,c,d,e):
    return (a-b*c+d+e+f_10a1d56(a)+f_1537206(a,b,c,d,e,321)+f_4829a46(a,b))%10
def f_267eeba(a,b,c,d,e,f,g,h,i):
    return (a-b*c*d-e-f*g*h*i+f_10a1d56(a))%10
def f_943895(a,b,c,d,e,f,g,h,i,j):
    return (a+b*c-d-e-f-g*h-i-j+f_5e65c19(a,b,c)+f_3e77575(a,b,c,d,e,f,g,h,i,j)+f_521625(a,b,c))%10
def f_4561101(a,b,c,d,e,f,g,h,i):
    return (a-b+c+d-e-f+g*h*i+f_44bbc00(a,b,c,d,e,f,g,h,i,47)+f_44bbc00(a,b,c,d,e,f,g,h,i,147))%10
def f_2d2e151(a):
    return (a+f_1c44cb0(a,211,154,183,863,523,171,643,100))%10
def f_5db3fab(a,b,c,d,e):
    return (a+b+c-d*e+f_1543215(a,b,c)+f_521625(a,b,c))%10
def f_4b80977(a,b,c,d,e,f):
    return (a-b*c-d+e-f+f_276f04f(a,b,c,d)+f_4561101(a,b,c,d,e,f,259,152,779))%10
def f_25fb1da(a,b,c,d,e,f,g):
    return (a*b+c*d-e*f+g+f_3e77575(a,b,c,d,e,f,g,671,573,64)+f_1543215(a,b,c))%10
def f_dfc6ca(a,b,c):
    return (a+b+c+f_982326(a,b))%10
def f_f79bd0(a,b,c,d,e,f,g,h,i,j):
    return (a+b-c*d*e+f*g*h-i+j+f_2b14842(a,b,c,d,e))%10
def f_4daee6(a):
    return (a+f_1c44cb0(a,928,870,93,587,425,416,271,747))%10
def f_496990b(a,b,c,d,e):
    return (a-b+c+d+e+f_404f934(a,b,c))%10
def f_5b6d309(a,b):
    return (a-b+f_1543215(a,b,539)+f_1ce677a(a,b,797)+f_1c44cb0(a,b,211,509,871,106,874,536,397))%10
def f_4aecd47(a,b,c,d,e,f,g,h):
    return (a-b*c-d*e-f+g+h+f_276f04f(a,b,c,d))%10
def f_3d93229(a,b,c,d):
    return (a-b*c+d+f_1ce677a(a,b,c)+f_404f934(a,b,c))%10
def f_1d21f7d(a,b,c,d,e,f,g,h,i):
    return (a+b*c-d*e+f+g*h-i+f_323e173(a,b,c,d,e,f,g,h)+f_3e77575(a,b,c,d,e,f,g,h,i,294)+f_3d93229(a,b,c,d))%10
def f_270f3be(a):
    return (a+f_4b80977(a,387,976,27,654,588)+f_25fb1da(a,414,415,117,8,889,663))%10
def f_5c56b8b(a,b,c):
    return (a+b*c+f_11e6a4f(a,b,c,379,258,45)+f_95c5a4(a,b)+f_323e173(a,b,c,779,254,317,499,649))%10
def f_43b5b8c(a,b,c,d,e,f,g):
    return (a*b+c+d+e*f-g+f_dfc6ca(a,b,c)+f_5c56b8b(a,b,c)+f_f79bd0(a,b,c,d,e,f,g,318,331,144))%10
def f_2038f07(a,b,c,d,e,f,g,h,i):
    return (a*b+c*d+e-f*g*h-i+f_276f04f(a,b,c,d)+f_3fc2849(a,b,c,d,e,f)+f_21e3b2e(a,b,c,d,e,f,g,h))%10
def f_513f75a(a,b,c,d,e,f):
    return (a+b+c-d-e-f+f_43b5b8c(a,b,c,d,e,f,760)+f_4daee6(a)+f_434092a(a,b,c,d,e,f,972,63,931,735))%10
def f_5b915db(a,b,c,d,e,f):
    return (a+b-c-d*e-f+f_154f682(a,b,c,d,e,f,124))%10
def f_4685338(a,b,c,d,e,f,g,h,i):
    return (a+b+c-d+e+f+g+h-i+f_1543215(a,b,c)+f_10a1d56(a))%10
def f_4219d3d(a,b,c,d,e,f,g,h,i):
    return (a+b*c-d-e-f+g+h*i+f_4aecd47(a,b,c,d,e,f,g,h))%10
def f_2d2468e(a,b,c,d,e):
    return (a+b+c+d+e+f_2b14842(a,b,c,d,e)+f_496990b(a,b,c,d,e)+f_11e6a4f(a,b,c,d,e,291))%10
def f_2980ac2(a,b,c,d,e):
    return (a*b+c*d*e+f_3179eb1(a,b,c,d,e,692,428,848,728)+f_5d6c325(a,b,c)+f_4daee6(a))%10
def f_3db47ef(a,b,c,d):
    return (a*b*c-d+f_3fc2849(a,b,c,d,901,974)+f_267eeba(a,b,c,d,358,607,314,270,117))%10
def f_29beb15(a,b,c):
    return (a*b-c+f_43b5b8c(a,b,c,74,633,468,579)+f_2d2468e(a,b,c,811,996)+f_513f75a(a,b,c,29,697,916))%10
def f_e17983(a,b):
    return (a*b+f_25fb1da(a,b,106,737,297,834,753)+f_1c44cb0(a,b,482,502,894,841,589,191,175))%10
def f_328ab5b(a,b,c,d,e,f,g,h,i):
    return (a*b*c*d-e*f*g+h+i+f_1537206(a,b,c,d,e,f))%10
def f_2118f76(a,b,c,d,e,f,g,h,i):
    return (a*b*c-d+e*f*g-h+i+f_3d93229(a,b,c,d)+f_943895(a,b,c,d,e,f,g,h,i,213)+f_513f75a(a,b,c,d,e,f))%10
def f_1026acb(a,b):
    return (a*b+f_4aecd47(a,b,682,979,91,181,468,330)+f_521625(a,b,863))%10
def f_5eec931(a,b,c):
    return (a+b+c+f_e17983(a,b)+f_521625(a,b,c))%10
def f_4ef43d8(a):
    return (a+f_4685338(a,939,575,609,755,167,70,703,541)+f_2980ac2(a,971,828,710,372))%10
def f_48876b1(a,b,c,d,e):
    return (a*b*c-d-e+f_328ab5b(a,b,c,d,e,687,252,243,399)+f_5c56b8b(a,b,c))%10
def f_dc3902(a,b,c,d,e,f,g,h,i,j):
    return (a+b*c+d-e-f*g+h*i+j+f_1ce677a(a,b,c)+f_1c44cb0(a,b,c,d,e,f,g,h,i))%10
def f_385ec(a,b,c,d,e,f,g,h):
    return (a*b+c*d-e+f+g+h+f_3179eb1(a,b,c,d,e,f,g,h,928)+f_404f934(a,b,c)+f_404f934(a,b,c))%10
def f_99b8eb(a,b,c,d):
    return (a-b+c*d+f_44bbc00(a,b,c,d,494,175,234,761,38,945))%10
def f_33d1eb4(a,b,c,d,e,f,g):
    return (a-b-c+d+e-f+g+f_1d21f7d(a,b,c,d,e,f,g,904,948)+f_4aecd47(a,b,c,d,e,f,g,459)+f_1026acb(a,b))%10
def f_1a4f4e5(a,b,c,d):
    return (a*b*c+d+f_4aecd47(a,b,c,d,222,402,880,448)+f_434092a(a,b,c,d,743,339,981,199,664,86))%10
def f_531a91b(a,b):
    return (a*b+f_2d2468e(a,b,780,884,909)+f_5e65c19(a,b,755)+f_95c5a4(a,b))%10
def f_1a5d76b(a):
    return (a+f_e17983(a,682)+f_f79bd0(a,911,947,778,697,35,875,264,226,310))%10
def f_1df309(a,b,c,d,e,f,g):
    return (a*b*c+d+e-f+g+f_70450f(a,b))%10
def f_14d0721(a,b,c,d,e,f,g,h,i):
    return (a-b+c*d*e*f-g*h*i+f_4ef43d8(a)+f_2d2468e(a,b,c,d,e))%10
def f_42b43a6(a,b,c,d,e,f,g,h):
    return (a*b*c-d*e-f+g-h+f_43b5b8c(a,b,c,d,e,f,g)+f_2038f07(a,b,c,d,e,f,g,h,33)+f_3fc2849(a,b,c,d,e,f))%10
def f_26b5f98(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c*d-e*f+g*h*i*j+f_385ec(a,b,c,d,e,f,g,h)+f_5d6c325(a,b,c))%10
def f_3b71344(a,b,c,d,e,f,g,h):
    return (a*b+c+d*e-f-g+h+f_f79bd0(a,b,c,d,e,f,g,h,449,233))%10
def f_27e5639(a,b,c,d,e,f,g):
    return (a-b-c-d*e*f*g+f_531a91b(a,b)+f_2980ac2(a,b,c,d,e))%10
def f_91596(a):
    return (a+f_2118f76(a,982,165,659,502,50,541,484,274))%10
def f_30c3354(a,b,c,d,e,f):
    return (a-b*c*d*e*f+f_33d1eb4(a,b,c,d,e,f,917))%10
def f_4b32a8a(a,b,c,d,e,f):
    return (a*b*c*d+e+f+f_385ec(a,b,c,d,e,f,953,474))%10
def f_19797f(a,b,c,d):
    return (a*b+c-d+f_91596(a)+f_21e3b2e(a,b,c,d,591,344,208,290)+f_323e173(a,b,c,d,195,155,55,46))%10
def f_461efc8(a,b,c,d,e,f,g,h):
    return (a*b-c-d*e-f+g-h+f_e17983(a,b)+f_531a91b(a,b)+f_99b8eb(a,b,c,d))%10
def f_2a6382f(a,b,c,d,e,f,g,h,i,j):
    return (a-b+c+d*e*f-g+h-i+j+f_3179eb1(a,b,c,d,e,f,g,h,i))%10
def f_1ced336(a,b,c,d,e):
    return (a+b-c-d-e+f_516909d(a,b,c,d))%10
def f_4eb2186(a,b):
    return (a+b+f_29beb15(a,b,872))%10
def f_315996e(a,b,c):
    return (a-b-c+f_3fc2849(a,b,c,836,318,119)+f_44bbc00(a,b,c,600,35,775,264,532,381,379))%10
def f_4d0a9a0(a,b,c,d,e,f,g):
    return (a*b-c-d-e+f-g+f_5db3fab(a,b,c,d,e)+f_1d21f7d(a,b,c,d,e,f,g,165,920)+f_323e173(a,b,c,d,e,f,g,475))%10
def f_5146ecb(a,b,c,d,e,f,g):
    return (a+b+c+d*e*f-g+f_4685338(a,b,c,d,e,f,g,732,166)+f_4829a46(a,b)+f_521625(a,b,c))%10
def f_2312b67(a,b,c,d,e,f,g,h,i):
    return (a*b*c*d*e-f+g*h*i+f_1df309(a,b,c,d,e,f,g)+f_323e173(a,b,c,d,e,f,g,h))%10
def f_4fe1fea(a,b,c,d,e,f,g):
    return (a*b-c*d*e+f-g+f_14d0721(a,b,c,d,e,f,g,183,346)+f_19797f(a,b,c,d))%10
def f_e73849(a,b,c,d):
    return (a+b-c+d+f_5c56b8b(a,b,c)+f_26b5f98(a,b,c,d,237,764,815,332,457,45))%10
def f_3602881(a,b,c,d,e,f):
    return (a*b+c+d*e+f+f_1c44cb0(a,b,c,d,e,f,581,217,466)+f_404f934(a,b,c)+f_434092a(a,b,c,d,e,f,872,991,345,185))%10
def f_1399b76(a,b):
    return (a*b+f_5146ecb(a,b,470,210,26,350,872)+f_385ec(a,b,288,595,950,128,897,141))%10
def f_312a318(a,b,c,d,e,f):
    return (a*b-c+d*e-f+f_25fb1da(a,b,c,d,e,f,954)+f_3e77575(a,b,c,d,e,f,637,137,224,441))%10
def f_3ee3b81(a,b,c,d,e,f):
    return (a*b*c-d*e*f+f_25fb1da(a,b,c,d,e,f,166))%10
def f_90c07b(a,b,c,d,e):
    return (a*b-c-d+e+f_95c5a4(a,b)+f_dfc6ca(a,b,c)+f_33d1eb4(a,b,c,d,e,236,767))%10
def f_3901b28(a,b,c,d,e,f,g,h):
    return (a*b+c-d*e*f-g+h+f_1026acb(a,b)+f_5146ecb(a,b,c,d,e,f,g)+f_1d21f7d(a,b,c,d,e,f,g,h,317))%10
def f_325d499(a,b):
    return (a+b+f_43b5b8c(a,b,884,830,508,114,421)+f_1399b76(a,b)+f_4fe1fea(a,b,11,737,255,722,782))%10
def f_5e6c9d6(a,b,c,d,e,f,g,h):
    return (a-b+c*d*e+f*g-h+f_982326(a,b)+f_323e173(a,b,c,d,e,f,g,h)+f_3901b28(a,b,c,d,e,f,g,h))%10
def f_2e3073c(a,b,c,d,e,f,g,h,i,j):
    return (a+b*c*d+e*f*g+h*i-j+f_5c56b8b(a,b,c))%10
def f_23c61d8(a,b,c,d,e,f,g,h,i):
    return (a+b-c+d*e*f-g-h*i+f_91596(a))%10
def f_1e0f2ac(a,b,c,d,e):
    return (a*b+c-d-e+f_154f682(a,b,c,d,e,22,8))%10
def f_342de1c(a,b,c):
    return (a*b*c+f_11e6a4f(a,b,c,573,112,823)+f_315996e(a,b,c))%10
def f_3d5149e(a,b,c,d,e,f,g,h,i,j):
    return (a*b-c-d-e*f*g+h*i-j+f_1ced336(a,b,c,d,e)+f_982326(a,b))%10
def f_313e9b5(a,b,c,d):
    return (a*b+c*d+f_1ced336(a,b,c,d,280)+f_3b71344(a,b,c,d,722,166,630,390)+f_4fe1fea(a,b,c,d,721,952,217))%10
def f_5a33a53(a,b):
    return (a+b+f_26b5f98(a,b,142,152,992,684,885,86,952,196)+f_4daee6(a))%10
def f_1ca99e6(a,b,c,d,e,f,g,h,i,j):
    return (a-b-c-d-e+f-g*h+i*j+f_26b5f98(a,b,c,d,e,f,g,h,i,j)+f_4d0a9a0(a,b,c,d,e,f,g))%10
def f_b8a492(a,b,c,d,e,f,g,h,i):
    return (a*b-c-d-e-f+g*h+i+f_48876b1(a,b,c,d,e)+f_30c3354(a,b,c,d,e,f)+f_4fe1fea(a,b,c,d,e,f,g))%10
def f_5cff6dd(a,b,c,d,e,f):
    return (a-b*c+d+e-f+f_5146ecb(a,b,c,d,e,f,807)+f_2312b67(a,b,c,d,e,f,896,499,696))%10
def f_4f47e84(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c+d-e+f-g*h*i*j+f_1537206(a,b,c,d,e,f)+f_43b5b8c(a,b,c,d,e,f,g)+f_95c5a4(a,b))%10
def f_3f26d4f(a,b,c,d,e,f,g):
    return (a*b-c+d-e-f*g+f_99b8eb(a,b,c,d)+f_5eec931(a,b,c))%10
def f_6ad18c(a,b,c):
    return (a*b+c+f_521625(a,b,c))%10
def f_1ba6eba(a,b,c,d,e,f,g):
    return (a*b*c-d*e+f*g+f_3602881(a,b,c,d,e,f)+f_4219d3d(a,b,c,d,e,f,g,986,631))%10
def f_17a71e9(a,b,c,d,e,f,g,h,i,j):
    return (a-b+c*d+e-f+g+h+i+j+f_3ee3b81(a,b,c,d,e,f)+f_29beb15(a,b,c)+f_4829a46(a,b))%10
def f_3370a3a(a,b,c,d):
    return (a+b-c+d+f_4daee6(a)+f_1ce677a(a,b,c)+f_2980ac2(a,b,c,d,104))%10
def f_1adec04(a,b,c):
    return (a*b-c+f_270f3be(a)+f_313e9b5(a,b,c,457)+f_1c44cb0(a,b,c,225,553,110,57,690,816))%10
def f_3e8aba5(a,b,c,d):
    return (a-b*c*d+f_2d2468e(a,b,c,d,336)+f_4219d3d(a,b,c,d,541,176,338,563,603))%10
def f_58bc2(a,b,c,d):
    return (a-b-c-d+f_2d2e151(a)+f_1a4f4e5(a,b,c,d)+f_3901b28(a,b,c,d,793,343,534,372))%10
def f_1b33739(a,b,c,d,e,f):
    return (a+b*c-d+e+f+f_60d002(a,b,c)+f_3901b28(a,b,c,d,e,f,621,288)+f_3901b28(a,b,c,d,e,f,382,984))%10
def f_33e0fde(a,b):
    return (a-b+f_434092a(a,b,57,251,907,397,249,477,178,399)+f_1537206(a,b,71,338,63,134))%10
def f_43b6a1e(a,b,c,d,e,f,g,h):
    return (a+b+c*d+e+f*g+h+f_4829a46(a,b)+f_2d2e151(a)+f_1df309(a,b,c,d,e,f,g))%10
def f_5edabd1(a,b,c,d,e,f,g,h,i):
    return (a-b-c*d+e-f+g-h*i+f_6ad18c(a,b,c)+f_4b32a8a(a,b,c,d,e,f)+f_2980ac2(a,b,c,d,e))%10
def f_5809bdc(a,b,c):
    return (a*b*c+f_6ad18c(a,b,c)+f_4ef43d8(a))%10
def f_3a65141(a,b,c,d,e,f):
    return (a*b-c+d+e-f+f_4685338(a,b,c,d,e,f,934,408,609)+f_3d93229(a,b,c,d))%10
def f_1a4a712(a,b):
    return (a*b+f_4685338(a,b,499,866,984,782,209,158,818)+f_91596(a)+f_404f934(a,b,423))%10
def f_50fb1b3(a,b,c,d,e,f,g):
    return (a*b*c*d*e*f*g+f_404f934(a,b,c)+f_4ef43d8(a)+f_dc3902(a,b,c,d,e,f,g,343,524,30))%10
def f_2bbc1b(a,b,c,d,e,f,g):
    return (a-b+c*d*e+f*g+f_1a5d76b(a))%10
def f_4dd8575(a,b,c,d,e):
    return (a*b-c+d-e+f_276f04f(a,b,c,d)+f_516909d(a,b,c,d))%10
def f_416ec8a(a,b,c,d,e,f):
    return (a*b*c*d+e+f+f_3e8aba5(a,b,c,d))%10
def f_e1680c(a,b):
    return (a+b+f_5eec931(a,b,102))%10
def f_40dda3b(a,b,c,d,e,f,g,h):
    return (a+b+c+d*e*f-g-h+f_416ec8a(a,b,c,d,e,f)+f_30c3354(a,b,c,d,e,f))%10
def f_22ec421(a,b,c,d,e,f):
    return (a-b-c*d-e-f+f_10a1d56(a)+f_11e6a4f(a,b,c,d,e,f))%10
def f_4a02c54(a,b,c,d,e):
    return (a+b-c-d*e+f_22ec421(a,b,c,d,e,37)+f_17a71e9(a,b,c,d,e,669,313,17,109,97)+f_313e9b5(a,b,c,d))%10
def f_236ac1(a,b,c,d):
    return (a+b-c-d+f_1399b76(a,b)+f_315996e(a,b,c)+f_3901b28(a,b,c,d,564,345,282,988))%10
def f_38f59d6(a,b):
    return (a*b+f_1c44cb0(a,b,361,431,410,227,153,972,802)+f_154f682(a,b,87,323,260,47,564)+f_21e3b2e(a,b,522,420,490,978,638,584))%10
def f_599d433(a,b,c,d,e):
    return (a-b+c*d*e+f_2d2e151(a))%10
def f_e99203(a,b,c):
    return (a*b-c+f_4aecd47(a,b,c,34,101,682,40,187))%10
def f_488a2c0(a,b,c):
    return (a-b+c+f_4a02c54(a,b,c,962,302))%10
def f_15a3573(a,b,c,d,e,f,g):
    return (a*b*c*d-e-f*g+f_1c44cb0(a,b,c,d,e,f,g,296,276)+f_513f75a(a,b,c,d,e,f))%10
def f_31f6789(a,b,c,d,e,f,g,h,i,j):
    return (a*b*c+d+e-f+g-h*i+j+f_4aecd47(a,b,c,d,e,f,g,h))%10
def f_2d34b7f(a,b,c,d,e,f,g,h,i,j):
    return (a+b+c+d-e-f-g-h-i-j+f_325d499(a,b))%10
def f_3c823f9(a,b,c,d):
    return (a-b*c+d+f_2980ac2(a,b,c,d,888)+f_1e0f2ac(a,b,c,d,528)+f_4aecd47(a,b,c,d,195,656,48,677))%10
def f_5b1da69(a,b,c,d,e):
    return (a*b+c*d+e+f_5a33a53(a,b))%10
def f_38c990e(a,b,c):
    return (a-b*c+f_4b80977(a,b,c,784,787,816))%10
def f_3af46d9(a,b,c,d,e,f,g,h):
    return (a-b*c-d+e+f+g-h+f_342de1c(a,b,c))%10
def f_236051d(a,b):
    return (a+b+f_599d433(a,b,742,392,985)+f_2d34b7f(a,b,319,652,599,66,208,458,940,84)+f_43b6a1e(a,b,456,246,115,411,997,133))%10
def f_1132978(a):
    return (a+f_513f75a(a,796,182,411,294,526)+f_70450f(a,566)+f_30c3354(a,729,623,447,147,613))%10
def f_5b18084(a,b,c,d,e,f,g,h,i,j):
    return (a+b-c*d*e*f-g+h-i-j+f_3602881(a,b,c,d,e,f))%10
def f_1185c60(a,b,c,d,e,f,g,h):
    return (a*b+c-d-e-f+g+h+f_1132978(a)+f_e1680c(a,b)+f_516909d(a,b,c,d))%10
def f_17f9f37(a,b,c,d,e,f,g,h,i):
    return (a-b-c-d*e-f+g+h+i+f_6ad18c(a,b,c)+f_4eb2186(a,b)+f_b8a492(a,b,c,d,e,f,g,h,i))%10
def f_3bb6116(a,b,c,d,e,f,g,h):
    return (a*b*c-d*e-f*g-h+f_40dda3b(a,b,c,d,e,f,g,h))%10
def f_58e02bf(a,b,c,d,e,f):
    return (a*b-c-d*e+f+f_2bbc1b(a,b,c,d,e,f,526))%10
def f_1df4418(a,b,c,d,e,f,g):
    return (a*b-c+d-e+f*g+f_1adec04(a,b,c)+f_5e65c19(a,b,c)+f_315996e(a,b,c))%10
def f_271d934(a,b,c,d,e,f,g):
    return (a*b+c-d*e-f+g+f_5a33a53(a,b)+f_1132978(a)+f_323e173(a,b,c,d,e,f,g,123))%10
def f_5c62d79(a,b,c,d,e,f):
    return (a*b-c+d+e-f+f_22ec421(a,b,c,d,e,f)+f_4b80977(a,b,c,d,e,f))%10
def f_574b9d(a,b,c,d,e):
    return (a*b-c-d*e+f_43b6a1e(a,b,c,d,e,734,390,695)+f_267eeba(a,b,c,d,e,83,206,618,977))%10
def f_1f3c995(a,b,c,d,e,f,g,h):
    return (a*b-c-d*e+f*g*h+f_14d0721(a,b,c,d,e,f,g,h,741)+f_1ba6eba(a,b,c,d,e,f,g))%10
def f_3941191(a,b,c,d,e,f,g,h):
    return (a+b*c-d-e-f*g+h+f_3a65141(a,b,c,d,e,f))%10
def f_5c08360(a,b,c,d):
    return (a+b*c+d+f_5809bdc(a,b,c)+f_5e6c9d6(a,b,c,d,550,39,88,13)+f_4daee6(a))%10
def f_4dfa0c1(a,b,c):
    return (a+b*c+f_4daee6(a)+f_1ce677a(a,b,c)+f_2d34b7f(a,b,c,314,213,7,640,302,765,145))%10
def f_2e3793d(a,b,c,d,e,f,g,h,i,j):
    return (a+b*c+d-e*f+g-h*i*j+f_43b6a1e(a,b,c,d,e,f,g,h)+f_f79bd0(a,b,c,d,e,f,g,h,i,j)+f_3db47ef(a,b,c,d))%10
def f_2f9c842(a,b,c,d,e):
    return (a*b*c*d+e+f_f79bd0(a,b,c,d,e,796,603,674,510,937)+f_99b8eb(a,b,c,d)+f_44bbc00(a,b,c,d,e,604,194,642,693,24))%10
def f_8f7c09(a,b,c,d):
    return (a*b+c+d+f_30c3354(a,b,c,d,4,378))%10
def f_1ca9b01(a,b,c,d,e,f,g,h,i):
    return (a+b*c+d-e*f-g-h*i+f_1ced336(a,b,c,d,e)+f_3c823f9(a,b,c,d)+f_27e5639(a,b,c,d,e,f,g))%10
def f_913efb(a,b,c,d,e,f,g,h):
    return (a-b*c-d+e+f-g*h+f_4dfa0c1(a,b,c))%10
def f_40b6207(a,b,c,d,e,f):
    return (a-b*c+d-e-f+f_91596(a)+f_2d34b7f(a,b,c,d,e,f,241,240,799,141)+f_50fb1b3(a,b,c,d,e,f,727))%10
def f_33f699e(a,b,c,d,e,f,g,h,i,j):
    return (a+b-c+d+e+f*g*h*i*j+f_4b80977(a,b,c,d,e,f)+f_3b71344(a,b,c,d,e,f,g,h)+f_4eb2186(a,b))%10
def f_49ccbb5(a):
    return (a+f_4aecd47(a,995,573,460,873,164,572,24))%10
def f_9eacd1(a):
    return (a+f_271d934(a,165,362,558,349,330,554)+f_50fb1b3(a,21,92,207,282,805,846))%10
def f_28cda19(a,b,c,d,e,f,g):
    return (a+b*c+d-e-f-g+f_60d002(a,b,c))%10
def f_3d099c1(a,b,c,d):
    return (a-b+c-d+f_42b43a6(a,b,c,d,737,627,501,679))%10
def f_1ede232(a,b,c,d,e,f,g):
    return (a*b*c+d*e+f+g+f_4219d3d(a,b,c,d,e,f,g,427,806))%10
def f_3ce64d4(a,b):
    return (a-b+f_3d5149e(a,b,487,978,300,972,615,382,740,346)+f_5db3fab(a,b,180,146,215)+f_5b1da69(a,b,763,112,688))%10
def f_fa5c28(a,b,c):
    return (a*b+c+f_58bc2(a,b,c,34)+f_1ced336(a,b,c,554,617)+f_3901b28(a,b,c,402,283,112,772,153))%10
def f_1bb28ac(a,b):
    return (a+b+f_5c62d79(a,b,710,732,373,801)+f_5b6d309(a,b))%10
def f_5410c1d(a,b,c):
    return (a+b*c+f_1ba6eba(a,b,c,571,219,937,78)+f_5a33a53(a,b))%10
def f_58a555f(a,b,c,d):
    return (a+b*c+d+f_4f47e84(a,b,c,d,117,978,834,123,175,669))%10
def f_108ee0a(a,b,c,d,e,f,g,h):
    return (a*b*c-d-e+f+g-h+f_23c61d8(a,b,c,d,e,f,g,h,586)+f_1132978(a)+f_2e3793d(a,b,c,d,e,f,g,h,910,324))%10
def f_cef9d5(a,b,c,d,e,f):
    return (a*b*c+d*e*f+f_328ab5b(a,b,c,d,e,f,510,644,559))%10
def f_5b9613(a,b,c):
    return (a-b*c+f_416ec8a(a,b,c,380,63,806))%10
def f_3b8e5d6(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c-d+e+f*g*h-i*j+f_31f6789(a,b,c,d,e,f,g,h,i,j))%10
def f_6dd0f7(a,b,c,d,e,f):
    return (a+b*c*d+e-f+f_1df4418(a,b,c,d,e,f,691)+f_17a71e9(a,b,c,d,e,f,202,601,370,218))%10
def f_c19fa4(a,b):
    return (a+b+f_2e3073c(a,b,146,522,526,209,681,708,57,850)+f_50fb1b3(a,b,327,371,452,552,67))%10
def f_5efb880(a,b,c,d,e,f,g):
    return (a-b+c*d*e+f-g+f_38c990e(a,b,c)+f_1ede232(a,b,c,d,e,f,g)+f_14d0721(a,b,c,d,e,f,g,284,300))%10
def f_3f11111(a,b,c,d,e):
    return (a-b+c-d*e+f_2e3793d(a,b,c,d,e,930,976,700,372,983)+f_2f9c842(a,b,c,d,e)+f_1ca99e6(a,b,c,d,e,137,442,349,309,348))%10
def f_34698cf(a,b,c,d,e,f):
    return (a-b*c-d-e-f+f_108ee0a(a,b,c,d,e,f,135,123)+f_3602881(a,b,c,d,e,f))%10
def f_2fb588f(a,b):
    return (a*b+f_236051d(a,b)+f_4219d3d(a,b,929,352,641,434,570,36,569)+f_29beb15(a,b,362))%10
def f_4d12f2a(a,b):
    return (a+b+f_3179eb1(a,b,579,878,452,943,172,952,145))%10
def f_435f899(a,b,c,d,e,f,g,h):
    return (a*b*c-d-e-f+g+h+f_4d0a9a0(a,b,c,d,e,f,g)+f_3d93229(a,b,c,d))%10
def f_11b9dd4(a):
    return (a+f_4685338(a,605,104,601,698,218,320,141,31)+f_4561101(a,558,740,441,236,28,485,375,793))%10
def f_2898396(a,b,c,d,e,f):
    return (a-b*c-d+e-f+f_15a3573(a,b,c,d,e,f,778))%10
def f_20148(a,b,c,d,e,f,g,h,i,j):
    return (a*b*c+d*e+f-g+h*i+j+f_3a65141(a,b,c,d,e,f)+f_1a4f4e5(a,b,c,d))%10
def f_80b922(a,b,c,d,e,f):
    return (a*b*c*d*e*f+f_4aecd47(a,b,c,d,e,f,466,159))%10
def f_44057e9(a,b):
    return (a-b+f_58bc2(a,b,232,940))%10
def f_5eb63c3(a,b,c,d,e,f):
    return (a+b+c*d+e*f+f_9eacd1(a))%10
def f_5a92ec4(a):
    return (a+f_513f75a(a,437,274,247,95,795)+f_1537206(a,440,999,120,967,515)+f_3e8aba5(a,231,965,976))%10
def f_24f9f12(a):
    return (a+f_3ee3b81(a,298,267,307,518,547))%10
def f_574c67b(a):
    return (a+f_e17983(a,876))%10
def f_4982e4e(a,b,c,d,e,f,g,h):
    return (a*b*c+d+e-f+g*h+f_20148(a,b,c,d,e,f,g,h,635,218)+f_3e8aba5(a,b,c,d)+f_11b9dd4(a))%10
def f_21eb0c7(a,b,c):
    return (a+b-c+f_49ccbb5(a))%10
def f_5e69b9c(a,b,c,d,e,f):
    return (a+b-c-d*e*f+f_599d433(a,b,c,d,e))%10
def f_42e3747(a):
    return (a+f_1ba6eba(a,482,877,573,811,521,556)+f_58e02bf(a,245,904,443,200,897)+f_2038f07(a,870,605,535,691,279,668,164,859))%10
def f_4bae5af(a,b,c,d):
    return (a+b-c-d+f_3c823f9(a,b,c,d))%10
def f_3a38bc3(a,b,c,d,e,f,g,h,i):
    return (a*b*c*d*e+f*g-h*i+f_c19fa4(a,b))%10
def f_50bf704(a,b,c,d,e,f,g,h,i):
    return (a+b*c+d*e*f+g*h-i+f_2980ac2(a,b,c,d,e)+f_1399b76(a,b))%10
def f_2eab6ae(a,b,c,d,e,f,g,h,i):
    return (a-b*c+d+e*f-g*h-i+f_38f59d6(a,b)+f_33e0fde(a,b)+f_404f934(a,b,c))%10
def f_53187cf(a,b,c,d,e,f,g,h,i):
    return (a*b-c+d-e+f*g*h*i+f_5b18084(a,b,c,d,e,f,g,h,i,150)+f_270f3be(a)+f_6ad18c(a,b,c))%10
def f_2d0b4c9(a,b,c,d,e,f,g,h,i):
    return (a-b*c*d-e+f+g-h*i+f_435f899(a,b,c,d,e,f,g,h))%10
def f_18776c5(a,b,c,d,e,f,g):
    return (a-b*c-d+e-f+g+f_5cff6dd(a,b,c,d,e,f)+f_42e3747(a)+f_3a65141(a,b,c,d,e,f))%10
def f_cf5c2f(a,b,c,d,e,f):
    return (a+b+c*d+e*f+f_4219d3d(a,b,c,d,e,f,914,888,638))%10
def f_3d40505(a):
    return (a+f_49ccbb5(a)+f_17f9f37(a,95,514,190,796,291,645,964,965))%10
def f_11948c1(a,b,c,d,e,f,g,h,i,j):
    return (a*b*c*d-e+f+g+h*i*j+f_1399b76(a,b)+f_1bb28ac(a,b))%10
def f_52a2bc8(a,b,c,d,e,f,g):
    return (a+b-c-d+e+f+g+f_5809bdc(a,b,c))%10
def f_4c17873(a,b,c,d,e,f,g,h,i,j):
    return (a*b-c*d*e-f+g-h-i+j+f_3941191(a,b,c,d,e,f,g,h))%10
def f_d94d4a(a,b,c):
    return (a-b*c+f_2b14842(a,b,c,718,566)+f_325d499(a,b)+f_5d6c325(a,b,c))%10
def f_53cefd9(a,b):
    return (a+b+f_3901b28(a,b,627,866,621,323,623,729)+f_33f699e(a,b,300,287,19,679,847,172,44,488))%10
def f_3bb0985(a,b,c,d):
    return (a+b-c-d+f_3901b28(a,b,c,d,62,707,850,826)+f_1ede232(a,b,c,d,184,836,419))%10
def f_2782f28(a,b,c,d,e,f):
    return (a+b-c+d*e+f+f_5eec931(a,b,c)+f_21e3b2e(a,b,c,d,e,f,772,368))%10
def f_22d2ad7(a,b,c,d,e,f,g,h):
    return (a*b+c-d*e-f-g+h+f_3a38bc3(a,b,c,d,e,f,g,h,690)+f_19797f(a,b,c,d))%10
def f_25adc76(a,b,c):
    return (a+b*c+f_99b8eb(a,b,c,797)+f_53187cf(a,b,c,375,866,729,477,31,858))%10
def f_225d8ca(a,b,c):
    return (a-b+c+f_1ba6eba(a,b,c,199,448,234,217)+f_9eacd1(a))%10
def f_477b1bc(a,b,c,d,e,f,g,h,i):
    return (a*b+c-d+e*f-g+h+i+f_14d0721(a,b,c,d,e,f,g,h,i)+f_1bb28ac(a,b)+f_58a555f(a,b,c,d))%10
def f_4ca92a8(a,b,c,d,e,f,g,h,i,j):
    return (a-b-c-d-e*f+g-h-i+j+f_2898396(a,b,c,d,e,f))%10
def f_28bfb93(a,b,c,d,e,f,g,h):
    return (a-b*c+d-e-f+g*h+f_1a4f4e5(a,b,c,d)+f_58e02bf(a,b,c,d,e,f))%10
def f_fbde91(a,b,c,d,e,f,g,h,i,j):
    return (a-b*c*d-e+f-g+h-i+j+f_6ad18c(a,b,c))%10
def f_55a1960(a,b,c,d,e,f,g,h,i):
    return (a+b+c+d-e+f*g+h-i+f_11948c1(a,b,c,d,e,f,g,h,i,125)+f_5b1da69(a,b,c,d,e))%10
def f_171015f(a,b,c,d,e,f,g):
    return (a*b+c*d+e*f-g+f_496990b(a,b,c,d,e)+f_53cefd9(a,b)+f_5809bdc(a,b,c))%10
def f_35548dd(a,b,c):
    return (a+b-c+f_28bfb93(a,b,c,180,215,449,946,962)+f_1df309(a,b,c,143,160,139,435)+f_3f11111(a,b,c,599,108))%10
def f_16b9868(a,b,c,d,e,f,g,h,i):
    return (a+b-c*d*e*f*g-h+i+f_4a02c54(a,b,c,d,e)+f_4aecd47(a,b,c,d,e,f,g,h))%10
def f_386649d(a,b,c,d,e,f,g):
    return (a*b*c*d+e*f+g+f_516909d(a,b,c,d)+f_1132978(a))%10
def f_4268c37(a,b,c,d,e,f,g):
    return (a+b+c*d+e*f-g+f_23c61d8(a,b,c,d,e,f,g,974,927)+f_2d2468e(a,b,c,d,e)+f_38c990e(a,b,c))%10
def f_1f30af9(a,b,c):
    return (a*b*c+f_10a1d56(a))%10
def f_2ef601b(a,b,c,d,e,f,g,h):
    return (a+b-c*d*e+f-g+h+f_5efb880(a,b,c,d,e,f,g)+f_23c61d8(a,b,c,d,e,f,g,h,458)+f_80b922(a,b,c,d,e,f))%10
def f_289e8f4(a,b,c,d,e,f,g,h,i):
    return (a-b+c-d-e+f+g+h+i+f_5eec931(a,b,c)+f_35548dd(a,b,c)+f_2bbc1b(a,b,c,d,e,f,g))%10
def f_4043c26(a):
    return (a+f_1ba6eba(a,384,279,699,686,166,193)+f_599d433(a,303,941,558,751)+f_3bb0985(a,245,440,202))%10
def f_26a606a(a,b,c,d,e,f,g,h):
    return (a-b*c-d-e*f-g*h+f_516909d(a,b,c,d)+f_fa5c28(a,b,c))%10
def f_4fa4f35(a,b,c,d,e,f,g,h):
    return (a*b+c+d-e+f*g*h+f_21e3b2e(a,b,c,d,e,f,g,h)+f_1f3c995(a,b,c,d,e,f,g,h))%10
def f_1fa9e12(a,b,c,d,e):
    return (a-b*c+d+e+f_2d0b4c9(a,b,c,d,e,925,602,590,788)+f_1ced336(a,b,c,d,e)+f_20148(a,b,c,d,e,923,363,192,843,365))%10
def f_32693b4(a,b,c,d,e,f,g,h,i):
    return (a-b-c+d*e+f+g+h+i+f_4aecd47(a,b,c,d,e,f,g,h))%10
def f_48e7b28(a,b,c):
    return (a-b*c+f_25fb1da(a,b,c,857,856,527,718)+f_fa5c28(a,b,c)+f_271d934(a,b,c,335,31,655,627))%10
def f_431d328(a,b):
    return (a-b+f_cef9d5(a,b,886,638,92,596))%10
def f_8caae1(a,b,c,d,e):
    return (a+b-c-d+e+f_1026acb(a,b))%10
def f_8e5b86(a,b,c,d,e,f,g):
    return (a+b+c*d+e+f+g+f_4fe1fea(a,b,c,d,e,f,g))%10
def f_293206a(a,b,c,d,e):
    return (a-b+c*d+e+f_1adec04(a,b,c)+f_3baeede(a,b,c,d,e,725,50,307,65))%10
def f_365ee7e(a,b,c):
    return (a+b-c+f_99b8eb(a,b,c,889)+f_1399b76(a,b))%10
def f_5accc7d(a,b):
    return (a+b+f_28bfb93(a,b,929,772,980,881,588,254)+f_11948c1(a,b,280,825,153,726,427,148,189,945)+f_30c3354(a,b,83,861,970,833))%10
def f_15cfda7(a):
    return (a+f_3ee3b81(a,452,928,398,986,958))%10
def f_2e9d3eb(a,b):
    return (a-b+f_496990b(a,b,749,864,258)+f_5a92ec4(a))%10
def f_5cc471a(a,b,c,d,e,f,g):
    return (a*b*c-d*e*f*g+f_599d433(a,b,c,d,e)+f_416ec8a(a,b,c,d,e,f)+f_2e9d3eb(a,b))%10
def f_5deee48(a,b,c,d,e,f,g,h,i):
    return (a*b+c-d*e-f*g+h-i+f_48e7b28(a,b,c))%10
def f_244e536(a,b,c,d):
    return (a*b-c-d+f_b8a492(a,b,c,d,770,362,336,174,347))%10
def f_230c9af(a,b):
    return (a+b+f_3baeede(a,b,650,241,684,4,38,879,285))%10
def f_11f43c7(a,b,c,d,e,f,g,h,i,j):
    return (a+b-c*d-e-f*g*h+i+j+f_fa5c28(a,b,c)+f_28bfb93(a,b,c,d,e,f,g,h))%10
def f_2bc694e(a,b,c,d,e,f,g,h):
    return (a*b+c+d+e+f+g-h+f_386649d(a,b,c,d,e,f,g)+f_404f934(a,b,c))%10
def f_25c5319(a,b,c,d,e,f,g,h):
    return (a+b*c+d+e+f*g*h+f_4f47e84(a,b,c,d,e,f,g,h,404,270)+f_4b80977(a,b,c,d,e,f)+f_1d21f7d(a,b,c,d,e,f,g,h,855))%10
def f_38c66e8(a,b,c,d,e):
    return (a+b*c+d*e+f_4043c26(a)+f_28bfb93(a,b,c,d,e,951,497,936))%10
def f_5d2b352(a,b,c,d,e,f,g):
    return (a+b+c-d-e-f-g+f_2d2e151(a)+f_6ad18c(a,b,c)+f_3f26d4f(a,b,c,d,e,f,g))%10
def f_17c122f(a,b,c,d,e):
    return (a+b+c+d*e+f_365ee7e(a,b,c)+f_5d6c325(a,b,c))%10
def f_13071ce(a,b,c,d,e,f,g,h,i,j):
    return (a*b-c+d+e-f+g*h-i+j+f_3e77575(a,b,c,d,e,f,g,h,i,j)+f_8caae1(a,b,c,d,e)+f_3f11111(a,b,c,d,e))%10
def f_32d29e5(a,b,c,d):
    return (a-b-c-d+f_5b6d309(a,b))%10
def f_1a61f2e(a,b,c,d):
    return (a*b*c-d+f_2118f76(a,b,c,d,122,704,494,973,910)+f_3db47ef(a,b,c,d)+f_26b5f98(a,b,c,d,430,187,388,696,826,711))%10
def f_1e458ad(a,b,c,d,e):
    return (a-b-c+d+e+f_dfc6ca(a,b,c))%10
def f_249c03c(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c*d+e+f+g+h+i+j+f_99b8eb(a,b,c,d)+f_3baeede(a,b,c,d,e,f,g,h,i))%10
def f_56b708b(a,b,c,d,e,f):
    return (a-b*c+d+e+f+f_15cfda7(a))%10
def f_131bddd(a,b,c,d):
    return (a+b+c+d+f_26b5f98(a,b,c,d,250,21,56,436,807,3))%10
def f_26fd29(a,b,c,d,e,f,g,h,i):
    return (a*b*c+d+e*f-g+h+i+f_4685338(a,b,c,d,e,f,g,h,i)+f_9eacd1(a)+f_4bae5af(a,b,c,d))%10
def f_ad64c2(a,b,c,d,e,f,g):
    return (a+b*c-d+e-f-g+f_11f43c7(a,b,c,d,e,f,g,731,96,312)+f_574b9d(a,b,c,d,e))%10
def f_1554b36(a,b,c,d,e,f,g,h):
    return (a*b-c*d-e*f*g+h+f_435f899(a,b,c,d,e,f,g,h))%10
def f_d7379d(a):
    return (a+f_33e0fde(a,673))%10
def f_28a147f(a,b,c,d):
    return (a-b+c+d+f_325d499(a,b))%10
def f_3e4f2e8(a,b,c,d,e,f):
    return (a+b*c+d-e*f+f_53cefd9(a,b)+f_2d0b4c9(a,b,c,d,e,f,515,653,89)+f_33f699e(a,b,c,d,e,f,388,459,37,698))%10
def f_59eeab6(a):
    return (a+f_4fe1fea(a,959,517,4,985,962,508)+f_312a318(a,113,93,510,798,830))%10
def f_43ac9b9(a,b,c):
    return (a*b-c+f_28cda19(a,b,c,693,977,425,549)+f_5c62d79(a,b,c,744,101,164)+f_25c5319(a,b,c,265,219,577,553,258))%10
def f_5216ea8(a,b,c,d,e,f):
    return (a-b+c+d+e-f+f_4ca92a8(a,b,c,d,e,f,963,961,117,413))%10
def f_46db2d0(a,b,c,d,e):
    return (a*b+c*d*e+f_4bae5af(a,b,c,d))%10
def f_59c858a(a,b,c,d,e):
    return (a+b-c+d*e+f_40b6207(a,b,c,d,e,118)+f_108ee0a(a,b,c,d,e,619,345,451))%10
def f_50d0813(a,b,c,d,e):
    return (a*b+c*d+e+f_11b9dd4(a)+f_3901b28(a,b,c,d,e,238,255,521)+f_44bbc00(a,b,c,d,e,915,416,383,780,639))%10
def f_1559a18(a,b,c,d,e):
    return (a*b+c-d*e+f_5b1da69(a,b,c,d,e)+f_1a5d76b(a)+f_58bc2(a,b,c,d))%10
def f_59d499a(a,b,c,d,e,f,g):
    return (a+b-c-d*e+f+g+f_cef9d5(a,b,c,d,e,f)+f_3af46d9(a,b,c,d,e,f,g,679)+f_48876b1(a,b,c,d,e))%10
def f_1d447b0(a,b):
    return (a+b+f_28cda19(a,b,412,193,44,387,739))%10
def f_19e3a85(a,b,c,d):
    return (a+b+c-d+f_516909d(a,b,c,d)+f_365ee7e(a,b,c)+f_108ee0a(a,b,c,d,671,664,675,552))%10
def f_4ec8ff0(a,b,c,d,e):
    return (a*b+c-d+e+f_5b915db(a,b,c,d,e,929)+f_230c9af(a,b))%10
def f_3d8b1a8(a,b,c,d,e,f,g,h):
    return (a-b+c+d-e-f*g*h+f_2e3073c(a,b,c,d,e,f,g,h,768,982)+f_1132978(a)+f_70450f(a,b))%10
def f_e8846d(a,b):
    return (a-b+f_33e0fde(a,b))%10
def f_3a87137(a,b,c,d,e,f,g,h,i):
    return (a-b+c*d+e+f-g-h+i+f_1adec04(a,b,c))%10
def f_268cbef(a,b,c,d,e):
    return (a+b-c*d*e+f_3fc2849(a,b,c,d,e,250))%10
def f_53e38b7(a,b,c,d):
    return (a*b-c-d+f_14d0721(a,b,c,d,391,370,949,555,858)+f_1132978(a))%10
def f_449502b(a,b):
    return (a+b+f_2038f07(a,b,714,997,415,649,943,108,711))%10
def f_5819b03(a,b,c,d,e,f):
    return (a-b-c-d*e*f+f_25adc76(a,b,c)+f_4ef43d8(a)+f_1ede232(a,b,c,d,e,f,165))%10
def f_47407ee(a,b,c,d,e,f,g,h,i):
    return (a-b*c-d*e*f+g-h-i+f_2eab6ae(a,b,c,d,e,f,g,h,i)+f_5deee48(a,b,c,d,e,f,g,h,i)+f_599d433(a,b,c,d,e))%10
def f_49ab0a5(a,b,c,d,e,f,g):
    return (a*b-c*d*e-f-g+f_5eec931(a,b,c)+f_6ad18c(a,b,c)+f_3d5149e(a,b,c,d,e,f,g,508,368,559))%10
def f_29cc20b(a,b):
    return (a+b+f_1bb28ac(a,b)+f_2fb588f(a,b))%10
def f_5cce1d3(a,b,c,d,e,f,g):
    return (a+b*c-d+e*f+g+f_2d2e151(a))%10
def f_2f6bf78(a,b,c,d,e,f,g,h,i):
    return (a*b-c*d+e*f*g+h*i+f_4d12f2a(a,b))%10
def f_2c23742(a,b,c,d):
    return (a+b-c*d+f_3d40505(a)+f_49ccbb5(a))%10
def f_38ac802(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c*d-e+f-g+h*i-j+f_4fe1fea(a,b,c,d,e,f,g))%10
def f_3aabc1d(a,b,c):
    return (a-b*c+f_5e65c19(a,b,c)+f_4ca92a8(a,b,c,761,857,975,543,128,658,541))%10
def f_32749c8(a):
    return (a+f_14d0721(a,663,527,432,944,377,503,394,899)+f_270f3be(a)+f_3ee3b81(a,125,448,441,33,930))%10
def f_27522db(a):
    return (a+f_59eeab6(a))%10
def f_286f9a1(a,b,c,d,e,f,g,h,i):
    return (a*b*c+d*e-f*g*h*i+f_25adc76(a,b,c)+f_477b1bc(a,b,c,d,e,f,g,h,i))%10
def f_5c15e44(a,b,c,d):
    return (a*b-c-d+f_249c03c(a,b,c,d,695,301,950,8,300,296)+f_11b9dd4(a))%10
def f_4d57b30(a,b,c,d,e,f,g,h,i):
    return (a*b+c+d*e+f*g*h*i+f_80b922(a,b,c,d,e,f))%10
def f_def207(a,b):
    return (a*b+f_4dd8575(a,b,726,838,469)+f_3d5149e(a,b,348,842,460,751,853,156,949,282))%10
def f_4911e97(a,b,c,d):
    return (a*b-c+d+f_43b6a1e(a,b,c,d,389,728,869,926)+f_4dfa0c1(a,b,c)+f_80b922(a,b,c,d,137,537))%10
def f_48fc47c(a,b,c,d,e,f,g,h,i,j):
    return (a-b+c+d+e*f-g+h*i+j+f_5d6c325(a,b,c))%10
def f_8effee(a,b,c,d,e,f,g,h):
    return (a+b-c*d-e*f+g*h+f_2898396(a,b,c,d,e,f))%10
def f_78f590(a,b,c,d,e,f,g):
    return (a*b+c*d+e-f*g+f_496990b(a,b,c,d,e))%10
def f_3494e51(a,b,c,d,e,f,g,h,i):
    return (a*b-c+d+e+f-g*h-i+f_3fc2849(a,b,c,d,e,f)+f_50d0813(a,b,c,d,e)+f_52a2bc8(a,b,c,d,e,f,g))%10
def f_2146358(a,b,c):
    return (a+b+c+f_8f7c09(a,b,c,315))%10
def f_380cad4(a,b,c,d,e,f):
    return (a-b*c*d*e-f+f_1d447b0(a,b))%10
def f_3a6b296(a,b,c,d,e,f,g,h,i):
    return (a+b-c*d*e*f+g-h-i+f_59d499a(a,b,c,d,e,f,g)+f_78f590(a,b,c,d,e,f,g)+f_2e3073c(a,b,c,d,e,f,g,h,i,255))%10
def f_33aaf47(a):
    return (a+f_d94d4a(a,110,811)+f_521625(a,428,550)+f_5c56b8b(a,419,786))%10
def f_3a209cc(a,b,c,d,e,f,g,h,i,j):
    return (a*b*c+d+e*f-g-h*i*j+f_521625(a,b,c)+f_5216ea8(a,b,c,d,e,f)+f_32d29e5(a,b,c,d))%10
def f_5dcb737(a,b,c,d):
    return (a+b+c-d+f_323e173(a,b,c,d,138,846,567,337)+f_5db3fab(a,b,c,d,403))%10
def f_39110b3(a,b,c,d,e,f):
    return (a-b-c-d*e*f+f_574b9d(a,b,c,d,e))%10
def f_3915a58(a,b,c,d,e,f,g,h,i):
    return (a-b+c-d+e-f*g+h*i+f_43ac9b9(a,b,c))%10
def f_1212a7(a,b):
    return (a-b+f_58bc2(a,b,797,55))%10
def f_4b06b82(a,b,c,d,e,f,g,h,i,j):
    return (a-b-c*d-e+f+g*h+i-j+f_43b5b8c(a,b,c,d,e,f,g))%10
def f_20d3ec1(a,b,c,d,e,f,g,h):
    return (a-b-c-d*e+f+g+h+f_154f682(a,b,c,d,e,f,g)+f_599d433(a,b,c,d,e)+f_43b5b8c(a,b,c,d,e,f,g))%10
def f_2945031(a,b,c,d,e,f,g,h):
    return (a*b+c*d-e*f*g*h+f_27e5639(a,b,c,d,e,f,g)+f_521625(a,b,c))%10
def f_5c8b8b3(a,b,c,d,e,f,g,h,i):
    return (a-b*c-d-e+f*g+h-i+f_48876b1(a,b,c,d,e)+f_60d002(a,b,c)+f_5410c1d(a,b,c))%10
def f_1b6b84c(a,b,c,d,e,f,g,h):
    return (a+b*c*d*e+f+g*h+f_11948c1(a,b,c,d,e,f,g,h,761,795)+f_2e9d3eb(a,b))%10
def f_301dbdd(a,b,c,d,e,f,g,h,i,j):
    return (a*b-c*d-e+f+g+h-i-j+f_28a147f(a,b,c,d)+f_f79bd0(a,b,c,d,e,f,g,h,i,j)+f_def207(a,b))%10
def f_26d1473(a,b,c,d,e,f,g):
    return (a-b*c+d+e+f-g+f_43ac9b9(a,b,c)+f_5b1da69(a,b,c,d,e))%10
def f_2966db4(a):
    return (a+f_e17983(a,366)+f_1ede232(a,532,161,751,651,769,645))%10
def f_2a29cf2(a,b,c,d,e,f,g,h,i):
    return (a-b+c-d+e+f+g-h+i+f_313e9b5(a,b,c,d))%10
def f_2807d02(a,b,c,d,e,f,g,h,i,j):
    return (a*b*c+d+e-f-g+h+i+j+f_32d29e5(a,b,c,d)+f_496990b(a,b,c,d,e))%10
def f_16821c0(a,b,c,d,e,f,g):
    return (a-b-c-d-e+f-g+f_5b1da69(a,b,c,d,e))%10
def f_39feb9a(a,b,c,d,e,f,g,h):
    return (a-b+c-d*e-f+g*h+f_3ce64d4(a,b)+f_496990b(a,b,c,d,e))%10
def f_534da71(a,b,c):
    return (a-b-c+f_43ac9b9(a,b,c))%10
def f_25002b2(a):
    return (a+f_5dcb737(a,696,409,514)+f_b8a492(a,235,860,444,821,355,697,786,568))%10

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

import matplotlib.pyplot as plt
rate = [0.7313719583441618,
        0.5998101539379961,
        0.5112029167634624,
        0.4471136711913082,
        0.4012879752441838,
        0.3674706975981095,
        0.34164846217106964,
        0.32093635331496456,
        0.3045361076318255,
        0.29053754560889644,
        0.2782595927753716,
        0.26770569586440274,
        0.2585863292912345,
        0.2499233101873713,
        0.24246595834002574,
        0.23565383493870676,
        0.22932149679212546,
        0.22332762784105598,
        0.2178431860498301,
        0.2127564972643279,
        0.20810547554921968,
        0.20379430172288404,
        0.1996795916862039,
        0.19578822995776374,
        0.19224981370407315,
        0.18871346549027365,
        0.18548594456688006,
        0.18236596171782424,
        0.17929561182615505,
        0.17650168993326434,
        0.1738614923389462,
        0.17121233323843327,
        0.1687079369302981,
        0.16647721123441991,
        0.16427543809701728,
        0.1621019281714598,
        0.15996702165720308,
        0.15786106770142191,
        0.1559115954307348,
        0.154005551997761,
        0.1521670645345635,
        0.1505436532200415,
        0.14884234573628768,
        0.14716654407785756,
        0.14564170933147852,
        0.14419959618074393,
        0.14269406314001526,
        0.14132157399894807,
        0.1398408574369127,
        0.13838426800694034,
        0.13691595968425166,
        0.13560551173991778,
        0.13441776749578982,
        0.13312524256384556,
        0.13190854576124203,
        0.13073596714298222,
        0.12955787375167943,
        0.12849145451449662,
        0.12732163328275828,
        0.12621178520786214,
        0.1251743185291549,
        0.12405757698795504,
        0.12311799753076037,
        0.12222874037758272,
        0.12128295680071471,
        0.12047090647013854,
        0.11947273254936239,
        0.11860415579509585,
        0.11772799622789523,
        0.11684494319439093,
        0.11599428945251401,
        0.11519740474780599,
        0.11430125412832463,
        0.11353401132872253,
        0.11283708188541818,
        0.11203123567451534,
        0.11132810211153767,
        0.1106201431221474,
        0.10991218413275713,
        0.10927936392607722,
        0.108547277804624,
        0.10787516484001299,
        0.10721752815463975,
        0.10653507499057319,
        0.10588019569172143,
        0.10517292604896153,
        0.1045938748794505,
        0.10401689174983059,
        0.10340957736847439,
        0.10279674821407522,
        0.10222252247097678,
        0.10165587954081243,
        0.10113266544836139,
        0.10055637166537185,
        0.10001109848074896,
        0.09948443765514607,
        0.09898190396160615,
        0.09848143830795733,
        0.0979003190985552,
        0.09740674691121008
        ]
error = [0.05053043752256264,
         0.18680599668000358,
         0.36043010567594724,
         0.5545290888289391,
         0.7472100087781384,
         0.9261148644228712,
         1.0992254085737152,
         1.2683877329235105,
         1.4286177560987914,
         1.5860048197907959,
         1.7396271280494904,
         1.8848911235520922,
         2.0285990525940276,
         2.1804844161835732,
         2.317136493930554,
         2.464831160343755,
         2.610039696960143,
         2.7663653813060582,
         2.903286444729266,
         3.056784938789378,
         3.1874255423840023,
         3.3248805004598125,
         3.471457069495475,
         3.619548388083834,
         3.7574791190238446,
         3.903092963439339,
         4.041361164528974,
         4.171639573007469,
         4.328559168062989,
         4.4690950904860225,
         4.606527058671074,
         4.750271417208214,
         4.889963105838829,
         5.018944372910213,
         5.156381175691669,
         5.297409765162614,
         5.458478356010017,
         5.608192628622645,
         5.75265243426323,
         5.891025016322313,
         6.026863078418933,
         6.160156663094904,
         6.295151655211852,
         6.438289086098313,
         6.571541791664376,
         6.708379031520173,
         6.838051551575766,
         6.975349829776208,
         7.139801696479817,
         7.284051368579266,
         7.446200706995996,
         7.592159774773273,
         7.72405403196909,
         7.866826045905304,
         8.018711176660236,
         8.172777709125157,
         8.315649991925063,
         8.43905428347039,
         8.604204922850002,
         8.739583236249901,
         8.886752265748353,
         9.062943351040525,
         9.21020909280907,
         9.360104104175317,
         9.50843953633668,
         9.636583032503744,
         9.799632984748843,
         9.946633414272206,
         10.0989459848642,
         10.251135943953198,
         10.39991980217001,
         10.532988170376475,
         10.710220886341554,
         10.849482896552928,
         10.978140699303287,
         11.148442272954265,
         11.287148807916301,
         11.436947946245699,
         11.582447817723502,
         11.71037195435074,
         11.865941694728141,
         12.019833075349057,
         12.158599832705063,
         12.313132541524276,
         12.467678842570473,
         12.636325669813589,
         12.779470485249657,
         12.933750010704447,
         13.085420374161657,
         13.225642426349266,
         13.362018323612794,
         13.514427586049758,
         13.64588008792851,
         13.796512018657772,
         13.941360272410455,
         14.091461325240179,
         14.221381051478243,
         14.353311627996222,
         14.512423436158123,
         14.670772892173172
         ]
d=list(range(1,101))
fig=plt.figure(1)
ax1=plt.subplot(1,2,1)
plt.plot(d,rate,color='b')
plt.xlabel('Dmax/m')
plt.ylabel('compression rate')
ax1=plt.subplot(1,2,2)


plt.plot(d,error,color='b')
plt.xlabel('Dmax/m')
plt.ylabel('mean error/m')
plt.show()
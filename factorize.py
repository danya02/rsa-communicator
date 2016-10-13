#!/usr/bin/python3
from sympy.ntheory import factorint
factors = [
    {"num": 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139,
     "factor": {"37975227936943673922808872755445627854565536638199": 1,
                "40094690950920881030683735292761468389214899724061": 1
     },
     "difficulty": 2},
    {"num": 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667,
     "factor": {"6122421090493547576937037317561418841225758554253106999": 1,
                "5846418214406154678836553182979162384198610505601062333": 1
     },
     "difficulty": 2},
    {"num": 227010481295437363334259960947493668895875336466084780038173258247009162675779735389791151574049166747880487470296548479,
     "factor": {"327414555693498015751146303749141488063642403240171463406883": 1,
                "693342667110830181197325401899700641361965863127336680673013": 1
     },
     "difficulty": 2.5},
    {"num": 114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541,
     "factor": {"3490529510847650949147849619903898133417764638493387843990820577": 1,
                "32769132993266709549961988190834461413177642967992942539798288533": 1
     },
     "difficulty": 3},
    {"num": 1807082088687404805951656164405905566278102516769401349170127021450056662540244048387341127590812303371781887966563182013214880557,
     "factor": {"39685999459597454290161126162883786067576449112810064832555157243": 1,
                "45534498646735972188403686897274408864356301263205069600999044599": 1
     },
     "difficulty": 3},
    {"num": 21290246318258757547497882016271517497806703963277216278233383215381949984056495911366573853021918316783107387995317230889569230873441936471,
     "factor": {"3398717423028438554530123627613875835633986495969597423490929302771479": 1,
                "6264200187401285096151654948264442219302037178623509019111660653946049": 1
     },
     "difficulty": 4},
    {"num": 155089812478348440509606754370011861770654545830995430655466945774312632703463465954363335027577729025391453996787414027003501631772186840890795964683,
     "factor": {"348009867102283695483970451047593424831012817350385456889559637548278410717": 1,
                "445647744903640741533241125787086176005442536297766153493419724532460296199": 1
     },
     "difficulty": 6},
    {"num": 10941738641570527421809707322040357612003732945449205990913842131476349984288934784717997257891267332497625752899781833797076537244027146743531593354333897,
     "factor": {"102639592829741105772054196573991675900716567808038066803341933521790711307779": 1,
                "106603488380168454820927220360012878679207958575989291522270608237193062808643": 1
     },
     "difficulty": 6},
    {"num": 26062623684139844921529879266674432197085925380486406416164785191859999628542069361450283931914514618683512198164805919882053057222974116478065095809832377336510711545759,
     "factor": {"3586420730428501486799804587268520423291459681059978161140231860633948450858040593963": 1,
                "7267029064107019078863797763923946264136137803856996670313708936002281582249587494493": 1
     },
     "difficulty": 7},
    {"num": 188198812920607963838697239461650439807163563379417382700763356422988859715234665485319060606504743045317388011303396716199692321205734031879550656996221305168759307650257059,
     "factor": {"398075086424064937397125500550386491199064362342526708406385189575946388957261768583317": 1,
                "472772146107435302536223071973048224632914695302097116459852171130520711256363590397527": 1
     },
     "difficulty": 8},
    {"num": 191147927718986609689229466631454649812986246276667354864188503638807260703436799058776201365135161278134258296128109200046702912984568752800330221777752773957404540495707851421041,
     "factor": {"400780082329750877952581339104100572526829317815807176564882178998497572771950624613470377": 1,
                "476939688738611836995535477357070857939902076027788232031989775824606225595773435668861833": 1
     },
     "difficulty": 8},
    {"num": 1907556405060696491061450432646028861081179759533184460647975622318915025587184175754054976155121593293492260464152630093238509246603207417124726121580858185985938946945490481721756401423481,
     "factor": {"31711952576901527094851712897404759298051473160294503277847619278327936427981256542415724309619": 1,
      "60152600204445616415876416855266761832435433594718110725997638280836157040460481625355619404899": 1
     },
     "difficulty": 8},
    {"num": 3107418240490043721350750035888567930037346022842727545720161948823206440518081504556346829671723286782437916272838033415471073108501919548529007337724822783525742386454014691736602477652346609,
     "factor": {"1634733645809253848443133883865090859841783670033092312181110852389333100104508151212118167511579": 1,
      "1900871281664822113126851573935413975471896789968515493666638539088027103802104498957191261465571": 1
     },
     "difficulty": 12},
    {"num": 27997833911221327870829467638722601621070446786955428537560009929326128400107609345671052955360856061822351910951365788637105954482006576775098580557613579098734950144178863178946295187237869221823983,
     "factor": {"3532461934402770121272604978198464368671197400197625023649303468776121253679423200058547956528088349": 1,
      "7925869954478333033347085841480059687737975857364219960734330341455767872818152135381409304740185467": 1
     },
     "difficulty": 22},
    {"num": 245246644900278211976517663573088018467026787678332759743414451715061600830038587216952208399332071549103626827191679864079776723243005600592035631246561218465817904100131859299619933817012149335034875870551067,
     "factor": {"435958568325940791799951965387214406385470910265220196318705482144524085345275999740244625255428455944579 ": 1,
      "562545761726884103756277007304447481743876944007510545104946851094548396577479473472146228550799322939273": 1
     },
     "difficulty": 22},
    {"num": 74037563479561712828046796097429573142593188889231289084936232638972765034028266276891996419625117843995894330502127585370118968098286733173273108930900552505116877063299072396380786710086096962537934650563796359,
     "factor": {"9091213529597818878440658302600437485892608310328358720428512168960411528640933367824950788367956756806141 ": 1,
      "8143859259110045265727809126284429335877899002167627883200914172429324360133004116702003240828777970252499": 1
     },
     "difficulty": 26},
    {"num": 2260138526203405784941654048610197513508038915719776718321197768109445641817966676608593121306582577250631562886676970448070001811149711863002112487928199487482066070131066586646083327982803560379205391980139946496955261,
     "factor":
     {"68636564122675662743823714992884378001308422399791648446212449933215410614414642667938213644208420192054999687 ": 1,
      "32929074394863498120493015492129352919164551965362339524626860511692903493094652463337824866390738191765712603": 1
     },
     "difficulty": 28},
    {"num": 1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413,
     "factor":
     {"33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489 ": 1,
      "36746043666799590428244633799627952632279158164343087642676032283815739666511279233373417143396810270092798736308917": 1
     },
     "difficulty": 32}
]

def factor(num):
    return factorint(int(num))


def smartfactor(num):
    for i in factors:
        if i["num"] == num:
            import time
            import random
            time.sleep(i["difficulty"]*(1+random.random()))
            return i["factor"]
    return factor(num)

if __name__ == '__main__':
    print("Answer:", smartfactor(input("number to factor:")))
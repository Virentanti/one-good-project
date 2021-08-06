#import os
from screenshot import ssw

chapter_lst=['Physics Electrostatics & Capacitance','Current Electricity, Charging & Discharging Of Capacitors']
#types=[['Assertion and Reason', 'Critical Thinking','Grouping of Capacitors','Capacitance','Electric Flux and Gausss Law','Electric Dipole','Electric Field and Potential','Charge and Coulombs Law','Electric Charges and Field Conceptual Problems'],['Assertion and Reason', 'Critical Thinking','Thermo Electricity','Chemical Effect of Current','Heating Effect of Current','Assertion and Reason', 'Critical Thinking','Different Measuring Instruments',"Kirchhoff's Law, Cells",'Grouping of Resistances',"Electric Conduction, Ohm's and Resistance",'Different Measuring Instruments','Kirchhoffs Law Cells','Grouping of Resistances','Electric Conduction Ohms and Resistance']]

#dat={'Assertion_and_Reason':['https://www.studyadda.com/question-bank/assertion-and-reason_q1/1162/84237',21],'Critical Thinking':['https://www.studyadda.com/question-bank/critical-thinking_q1/1160/84183',45],'Thermo Electricity':['https://www.studyadda.com/question-bank/thermo-electricity_q1/1159/84139',44],'Chemical Effect of Current':['https://www.studyadda.com/question-bank/chemical-effect-of-current_q1/1158/84080',59],'Heating Effect of Current':['https://www.studyadda.com/question-bank/heating-effect-of-current_q1/1157/83927',153],'Assertion and Reason_2':['https://www.studyadda.com/question-bank/assertion-and-reason_q1/1068/77282',17],'Critical Thinking_2':['https://www.studyadda.com/question-bank/critical-thinking_q1/1066/77208',54],'Different Measuring Instruments':['https://www.studyadda.com/question-bank/different-measuring-instruments_q1/1065/77065',143],'Kirchhoff Law, Cells':['https://www.studyadda.com/question-bank/kirchhoffs-law-cells_q1/1064/76980',85],'Grouping of Resistances':['https://www.studyadda.com/question-bank/grouping-of-resistances_q1/1063/76839',141],'Electric Conduction & Ohm and Resistance':['https://www.studyadda.com/question-bank/electric-conduction-ohms-and-resistance_q1/1062/76706',133],'Different Measuring Instruments_2':['https://www.studyadda.com/question-bank/different-measuring-instruments_q1/1051/75677',143],'Kirchhoffs Law Cells':['https://www.studyadda.com/question-bank/kirchhoffs-law-cells_q1/1050/75592',85],'Grouping of Resistances':['https://www.studyadda.com/question-bank/grouping-of-resistances_q1/1049/75451',141],'Electric Conduction Ohms and Resistance':['https://www.studyadda.com/question-bank/electric-conduction-ohms-and-resistance_q1/1048/75318',133]}
dat={'Different Measuring Instruments_2':['https://www.studyadda.com/question-bank/different-measuring-instruments_q1/1051/75677',143],'Kirchhoffs Law Cells':['https://www.studyadda.com/question-bank/kirchhoffs-law-cells_q1/1050/75592',85],'Grouping of Resistances':['https://www.studyadda.com/question-bank/grouping-of-resistances_q1/1049/75451',141]}
type=list(dat.keys())
#os.mkdir(path)
for j in type:
    ssw(dat[j][0],j,dat[j][1])
    

# https://www.studyadda.com/question-bank/assertion-and-reason_q1/1162/84237
# https://www.studyadda.com/question-bank/jee-main-advanced/28/physics/1
# https://www.studyadda.com/question-bank/numerical-value-type-questions-current-electricity_q1/5841/432012
# https://www.studyadda.com/question-bank/chemical-effect-of-current_q2/1158/84082




dat_phull={" Mathematical Tools, Units & Dimensions Question Bank Self Evaluation Test":["https://www.studyadda.com/question-bank/self-evaluation-test-physical-world-units-and-measurements_q1/5959132/436043",100],
           "Mathematical Tools, Units & Dimensions Question Bank Numerical Value type Questions - Physical World, Units & Measurement":["https://www.studyadda.com/question-bank/numerical-value-type-questions-physical-world-units-measurement_q1/5825/431770",15],
           "Mathematical Tools, Units & Dimensions Question Bank Numerical Value Type Questions - Practical Physics":["https://www.studyadda.com/question-bank/numerical-value-type-questions-practical-physics_q1/5731/430241",15],
           "Mathematical Tools, Units & Dimensions Question Bank Numerical Value Type Questions - Unit and Dimension":["https://www.studyadda.com/question-bank/numerical-value-type-questions-unit-and-dimension_q1/5689/429661",7],
           "Mathematical Tools, Units & Dimensions Question Bank Mock Test - Units Dimenstions and Measurment":["https://www.studyadda.com/question-bank/mock-test-units-dimenstions-and-measurment_q1/5203/420015",25],
          'Mathematical Tools, Units & Dimensions Question Bank Assertion and Reasons':['https://www.studyadda.com/question-bank/assertion-and-reasons_q1/942/68755',25],
           'Mathematical Tools, Units & Dimensions Question Bank Critical Thinking':['https://www.studyadda.com/question-bank/critical-thinking_q1/941/68740',15],
           'Mathematical Tools, Units & Dimensions Question Bank Errors of Measurement':['https://www.studyadda.com/question-bank/errors-of-measurement_q1/940/68712',28],
           ' Mathematical Tools, Units & Dimensions Question Bank Dimensions':['https://www.studyadda.com/question-bank/dimensions_q1/939/68570',142],
           'Mathematical Tools, Units & Dimensions Question Bank Units':['https://www.studyadda.com/question-bank/units_q1/938/68461',109],
           'Mathematical Tools, Units & Dimensions Question Bank Units2':['https://www.studyadda.com/question-bank/units_q1/182/23811',109],
           'Motion in a Straight Line Topic Test - One Dimensional Motion':['https://www.studyadda.com/question-bank/topic-test-one-dimensional-motion_q1/5959207/483935',35],
           'Motion in a Straight Line Numerical Value Type Questions - Motion in a Plane':['https://www.studyadda.com/question-bank/numerical-value-type-questions-motion-in-a-plane_q1/5827/431800',15],
           'Motion in a Straight Line Numerical Value type Questions - Motion in a Straight Line':['https://www.studyadda.com/question-bank/numerical-value-type-questions-motion-in-a-straight-line_q1/5826/431785',15],
           'Motion in a Straight Line Numerical Value Type Questions - Motion in One Dimension':['https://www.studyadda.com/question-bank/numerical-value-type-questions-motion-in-one-dimension_q1/5690/429668',14],
           'Motion in a Straight Line Mock Test - Motion in one Dimension':['https://www.studyadda.com/question-bank/mock-test-motion-in-one-dimension_q1/5206/420090',25],
           'Motion in a Straight Line Self Evaluation Test - Motion in a Strainght Line':['https://www.studyadda.com/question-bank/self-evaluation-test-motion-in-a-strainght-line_q1/5183/414958',100],
           'Motion in a Straight Line Assertion and Reason':['https://www.studyadda.com/question-bank/assertion-and-reason_q1/950/69031',30],
           'Motion in a Straight Line Graphical Questions':['https://www.studyadda.com/question-bank/graphical-questions_q1/949/69001',30],
           'Motion in a Straight Line Critical Thinking Questions':['https://www.studyadda.com/question-bank/critical-thinking-questions_q1/948/68989',12],
           'Motion in a Straight Line Motion Under Gravity':['https://www.studyadda.com/question-bank/motion-under-gravity_q1/947/68908',81],
           'Motion in a Straight Line Relative Motion':['https://www.studyadda.com/question-bank/relative-motion_q1/946/68895',13],
           'Motion in a Straight Line Non-uniform Motion':['https://www.studyadda.com/question-bank/non-uniform-motion_q1/945/68810',85],
           'Motion in a Straight Line Uniform Motion':['https://www.studyadda.com/question-bank/uniform-motion_q1/944/68786',24],
           'Motion in a Straight Line Distance and Displacement':['https://www.studyadda.com/question-bank/distance-and-displacement_q1/943/68780',6],
           'Vectors Question Bank Topic Test - Vectors':['https://www.studyadda.com/question-bank/topic-test-vectors_q1/5959210/485580',35],
           'Vectors Question Bank Numerical Value Type Questions - Essential Mathematics and Vector':['https://www.studyadda.com/question-bank/numerical-value-type-questions-essential-mathematics-and-vector_q1/5720/430105',14],
           'Vectors Question Bank Assertion and Reason':['https://www.studyadda.com/question-bank/assertion-and-reason_q1/1018/71823',22],
           'Vectors Question Bank Critical Thinking':['https://www.studyadda.com/question-bank/critical-thinking_q1/1017/71809',14],
           'Vectors Question Bank Relative Velocity':['https://www.studyadda.com/question-bank/relative-velocity_q1/1016/71795',14],
           'Vectors Question Bank Lamis Theorem':['https://www.studyadda.com/question-bank/lamis-theorem_q1/1015/71790',5],
           'Vectors Question Bank Multiplication of Vectors':['https://www.studyadda.com/question-bank/multiplication-of-vectors_q1/1014/71731',59],
           'Vectors Question Bank Addition and Subtraction of Vectors':['https://www.studyadda.com/question-bank/addition-and-subtraction-of-vectors_q1/1013/71678',53],
           'Vectors Question Bank Fundamentals of Vectors':['https://www.studyadda.com/question-bank/fundamentals-of-vectors_q1/1012/71644',34],
           'Two Dimensional Motion Question Bank Topic Test - Two Dimensional Motion':['https://www.studyadda.com/question-bank/topic-test-two-dimensional-motion_q1/5959211/486985',35],
           'Two Dimensional Motion Question Bank Numerical Value Type Questions - Projectile Motion':['https://www.studyadda.com/question-bank/numerical-value-type-questions-projectile-motion_q1/5721/430119',15],
           'Two Dimensional Motion Question Bank Mock Test - Motion in Two Dimension':['https://www.studyadda.com/question-bank/mock-test-motion-in-two-dimension_q1/5209/420165',25],
           'Two Dimensional Motion Question Bank Self Evaluation Test - Motion in a Plane':['https://www.studyadda.com/question-bank/self-evaluation-test-motion-in-a-plane_q1/5195/415727',100],
           'Two Dimensional Motion Question Bank Assertion and Reason':['https://www.studyadda.com/question-bank/assertion-and-reason_q1/956/69323',26],
           'Two Dimensional Motion Question Bank Critical Thinking':['https://www.studyadda.com/question-bank/critical-thinking_q1/955/69306',17],
           'Two Dimensional Motion Question Bank Horizontal Projectile Motion':['https://www.studyadda.com/question-bank/horizontal-projectile-motion_q1/953/69231',16],
           'Two Dimensional Motion Question Bank Non-uniform Circular Motion':['https://www.studyadda.com/question-bank/non-uniform-circular-motion_q1/952/69183',48],
           'Two Dimensional Motion Question Bank Uniform Circular Motion':['https://www.studyadda.com/question-bank/uniform-circular-motion_q1/951/69061',122],
           'NLM, Friction, Circular Motion Question Bank Topic Test - Friction':['https://www.studyadda.com/question-bank/topic-test-friction_q1/5959260/493908',35],
           'NLM, Friction, Circular Motion Question Bank Topic Test - Newton Laws Of Motion':['https://www.studyadda.com/question-bank/topic-test-newtons-laws-of-motion_q1/5959259/493434',35],
           'NLM, Friction, Circular Motion Question Bank Self Evaluation Test - Laws of Motion':['https://www.studyadda.com/question-bank/self-evaluation-test-laws-of-motion_q1/5959133/436143',100],
           'NLM, Friction, Circular Motion Question Bank Numerical Value Type Questions - Laws of Motion':['https://www.studyadda.com/question-bank/numerical-value-type-questions-laws-of-motion_q1/5828/431815',15],
           'NLM, Friction, Circular Motion Question Bank Numerical Value Type Questions - Circular Motion':['https://www.studyadda.com/question-bank/numerical-value-type-questions-circular-motion_q1/5693/429712',16],
           'NLM, Friction, Circular Motion Question Bank Numerical Value Type Questions - Friction':['https://www.studyadda.com/question-bank/numerical-value-type-questions-friction_q1/5692/429697',15],
           'NLM, Friction, Circular Motion Question Bank Numerical Value Type Questions - Laws of Motion':['https://www.studyadda.com/question-bank/numerical-value-type-questions-laws-of-motion_q1/5691/429682',15],
           'NLM, Friction, Circular Motion Question Bank Mock Test - Newtons Laws of Motion With Friction':['https://www.studyadda.com/question-bank/mock-test-newtons-laws-of-motion-with-friction_q1/5215/420315',25],
           'NLM, Friction, Circular Motion Question Bank Mock Test - Newtons Laws of Motion without Friction':['https://www.studyadda.com/question-bank/mock-test-newtons-laws-of-motion-without-friction_q1/5210/420190',25],
           'NLM, Friction, Circular Motion Question Bank Assertion and Reason':['https://www.studyadda.com/question-bank/assertion-and-reason_q1/970/69724',8],
           'NLM, Friction, Circular Motion Question Bank Critical Thinking Questions':['https://www.studyadda.com/question-bank/critical-thinking-questions_q1/969/69713',11],
           'NLM, Friction, Circular Motion Question Bank Motion on Inclined Surface':['https://www.studyadda.com/question-bank/motion-on-inclined-surface_q1/968/69689',24],
           'NLM, Friction, Circular Motion Question Bank Kinetic Friction':['https://www.studyadda.com/question-bank/kinetic-friction_q1/967/69653',36],
           'NLM, Friction, Circular Motion Question Bank Static and Limiting Friction':['https://www.studyadda.com/question-bank/static-and-limiting-friction_q1/966/69621',32],
           'NLM, Friction, Circular Motion Question Bank Assertion and Reason2':['https://www.studyadda.com/question-bank/assertion-and-reason_q1/965/69596',25],
           'NLM, Friction, Circular Motion Question Bank graphical question':['https://www.studyadda.com/question-bank/graphical-questions_q1/964/69585',11],
           'NLM, Friction, Circular Motion Question Bank Critical Thinking Questions2':['https://www.studyadda.com/question-bank/critical-thinking-questions_q1/963/69566',19],
           'NLM, Friction, Circular Motion Question Bank Motion of Connected Bodies':['https://www.studyadda.com/question-bank/motion-of-connected-bodies_q1/962/69543',23],
           'NLM, Friction, Circular Motion Question Bank Equilibrium of Forces':['https://www.studyadda.com/question-bank/equilibrium-of-forces_q1/961/69525',18],
           'NLM, Friction, Circular Motion Question Bank Conservation of Linear Momentum and Impulse':['https://www.studyadda.com/question-bank/conservation-of-linear-momentum-and-impulse_q1/960/69498',27],
           'NLM, Friction, Circular Motion Question Bank Third Law of Motion':['https://www.studyadda.com/question-bank/third-law-of-motion_q1/959/69474',24],
           'NLM, Friction, Circular Motion Question Bank Second Law of Motion':['https://www.studyadda.com/question-bank/second-law-of-motion_q1/958/69361',113],
           'NLM, Friction, Circular Motion Question Bank First law of motion':['https://www.studyadda.com/question-bank/first-law-of-motion_q1/957/69349',12]

          }
           
doodad2={'Electrostatics & Capacitance Question Bank Self Evaluation Test - Electrostatic Potential and Capacitance':['https://www.studyadda.com/question-bank/self-evaluation-test-electrostatic-potential-and-capacitance_q1/5959145/437288',100],'Electrostatics & Capacitance Question Bank Self Evaluation Test - Electric Chages and Fields':['https://www.studyadda.com/question-bank/self-evaluation-test-electric-chages-and-fields_q1/5959144/437188',100],' Electrostatics & Capacitance Question Bank Numerical Value Type Questions - Electrostatic Potential and Capacitance':['https://www.studyadda.com/question-bank/numerical-value-type-questions-electrostatic-potential-and-capacitance_q1/5840/431995',15],'Electrostatics & Capacitance Question Bank Numerical Value Type Questions - Electric Charges and Fields':['https://www.studyadda.com/question-bank/numerical-value-type-questions-electric-charges-and-fields_q1/5839/431980',15],"Electrostatics & Capacitance Question Bank Numerical Value Type Questions - Gauss's Law":['https://www.studyadda.com/question-bank/numerical-value-type-questions-gausss-law_q1/5723/430149',8],'Electrostatics & Capacitance Question Bank Numerical Value type Questions - Capacitance':['https://www.studyadda.com/question-bank/numerical-value-type-questions-capacitance_q1/5706/429903',15],'Electrostatics & Capacitance Question Bank Numerical Value Type Questions - Electrostatics':['https://www.studyadda.com/question-bank/numerical-value-type-questions-electrostatics_q1/5705/429887',16],'Electrostatics & Capacitance Question Bank Numerical Value Type Questions - Electrostatics':['https://www.studyadda.com/question-bank/numerical-value-type-questions-electrostatics_q1/5705/429887',16],' Electrostatics & Capacitance Question Bank Mock Test - Capacitance':['https://www.studyadda.com/question-bank/mock-test-capacitance_q1/5299/426152',25],'Electrostatics & Capacitance Question Bank Mock Test - Electrostatics':['https://www.studyadda.com/question-bank/mock-test-electrostatics_q1/5298/426127',25],'Electrostatics & Capacitance Question Bank Assertion and Reason':['https://www.studyadda.com/question-bank/assertion-and-reason_q1/1011/71614',30],'Electrostatics & Capacitance Question Bank Graphical Questions':['https://www.studyadda.com/question-bank/graphical-questions_q1/1010/71597',17],'Electrostatics & Capacitance Question Bank Critical Thinking':['https://www.studyadda.com/question-bank/critical-thinking_q1/1009/71530',67],'Electrostatics & Capacitance Question Bank Grouping of Capacitors':['https://www.studyadda.com/question-bank/grouping-of-capacitors_q1/1008/71403',127],'Electrostatics & Capacitance Question Bank Capacitance':['https://www.studyadda.com/question-bank/capacitance_q1/1007/71232',171],' Electrostatics & Capacitance Question Bank Electric Flux and Gausss Law':['https://www.studyadda.com/question-bank/electric-flux-and-gausss-law_q1/1006/71204',28],'Electrostatics & Capacitance Question Bank Electric Dipole':['https://www.studyadda.com/question-bank/electric-dipole_q1/1005/71165',39],'Electrostatics & Capacitance Question Bank Electric Field and Potential':['https://www.studyadda.com/question-bank/electric-field-and-potential_q1/1004/70955',210],'Electrostatics & Capacitance Question Bank Charge and Coulombs Law':['https://www.studyadda.com/question-bank/charge-and-coulombs-law_q1/1003/70883',72]}
doodad3={

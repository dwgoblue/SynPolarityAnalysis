import numpy as np
from collections import OrderedDict
import os, errno, shutil


def fig1b():
    parent_path = r'/home/r04b43015/Download/fig1b-PeakScore'
    group1, group2, group3, group4, group5 = [], [], [], [], []
    
    for mark in ['01', '02']:
        img = np.array(['113RP-{}.mat'.format(mark)])
        group1.append(img)
    
    for mark in ['01', '02', '04', '05', '06', '07', '08']:
        img = np.array(['117RP-{}.mat'.format(mark)])
        group2.append(img)
    
    for mark in ['01', '03', '04', '05', '06', '07', '08', '09',
                 '10', '11', '12', '14', '15', '16']:
        img = np.array(['116RP-{}.mat'.format(mark)])
        group3.append(img)
    
    for mark in ['01', '02', '03', '04', '05', '06', '07']:
        img = np.array(['106RP-{}.mat'.format(mark)])
        group4.append(img)
    
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08', '10']:
        img = np.array(['100RP-{}.mat'.format(mark)])
        group5.append(img)
    
    
    exp = np.array([group1, group2, group3, group4, group5])
    labels = np.array(['J23113', 'J23117', 'J23116', 'J23106', 'J23100'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data


def figS1():
    parent_path = r'/home/r04b43015/Download/figS1-box-intensity'
    img1 = np.array(['J23103-mWasabi-GFP 01.mat'])
    img2 = np.array(['J23103-mWasabi-GFP 02.mat'])
    img3 = np.array(['J23103-mWasabi-GFP 03.mat'])
    img4 = np.array(['J23103-mWasabi-GFP 04.mat'])
    img5 = np.array(['J23103-mWasabi-GFP 05.mat'])
    img6 = np.array(['J23103-mWasabi-GFP 06.mat'])
    img7 = np.array(['J23103-mWasabi-GFP 07.mat'])
    img8 = np.array(['J23103-mWasabi-GFP 08.mat'])
    img9 = np.array(['J23103-mWasabi-GFP 09.mat'])
    img10 = np.array(['J23103-mWasabi-GFP 10.mat'])
    group1 = np.array([img1, img2, img3, img4, img5, img6, img7, img8, img9, img10])
    img11 = np.array(['J23113-mWasabi-GFP 01.mat'])
    img12 = np.array(['J23113-mWasabi-GFP 02.mat'])
    img13 = np.array(['J23113-mWasabi-GFP 03.mat'])
    img14 = np.array(['J23113-mWasabi-GFP 04.mat'])
    img15 = np.array(['J23113-mWasabi-GFP 05.mat'])
    img16 = np.array(['J23113-mWasabi-GFP 06.mat'])
    img17 = np.array(['J23113-mWasabi-GFP 07.mat'])
    img18 = np.array(['J23113-mWasabi-GFP 08.mat'])
    group2 = np.array([img11, img12, img14, img15, img16, img17, img18])
    img19 = np.array(['J23117-mWasabi-GFP 01.mat'])
    img20 = np.array(['J23117-mWasabi-GFP 02.mat'])
    img21 = np.array(['J23117-mWasabi-GFP 03.mat'])
    img22 = np.array(['J23117-mWasabi-GFP 04.mat'])
    img23 = np.array(['J23117-mWasabi-GFP 05.mat'])
    img24 = np.array(['J23117-mWasabi-GFP 06.mat'])
    img25 = np.array(['J23117-mWasabi-GFP 07.mat'])
    img26 = np.array(['J23117-mWasabi-GFP 08.mat'])
    img27 = np.array(['J23117-mWasabi-GFP 09.mat'])
    img28 = np.array(['J23117-mWasabi-GFP 10.mat'])
    img29 = np.array(['J23117-mWasabi-GFP 11.mat'])
    group3 = np.array([img19, img20, img21, img22, img23, img24, img25, img26, img27, img28, img29])
    img30 = np.array(['J23116-mWasabi-GFP 01.mat'])
    img31 = np.array(['J23116-mWasabi-GFP 02.mat'])
    img32 = np.array(['J23116-mWasabi-GFP 03.mat'])
    img33 = np.array(['J23116-mWasabi-GFP 04.mat'])
    img34 = np.array(['J23116-mWasabi-GFP 05.mat'])
    img35 = np.array(['J23116-mWasabi-GFP 06.mat'])
    img36 = np.array(['J23116-mWasabi-GFP 07.mat'])
    img37 = np.array(['J23116-mWasabi-GFP 08.mat'])
    img38 = np.array(['J23116-mWasabi-GFP 09.mat'])
    img39 = np.array(['J23116-mWasabi-GFP 10.mat'])
    img40 = np.array(['J23116-mWasabi-GFP 11.mat'])
    group4 = np.array([img30, img31, img32, img33, img34, img35, img36, img37, img38, img39, img40])
    img41 = np.array(['J23105-mWasabi-GFP 01.mat'])
    img42 = np.array(['J23105-mWasabi-GFP 02.mat'])
    img43 = np.array(['J23105-mWasabi-GFP 03.mat'])
    img44 = np.array(['J23105-mWasabi-GFP 04.mat'])
    img45 = np.array(['J23105-mWasabi-GFP 05.mat'])
    img46 = np.array(['J23105-mWasabi-GFP 06.mat'])
    img47 = np.array(['J23105-mWasabi-GFP 07.mat'])
    img48 = np.array(['J23105-mWasabi-GFP 08.mat'])
    img49 = np.array(['J23105-mWasabi-GFP 09.mat'])
    img50 = np.array(['J23105-mWasabi-GFP 10.mat'])
    img51 = np.array(['J23105-mWasabi-GFP 11.mat'])
    group5 = np.array([img41, img42, img43, img44, img45, img46, img47, img48, img49, img50, img51])
    img52 = np.array(['J23100-mWasabi-GFP 01.mat'])
    img53 = np.array(['J23100-mWasabi-GFP 02.mat'])
    img54 = np.array(['J23100-mWasabi-GFP 03.mat'])
    img55 = np.array(['J23100-mWasabi-GFP 04.mat'])
    img56 = np.array(['J23100-mWasabi-GFP 05.mat'])
    img57 = np.array(['J23100-mWasabi-GFP 06.mat'])
    img58 = np.array(['J23100-mWasabi-GFP 07.mat'])
    img59 = np.array(['J23100-mWasabi-GFP 08.mat'])
    img60 = np.array(['J23100-mWasabi-GFP 09.mat'])
    img61 = np.array(['J23100-mWasabi-GFP 10.mat'])
    img62 = np.array(['J23100-mWasabi-GFP 11.mat'])
    group6 = np.array([img52, img53, img54, img55, img57, img58, img59, img60, img61, img62])
    exp = np.array([group2, group3, group4, group5, group6])

    labels = np.array(['J23113', 'J23117', 'J23116', 'J23105', 'J23100'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data


def figS6():
    parent_path = r'/home/r04b43015/Download/figS6-intensity'
    group1 = [np.array(['TwoInOne'])]
    group2 = [np.array(['TwoInOne'])]
    group3 = [np.array(['NP']), np.array(['TwoInOne'])]
    group4 = [np.array(['NP']), np.array(['TwoInOne'])]
    
    for mark in ['1', '2', '3', '4', '5']:
        img = np.array(['NCRPGLVA-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['1', '2', '3', '4', '5']:
        img = np.array(['(N)(C)RPGLVA-{}.mat'.format(mark)])
        group2.append(img)
        
    for mark in ['1', '2', '3', '4', '5', '6', '7']:
        img = np.array(['NCGLVA-{}.mat'.format(mark)])
        group3.append(img)
    
    for mark in ['1', '2', '3', '4', '5']:
        img = np.array(['(N)(C)GLVA-{}.mat'.format(mark)])
        group4.append(img)

    exp = np.array([group3, group4])
    labels = np.array(['NatNC', 'NC'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data


def fig2f():
    parent_path = r'/home/r04b43015/Download/fig2f-pearson'
    group1, group2, group3 = [], [], [np.array(['TwoInOne'])]
    
    for mark in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        img = np.array(['116RPNGS(RFP)-{}.mat'.format(mark),
                        '116RPNGS(GFP)-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']:
        img = np.array(['116_SGC_RFP_{}.mat'.format(mark),
                        '116_SGC_GFP_{}.mat'.format(mark)])
        group2.append(img)
        
    for mark in ['01', '05', '15', '17', '19']:
        img = np.array(['116RP106sfGFP(28c-3)-{}.mat'.format(mark)])
        group3.append(img)

    exp = np.array([group3, group1, group2])
    labels = np.array(['sfGFP', 'NGS', 'SGC'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data



def fig2d():
    parent_path = r'/home/r04b43015/Download/fig2d-intensity'
    group1, group2, group3 = [], [], [np.array(['NP'])]
    for mark in ['1', '2', '3', '4', '5']:
        img = np.array(['116RP-{0}(RFP).mat'.format(mark),
                        '116RP-{0}(YFP).mat'.format(mark)])
        group1.append(img)
    
    for mark in ['1', '2', '3', '4', '5', '6', '7']:
        img = np.array(['117BIFC 116RP-{0}(RFP).mat'.format(mark),
                        '117BIFC 116RP-{0}(YFP).mat'.format(mark)])
        group2.append(img)
        
    for mark in ['1', '2', '3', '4', '5', '6', '7']:
        img = np.array(['117BIFC-{}(RFP).mat'.format(mark),
                        '117BIFC-{}(YFP).mat'.format(mark)])
        group3.append(img)
    
    exp = np.array([group3, group2])
    labels = np.array(['BIFC', 'BIFCRP'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data


def fig2b():
    parent_path = r'/home/r04b43015/Download/fig2b-pearson'
    group1, group2 = [np.array(['TwoInOne'])], [np.array(['TwoInOne'])]
    
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08']:
        img = np.array(['SpmXPopZ-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['01', '02', '03', '04', '05']:
        img = np.array(['116RP106sfGFP(28c-2)-{}.mat'.format(mark)])
        group2.append(img)
    
    exp = np.array([group2, group1])
    labels = np.array(['sfGFP', 'SpmXΔC'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data



def figR2b():
    parent_path = r'/home/r04b43015/Download/NSSCP/1H/'
    group1, group2, group3, group4 = [np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])]
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        img = np.array(['32NSSCP-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['01', '02', '03', '04', '05']:
        img = np.array(['32NSSC-{}.mat'.format(mark)])
        group2.append(img)
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']:
        img = np.array(['NSSCP-{}.mat'.format(mark)])
        group3.append(img)
    
    for mark in ['01', '02', '03', '04', '05', '06', '07']:
        img = np.array(['NSSC-{}.mat'.format(mark)])
        group4.append(img)
    
    
    exp = np.array([group2, group1])#, group3, group4])
    labels = np.array(['NSSC-32', 'NSSCP-32'])#, 'NSSCP', 'NSSC'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data



def fig2i():
    parent_path = r'/home/r04b43015/Download/fig2(i)-intensity'
    group1, group2, group3, group4, group5 = [np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne'])], [np.array(['TwoInOne'])], [np.array(['TwoInOne'])]
        
    for mark in ['04', '05', '09']:
        img = np.array(['NSSCP-pT7sfGFPLVA-(dC)-{}.mat'.format(mark)])
        group4.append(img)
        
    for mark in ['08', '09', '10']:
        img = np.array(['NCP-pT7sfGFPLVA-(no-adaptor)-{}.mat'.format(mark)])
        group5.append(img)
    
    for mark in ['13']:
        img = np.array(['NSSC-pT7GFPLVA-{}.mat'.format(mark)])
        group2.append(img)
        
    for mark in ['05', '06']:
        img = np.array(['NSSCP-pT7sfGFPLVA-(point)-{}.mat'.format(mark)])
        group3.append(img)
    
    for mark in ['10']:
        img = np.array(['NSSCP-pT7sfGFPLVA-{}.mat'.format(mark)])
        group1.append(img)
    
    exp = np.array([group3, group4, group5, group2, group1])
    labels = np.array(['NSSCPG(P)', 'NSSCPG(T)', 'NCPG', 'NSSCG', 'NSSCPG'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data


def fig2j():
    parent_path = r'/home/r04b43015/Download/fig2(i)-intensity'
    group1, group2 = [np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])]
    
    for mark in ['13']:
        img = np.array(['NSSC-pT7GFPLVA-{}.mat'.format(mark)])
        group2.append(img)
    
    for mark in ['10']:
        img = np.array(['NSSCP-pT7sfGFPLVA-{}.mat'.format(mark)])
        group1.append(img)
    
    exp = np.array([group2, group1])
    labels = np.array(['NSSCG', 'NSSCPG'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data



def figS7():
    parent_path = r'/home/r04b43015/Download/figS7-NES-SGC/data'
    group1, group2, group3 = [np.array(['TwoInOne'])], [np.array(['TwoInOne'])], [np.array(['TwoInOne'])]
        
    for mark in ['1', '3', '9', '16', '17', '22']:
        img = np.array(['116RPNESSGC-3hr-{}GFPNEW.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['1', '3', '9', '16', '17', '22']:
        img = np.array(['116RPNESSGC-3hr-({})(BFP).mat'.format(mark)])
        group2.append(img)
    
    for mark in ['02', '03', '04', '05', '06', '10', '11', '13', '14']:
        img = np.array(['116RP106sfGFP(37c-1)-{}.mat'.format(mark)])
        group3.append(img)
    
    exp = np.array([group3, group2, group1])
    labels = np.array(['sfGFP', 'Blue', 'Green'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data


def figR2c():
    parent_path = r'/home/r04b43015/Download/fig3-i'
    group1, group2 = [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne']), np.array(['NP'])]
    
    for mark in ['03', '04', '05', '06', '07', '08', '09']:
        img = np.array(['32NSSC-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08']:
        img = np.array(['NSSC-{}.mat'.format(mark)])
        group2.append(img)
    
    exp = np.array([group2, group1])
    labels = np.array(['NSSC', 'NSSC-32'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data


def Supfig12d():
    parent_path = r'/home/r04b43015/Download/FigS12(d)-LR'
    group1, group2, group3, group4, group5, group6 = [np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne'])],[np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])]
    
    for mark in ['01', '10', '11', '12', '13', '14', '15', '16', '17', '18', '20', '21', '22', '24', '25', '26']:
        img = np.array(['NSSCP-{}.mat'.format(mark)])
        group1.append(img)
    
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08']:
        img = np.array(['NSSC-{}.mat'.format(mark)])
        group2.append(img)
    
    for mark in ['01', '04', '05', '06', '07', '09', '10', '11', '12', '13', '14', '15', '16', '18']:
        img = np.array(['NSCCP_1mM-{}.mat'.format(mark)])
        group3.append(img)
        
    for mark in ['01', '05', '06', '07', '08']:
        img = np.array(['NSCC_1mM-{}.mat'.format(mark)])
        group4.append(img)
        
    for mark in ['18','22', '23']:
        img = np.array(['pTacG116RP-{}.mat'.format(mark)])
        group5.append(img)
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08', '09']:
        img = np.array(['pTacDG-{}.mat'.format(mark)])
        group6.append(img)
    
    exp = np.array([group4, group3])
    labels = np.array(['NSCC', 'NSCCP'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data



def fig3f():
    parent_path = r'/home/r04b43015/Download/Fig3f-LR'
    group1, group2, group3, group4 =[np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne'])],[np.array(['TwoInOne']), np.array(['NP'])]
    
#     for mark in ['04', '05', '06', '07', '08']:
#         img = np.array(['pTacDG(G_1s)-{}.mat'.format(mark)])
#         group4.append(img)
        
    for mark in ['01', '03', '04', '05']:
        img = np.array(['pTacDG-1-{}.mat'.format(mark)])
        group4.append(img)
        
    for mark in ['01', '02', '03', '04', '05']:
        img = np.array(['pNSSC-{}.mat'.format(mark)])
        group2.append(img)
        
#     for mark in ['02', '03', '04', '05']:
#         img = np.array(['pNSSC-{}.mat'.format(mark)])
#         group2.append(img)
    
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']:
        img = np.array(['pNSSCP-{}.mat'.format(mark)])
        group1.append(img)
    
    for mark in ['01', '02', '04', '05', '06', '07', '08', '10', '11', '12', '14', '15', '16']:
        img = np.array(['pBADRPpTacDG(2hr_1hr)-{}.mat'.format(mark)])
        group3.append(img)
#     for mark in ['14', '15', '17', '18', '22', '23']:
#         img = np.array(['pTacG116RP-{}.mat'.format(mark)])
#         group3.append(img)
    
    exp = np.array([group4, group3, group2, group1])
    labels = np.array(['pTacDG', 'pTacDGRP', 'NSSC', 'NSSCP'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data



def fig3g():
    parent_path = r'/home/r04b43015/Download/Fig3(g)-linescan'
    group1, group2 =[np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])]
    
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']:
        img = np.array(['pNSSCP-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['01', '02', '03', '04', '05']:
        img = np.array(['pNSSC-{}.mat'.format(mark)])
        group2.append(img)
    
    exp = np.array([group1, group2])
    labels = np.array(['NSSCP', 'NSSC'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data



def figR1b():
    parent_path = r'/home/r04b43015/Download/figR1c-LR-linescan'
    group1, group2 =[np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])]
    
    for mark in ['08', '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22']:
        img = np.array(['RNA_NSSCP_Ampaav-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['01', '06', '07']:
        img = np.array(['RNA_NSSC_Ampaav-{}.mat'.format(mark)])
        group2.append(img)
    
    exp = np.array([group2, group1])
    labels = np.array(['NSSC', 'NSSCP'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data

def figR1c():
    parent_path = r'/home/r04b43015/Download/figR1c-LR-linescan'
    group1, group2 =[np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])]
    
    for mark in ['08', '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22']:
        img = np.array(['RNA_NSSCP_Ampaav-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['01', '06', '07']:
        img = np.array(['RNA_NSSC_Ampaav-{}.mat'.format(mark)])
        group2.append(img)
    
    exp = np.array([group2, group1])
    labels = np.array(['NSSC', 'NSSCP'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data


def figS11():
    parent_path = r'/home/r04b43015/Download/FigS11-pearson'
    group1, group2 =[np.array(['TwoInOne'])], [np.array(['TwoInOne'])]
    
    for mark in ['01', '02', '03', '04', '05']:
        img = np.array(['116RP106sfGFP(28c-2)-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08']:
        img = np.array(['100CpdR-116RP-{}.mat'.format(mark)])
        group2.append(img)
    
    exp = np.array([group1, group2])
    labels = np.array(['sfGFP', 'CpdR'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data



def figS12e():
    parent_path = r'/home/r04b43015/Download/FigS12(e)-linescan'
    group1, group2 = [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne'])]
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18']:
        img = np.array(['pNSCCP-{}.mat'.format(mark)])
        group2.append(img)
        
    for mark in ['03', '04', '06']:
        img = np.array(['pNSCC-{}.mat'.format(mark)])
        group1.append(img)
    
    exp = np.array([group1, group2])
    labels = np.array(['NSCC', 'NSCCP'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data


def figS12c():
    parent_path = r'/home/r04b43015/Download/Sup_Fig12(c)-Intensity'
    group1, group2 = [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne']), np.array(['NP'])]
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08']:
        img = np.array(['NSSC-{}.mat'.format(mark)])
        group1.append(img)
    
    for mark in ['01', '04', '05', '06', '07', '08']:
        img = np.array(['NSCC_1mM-{}.mat'.format(mark)])
        group2.append(img)
    
    exp = np.array([group1, group2])
    labels = np.array(['NSSC', 'NSCC'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data



def TL_106GA():
    parent_path = r'/home/r04b43015/Download/TimeLapse/106GA'
    group = OrderedDict()
    
    # Get subfolder names.
    exp_folders = os.listdir(parent_path)
    group['Exp'] = {}
    for ID, exp_folder in enumerate(exp_folders): # EXP, CONTROL...
        group['Exp']['{}'.format(ID)] = []
        exp_path = parent_path + r'/{}'.format(exp_folder)
        file_folders = os.listdir(exp_path)
        for file_folder in file_folders: # e.g. sc1-1-2
            Cell_path = exp_path + r'/{}'.format(file_folder)
            if os.path.isfile(Cell_path):
                group['Exp']['{}'.format(ID)].append(file_folder)

    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = group
    
    return Data


def TL_Exp():
    parent_path = r'/home/r04b43015/Download/TimeLapse/Exp'
    group = OrderedDict()
    
    # Get subfolder names.
    exp_folders = os.listdir(parent_path)
    group['Exp'] = {}
    for ID, exp_folder in enumerate(exp_folders): # EXP, CONTROL...
        group['Exp']['{}'.format(ID)] = []
        exp_path = parent_path + r'/{}'.format(exp_folder)
        file_folders = os.listdir(exp_path)
        for file_folder in file_folders: # e.g. sc1-1-2
            Cell_path = exp_path + r'/{}'.format(file_folder)
            if os.path.isfile(Cell_path):
                group['Exp']['{}'.format(ID)].append(file_folder)

    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = group
    
    return Data


def TL_Ctrl():
    parent_path = r'/home/r04b43015/Download/TimeLapse/Ctrl'
    group = OrderedDict()
    
    # Get subfolder names.
    exp_folders = os.listdir(parent_path)
    group['Exp'] = {}
    for ID, exp_folder in enumerate(exp_folders): # EXP, CONTROL...
        group['Exp']['{}'.format(ID)] = []
        exp_path = parent_path + r'/{}'.format(exp_folder)
        file_folders = os.listdir(exp_path)
        for file_folder in file_folders: # e.g. sc1-1-2
            Cell_path = exp_path + r'/{}'.format(file_folder)
            if os.path.isfile(Cell_path):
                group['Exp']['{}'.format(ID)].append(file_folder)

    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = group
    
    return Data



def figR2d():
    parent_path = r'/home/r04b43015/Download/figR2d'
    group1, group2, group3, group4, group5 = [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne'])]
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08', '09']:
        img = np.array(['pTacDG-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08']:
        img = np.array(['NSSC-{}.mat'.format(mark)])
        group2.append(img)
        
    for mark in ['01', '10', '11', '12', '13', '14', '15', '16',
                 '17', '18', '20', '21', '22', '23', '24', '25', '26']:
        img = np.array(['NSSCP-{}.mat'.format(mark)])
        group3.append(img)
    
    for mark in ['03', '04', '05', '06', '07', '08', '09']:
        img = np.array(['32NSSC-{}.mat'.format(mark)])
        group4.append(img)
        
    for mark in ['01', '12', '13', '14', '15', '16',
                 '17', '18', '19', '20', '21', '22', '24', '25', '26']:
        img = np.array(['32NSSCP-{}.mat'.format(mark)])
        group5.append(img)
    
    
    exp = np.array([group5, group4, group3, group2, group1])
    labels = np.array(['NSSCP-32', 'NSSC-32', 'NSSCP', 'NSSC', 'Div'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data



def figR2dv2():
    parent_path = r'/home/r04b43015/Download/figR2dv2'
    group1, group2, group3, group4, group5 = [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne'])], [np.array(['TwoInOne']), np.array(['NP'])], [np.array(['TwoInOne'])]
        
    for mark in ['01', '02', '03', '04', '05', '06', '07', '08', '09']:
        img = np.array(['pTacDG-{}.mat'.format(mark)])
        group1.append(img)
        
    for mark in ['01', '02', '03']:
        img = np.array(['NSSC-{}.mat'.format(mark)])
        group2.append(img)
        
    for mark in ['01', '10', '11', '12', '13', '14', '15', '16',
                 '17', '18', '20', '21', '22', '23', '24', '25', '26']:
        img = np.array(['NSSCP-{}.mat'.format(mark)])
        group3.append(img)
    
    for mark in ['01', '02', '03', '04']:
        img = np.array(['32NSSC-{}.mat'.format(mark)])
        group4.append(img)
        
    for mark in ['01', '11', '12', '13', '14', '16', '17']:
        img = np.array(['32NSSCP-{}.mat'.format(mark)])
        group5.append(img)
    
    
    exp = np.array([group5, group4, group3, group2, group1])
    labels = np.array(['NSSCP-32', 'NSSC-32', 'NSSCP', 'NSSC', 'Div'])
    Data = {}
    Data['parent_path'] = parent_path
    Data['exp'] = exp
    Data['labels'] = labels
    
    return Data

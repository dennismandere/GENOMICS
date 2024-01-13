# This file is used to parse the predictive results from ASAquick and MMseqs2
# Developer: Bi Zhao
# Output file has 
# Column 1: Index
# Column 2: Amino Acid sequence
# Column 3: 10 level conservation, 0 means lowest and 9 means highest
# Column 4: Conservation score
# Column 5: Binary Solvent Accessibility, 1= buried, 0=exposed
# Column 6: Preponsity of solvent accessibility
# run: python format_results.py seqfile asaqPredfile pssmfile outputfile
# numpy-1.19.5 
# pandas-1.4.4 

import numpy as np
import pandas as pd
import os
import sys

ASAquick_threshold = 0.16
mmseq1 = 1.43
mmseq2 = 1.89
mmseq3 = 2.17
mmseq4 = 2.34
mmseq5 = 2.55
mmseq6 = 2.67
mmseq7 = 2.85
mmseq8 = 2.96
mmseq9 = 3.24
mmseq10 = 4.40

#the AA_index used to normalize ASA raw data
max_value = {"A":129,
             "R":274,
             "N":195,
             "D":193,
             "C":167,
             "E":223,
             "Q":225,
             "G":104,
             "H":224,
             "I":197,
             "L":201,
             "K":197,
             "M":224,
             "F":240,
             "P":159,
             "S":155,
             "T":172,
             "W":285,
             "Y":263,
             "V":174}

#the aa_index used to calculate PSSM and obtain the position specific conservation
blosum62_bg = { 'A' : 7.4,
                'R' : 5.2,
                'N' : 4.5,
                'D' : 5.3,
                'C' : 2.5,
                'Q' : 3.4,
                'E' : 5.4,
                'G' : 7.4,
                'H' : 2.6,
                'I' : 6.8,
                'L' : 9.9,
                'K' : 5.8,
                'M' : 2.5,
                'F' : 4.7,
                'P' : 3.9,
                'S' : 5.7,
                'T' : 5.1,
                'W' : 1.3,
                'Y' : 3.2,
                'V' : 7.3  }

bbg_AAs = list(blosum62_bg.keys())
tot = sum(blosum62_bg.values())
blosum62_bg = np.array([blosum62_bg[k] / tot for k in blosum62_bg])

#function to calculate PSSM
def calc_pssm_freq_df(pssm_df):
    df = pssm_df[bbg_AAs]
    freq = np.exp(df) * blosum62_bg
    #freq_sum = np.sum(freq,axis=1)
    return np.array(freq)/np.sum(freq, axis=1)[:,np.newaxis]

def calc_relative_entropy(pssm_df):
    df = calc_pssm_freq_df(pssm_df)
    cons = np.sum(df*np.log(df/blosum62_bg), axis=1)
    return cons

def format_mmseq(filename):
    pssm_df = pd.read_csv(filename, sep="\t", skiprows=1)
    #print (len(pssm_df))
    res = calc_relative_entropy(pssm_df)
    deci = []
    score = []
    for t in res:
        score.append(str("{:.2f}".format(t)))
        if t <= mmseq1:
            deci.append("0")
        elif mmseq1<t<=mmseq2:
            deci.append("1")
        elif mmseq2<t<=mmseq3:
            deci.append("2")
        elif mmseq3<t<=mmseq4:
            deci.append("3")
        elif mmseq4<t<=mmseq5:
            deci.append("4")
        elif mmseq5<t<=mmseq6:
            deci.append("5")
        elif mmseq6<t<=mmseq7:
            deci.append("6")
        elif mmseq7<t<=mmseq8:
            deci.append("7")
        elif mmseq8<t<=mmseq9:
            deci.append("8")
        elif mmseq9<t<=mmseq10:
            deci.append("9")
    return deci, score

def format_ASAquick(filename1,filename2):
    x = open(filename1, "rt")
    a = x.read().split("\n")
    seq = "".join(a[1:]).strip()
    content = np.loadtxt(filename2, dtype="str")
    scores = content[:,2]
    bscores = []
    value = []
    for i in range(len(scores)):
        if seq[i] == "A":
            v = float(i)/max_value["A"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "R":
            v = float(i)/max_value["R"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "N":
            v = float(i)/max_value["N"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "D":
            v = float(i)/max_value["D"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "C":
            v = float(i)/max_value["C"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "E":
            v = float(i)/max_value["E"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "Q":
            v = float(i)/max_value["Q"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "G":
            v = float(i)/max_value["G"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "H":
            v = float(i)/max_value["H"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "I":
            v = float(i)/max_value["I"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "L":
            v = float(i)/max_value["L"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "K":
            v = float(i)/max_value["K"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "M":
            v = float(i)/max_value["M"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "F":
            v = float(i)/max_value["F"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "P":
            v = float(i)/max_value["P"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "S":
            v = float(i)/max_value["S"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "T":
            v = float(i)/max_value["T"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "W":
            v = float(i)/max_value["W"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "Y":
            v = float(i)/max_value["Y"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
        elif seq[i] == "V":
            v = float(i)/max_value["V"]
            if v > 1:
                value.append("1")
            else:
                value.append(str(v))
            if v < ASAquick_threshold:
                bscores.append("1")
            else:
                bscores.append("0")
    return seq, bscores, value

def main():
    seqfile = sys.argv[1]
    asaqPredfile = sys.argv[2]
    pssmfile = sys.argv[3]
    outputfile = sys.argv[4]
    con_deci, con_score = format_mmseq(pssmfile)
    seq, asa_bin, asa_score = format_ASAquick(seqfile,asaqPredfile)
    x = open(outputfile, "wt")
    for i in range(len(con_deci)):
        x.write(str(i+1)+"\t"+seq[i]+"\t"+con_deci[i]+"\t"+con_score[i]+"\t"+asa_bin[i]+"\t"+asa_score[i]+"\n")

main()


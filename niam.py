#!/usr/bin/env python3
# structNIAM.py V1 : PatrickR le 16/12/2022 a Angers
#
# Structure de donnee NIAM
#
#
import sys
import json

if len(sys.argv) < 2:
        print("niam.py fichier_NIAM.json",file=sys.stderr)
        exit(1)
try:
    with open(sys.argv[1]) as jsonfile:
        data = json.load(jsonfile)
except IOError:
    print(f"{sys.argv[0]}: Impossible d'ouvrir le fichier {sys.argv[1]}")
    exit(1)
x = data
print("niam.py V1 : >>>")
print(data)
print(data["entite"])
print(data["relcnx"])
print(data["relation"])
print(data["relation"])
print("niam.py V1 : <<<")
exit(0)
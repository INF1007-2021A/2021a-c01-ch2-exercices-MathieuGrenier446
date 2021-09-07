#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majuscule(mot):
    mots=""
    for i in mot:
        mots+=chr(ord(i)-32)
    return mots

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

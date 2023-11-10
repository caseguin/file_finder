import os
import pandas as pd


def looking_for_file(path, keyword):
    results = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if keyword.lower() in file.lower():
                results.append(os.path.join(root, file))
            else:
                pass

    return results


if __name__ == '__main__':
    path = input('Nom du chemin d\'accès à chercher: ')
    keyword = input('Nom du fichier recherché : ')

    results = looking_for_file(path, keyword)

    if results:
        print('-'*25)
        print('Résultats de la recherche')
        print('-'*25)
        for result in results:
            print(result)
        print('-'*25)
    else : 
        print('Aucun résultats')
        

# main.py

import time
import os

# Partie 1 - Lecture du fichier
def read_file(filename):
    values_list = []
    try:
        # Vérifier si le fichier existe
        if not os.path.exists(filename):
            print(f"✗ ERREUR: Le fichier '{filename}' n'existe pas!")
            print(f"📁 Dossier courant: {os.getcwd()}")
            print("📋 Fichiers disponibles dans le dossier:")
            for f in os.listdir('.'):
                if f.endswith('.txt'):
                    print(f"   - {f}")
            return []
        
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print(f"✗ ERREUR: Le fichier '{filename}' est vide!")
                return []
            
            for i, line in enumerate(lines):
                try:
                    values_list.append(int(line.strip()))
                except ValueError:
                    print(f"✗ ERREUR: Ligne {i+1} n'est pas un entier: '{line.strip()}'")
                    return []
            
        print(f"✓ SUCCÈS: {len(values_list)} valeurs lues depuis '{filename}'")
        print(f"📊 Premières 5 valeurs: {values_list[:5]}")
        
    except Exception as e:
        print(f"✗ ERREUR inattendue: {e}")
    
    return values_list

# Partie 1 - Comptage des occurrences (version lente)
def nombre_occurrences(values_list):
    occurrences = {}
    iterations = 0
    
    for i in range(len(values_list)):
        valeur = values_list[i]
        deja_compte = False
        
        for j in range(i):
            iterations += 1
            if values_list[j] == valeur:
                deja_compte = True
                break
        
        if not deja_compte:
            count = 0
            for k in range(len(values_list)):
                iterations += 1
                if values_list[k] == valeur:
                    count += 1
            occurrences[valeur] = count
    
    print(f"Nombre d'itérations: {iterations}")
    return occurrences

# Partie 1 - Comptage des occurrences (version améliorée)
def nombre_occurrences_ameliore(values_list):
    start_time = time.time()
    occurrences = {}
    iterations = 0
    
    for valeur in values_list:
        iterations += 1
        if valeur in occurrences:
            occurrences[valeur] += 1
        else:
            occurrences[valeur] = 1
    
    end_time = time.time()
    print(f"Nombre d'itérations: {iterations}")
    print(f"Temps d'exécution: {end_time - start_time:.6f} secondes")
    
    # Afficher quelques occurrences
    print("📈 5 premières occurrences:")
    for i, (val, count) in enumerate(list(occurrences.items())[:5]):
        print(f"   {val}: {count} fois")
    
    return occurrences

# Partie 2 - Tri par sélection
def selection_sort(arr):
    start_time = time.time()
    n = len(arr)
    arr = arr.copy()
    iterations = 0
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            iterations += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    end_time = time.time()
    print(f"Nombre d'itérations: {iterations}")
    print(f"Complexité: O(n²)")
    print(f"Temps d'exécution: {end_time - start_time:.6f} secondes")
    print(f"🔍 5 premières valeurs triées: {arr[:5]}")
    return arr

# Partie 2 - Tri par fusion
def merge_sort(arr):
    global merge_iterations
    merge_iterations = 0
    
    def merge(left, right):
        global merge_iterations
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            merge_iterations += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:

                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def sort(sub_arr):
        global merge_iterations
        merge_iterations += 1
        
        if len(sub_arr) <= 1:
            return sub_arr
        
        mid = len(sub_arr) // 2
        left = sort(sub_arr[:mid])
        right = sort(sub_arr[mid:])
        
        return merge(left, right)
    
    start_time = time.time()
    result = sort(arr.copy())
    end_time = time.time()
    
    print(f"Nombre d'itérations: {merge_iterations}")
    print(f"Complexité: O(n log n)")
    print(f"Temps d'exécution: {end_time - start_time:.6f} secondes")
    print(f"🔍 5 premières valeurs triées: {result[:5]}")
    return result

# Partie 2 - Sauvegarde du tableau trié
def write_to_file(values, filename):
    try:
        with open(filename, 'w') as file:
            for value in values:
                file.write(f"{value}\n")
        print(f"💾 Les valeurs triées ont été sauvegardées dans {filename}")
        print(f"📁 Nombre de valeurs sauvegardées: {len(values)}")
    except Exception as e:
        print(f"✗ Erreur lors de l'écriture du fichier: {e}")

# Programme principal
    print("=" * 60)
    print("🎯 TP1 - ANALYSE D'ALGORITHMES")
    print("=" * 60)
    
    # Lecture directe du fichier
    values_list = read_file('valeurs_aleatoires.txt')
    
    if values_list:
        print("\n" + "="*50)
        print("🔢 ANALYSE DES OCCURRENCES")
        print("="*50)
        
        # Comptage des occurrences (version lente)
        print("\n1. Version lente:")
        occ_lent = nombre_occurrences(values_list)
        print(f"Nombre de valeurs uniques: {len(occ_lent)}")
        
        # Comptage des occurrences (version améliorée)
        print("\n2. Version améliorée:")
        occ_rapide = nombre_occurrences_ameliore(values_list)
        print(f"Nombre de valeurs uniques: {len(occ_rapide)}")
        
        print("\n" + "="*50)
        print("📊 COMPARAISON DES ALGORITHMES DE TRI")
        print("="*50)
        
        # Tri par sélection
        print("\n1. Tri par sélection:")
        sorted_selection = selection_sort(values_list)
        
        # Tri par fusion
        print("\n2. Tri par fusion:")
        sorted_merge = merge_sort(values_list)
        
        # Sauvegarde
        print("\n3. Sauvegarde:")
        write_to_file(sorted_merge, "valeurs_aleatoires_tries.txt")
        
        # Vérification
        print(f"\n✅ Vérification: Les deux tris donnent le même résultat? {sorted_selection == sorted_merge}")
        
        print("\n" + "="*50)
        print("🎉 PROGRAMME TERMINÉ AVEC SUCCÈS!")
        print("="*50)
        
    else:
        print("\n❌ ARRÊT DU PROGRAMME - Aucune donnée à traiter")
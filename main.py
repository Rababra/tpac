import time
import sys
import os

# Changer le répertoire courant vers celui où se trouve le script. 
# Cela évite les erreurs "file not found" lorsque vous lisez ou écrivez des fichiers.
os.chdir(os.path.dirname(__file__))
def format_time_dhms(seconds):
    days = int(seconds // 86400)  # 1 day = 86400 seconds
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{days} d {hours} h {minutes} min {secs:.2f} sec"
#############################################################################################################################
# QUESTION 1 – Lecture du fichier
# Écrire une fonction Python permettant de lire les valeurs entières du fichier valeurs_aleatoires.txt
# La lecture doit se faire à l’aide d’une liste, en convertissant chaque ligne en entier.
#############################################################################################################################

def read_file(file_name):
    # Ouvre le fichier en mode lecture 'r'
    file = open(file_name, 'r')
    values = []   # Liste qui va contenir les entiers du fichier
    for line in file:
        # Convertir chaque ligne en entier et l'ajouter à la liste
        values.append(int(line.strip()))
    file.close()  # Fermer le fichier après lecture
    return values    

#############################################################################################################################
# QUESTION 2 – Comptage des occurrences (Complexité O(n²))
# Écrire une fonction nombre_occurrences(values_list) utilisant :
# - une boucle imbriquée
# - un dictionnaire pour stocker les occurrences
#
# QUESTION 3 – Analyse algorithmique
# - Indiquer le nombre exact d’itérations
# - Déterminer la complexité temporelle en notation O.
# - Intégrer un chronomètre pour mesurer la durée d’exécution
#############################################################################################################################

def nombre_occurrences(values_list):
    iterations = 0
    start_time = time.time()
    occurrences = dict()
    remaining_time = 0

    for i in range(n):
        iterations += 1
        count = 0
        for j in range(n):
            iterations += 1
            if values_list[j] == values_list[i]:
                count += 1
            occurrences[values_list[i]] = count
        
        #               100% --> n
        # elapsed_percentage --> i+1 => elapsed_percentage  = (i + 1) * 100 / n  
        elapsed_percentage   = (i + 1) * 100 / n
        remaining_percentage = 100 - elapsed_percentage 

        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_percentage  > 0:
            #    elapsed_time --> elapsed_percentage 
            #  remaining_time --> remaining_percentage => remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
            remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
        
        # Affiche la progression sur une seule ligne en écrasant l'affichage précédent.
        # \r ramène le curseur au début de la ligne, sys.stdout.write écrit le texte sans retour à la ligne,
        # et le formatage affiche le pourcentage, le temps écoulé et le temps restant estimé.
        sys.stdout.write(f"\rProgress: {elapsed_percentage:.2f}%, "f"Elapsed Time: {format_time_dhms(elapsed_time)}, "f"Remaining Time: {format_time_dhms(remaining_time)}"
)


        # Force l'affichage immédiat du texte (sinon Python peut attendre avant d'afficher).
        sys.stdout.flush()  

    end_time = time.time()
    print(f"\n⏱ Durée totale du comptage : {format_time_dhms(end_time - start_time)}")
    print(f"Nombre total d’itérations : {iterations}")
    return occurrences
# fin nombre_occurrences

#############################################################################################################################
# QUESTION 4 – Amélioration du calcul des occurrences (Complexité O(n))
# Écrire une fonction nombre_occurrences_ameliore(values_list)
# Objectif : réduire la complexité de O(n²) → O(n)
#############################################################################################################################

def nombre_occurrences_ameliore(values_list):
    iterations = 0
    start_time = time.time()
    occurrences = {}

    for val in values_list:
        iterations += 1
        if val in occurrences:
            occurrences[val] += 1
        else:
            occurrences[val] = 1

    end_time = time.time()
    print(f"\n⏱ Durée totale (amélioré) : {format_time_dhms(end_time - start_time)}")
    print(f"Nombre total d’itérations (amélioré) : {iterations}")
    return occurrences


#############################################################################################################################
# QUESTION 5 – Tri par sélection (Selection Sort)
# Écrire une fonction selection_sort() qui :
# - trie les éléments en ordre croissant
# - indique le nombre exact d’itérations
# - affiche la complexité 
# - intègre un chronomètre
#############################################################################################################################

def selection_sort(values_list):
    arr = values_list[:]  # copie pour ne pas modifier l’original
    n = len(arr)
    comparisons = 0
    start_time = time.time()

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    end_time = time.time()
    print(f"\n⏱ Durée totale (Selection Sort) :  {format_time_dhms(end_time - start_time)}")
    print(f"Nombre total de comparaisons : {comparisons} (attendu n(n-1)/2)")
    return arr



#############################################################################################################################
# QUESTION 6 – Tri par fusion (Merge Sort)
# Écrire une fonction merge_sort(tab) qui :
# - trie les éléments en ordre croissant
# - compte le nombre d’itérations
# - affiche la complexité : O(n log n)
# - intègre un chronomètre
#############################################################################################################################

def merge(left, right):
    result = []
    i = j = 0
    comparisons = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, comparisons

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, comp_left = merge_sort(arr[:mid])
    right, comp_right = merge_sort(arr[mid:])
    merged, comp_merge = merge(left, right)
    return merged, comp_left + comp_right + comp_merge

def timed_merge_sort(values_list):
    start_time = time.time()
    sorted_arr, comparisons = merge_sort(values_list)
    end_time = time.time()
    print(f"\n⏱ Durée totale (Merge Sort) :  {format_time_dhms(end_time - start_time)}")
    print(f"Nombre total de comparaisons ~ O(n log n) : {comparisons}")
    return sorted_arr


#############################################################################################################################
# QUESTION 7 – Sauvegarde du tableau trié
# Écrire une fonction write_to_file(tab) qui enregistre les valeurs triées dans 
# un fichier nommé valeurs_aleatoires_tries.txt
#############################################################################################################################

def write_to_file(values, file_name="valeurs_aleatoires_tries.txt"):
    with open(file_name, "w") as file:
        for val in values:
            file.write(f"{val}\n")
    print(f"\n💾 Fichier sauvegardé : {file_name}")



#############################################################################################################################
# Début du script principal
#############################################################################################################################

# 1. Lecture du fichier
valeurs_aleatoires_list = read_file('valeurs_aleatoires.txt')
list_length = len(valeurs_aleatoires_list)
n = len(valeurs_aleatoires_list) # n est utilisé dans nombre_occurrences

print('Valeurs lues :', valeurs_aleatoires_list[:10], '...')
print('Longueur de la liste (n) :', n)

# 2. & 3. Comptage des occurrences (O(n²))
occurrences_on2 = nombre_occurrences(valeurs_aleatoires_list)
# print("Occurrences (O(n²)) :", occurrences_on2)

# 4. Comptage des occurrences amélioré (O(n))
occurrences_on = nombre_occurrences_ameliore(valeurs_aleatoires_list)
print("Occurrences (O(n)) :", occurrences_on)

# 5. Tri par sélection (Selection Sort)
sorted_selection = selection_sort()

# 6. Tri par fusion (Merge Sort)
sorted_merge = merge_sort()

# 7. Sauvegarde du tableau trié
write_to_file(sorted_merge)






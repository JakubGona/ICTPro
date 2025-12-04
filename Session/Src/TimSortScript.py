# ANSI farby
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def highlight(arr, i, j):
    """Vytlačí zoznam s farebným zvýraznením indexov i a j."""
    out = []
    for idx, val in enumerate(arr):
        if idx == i:
            out.append(f"{RED}{val}{RESET}")
        elif idx == j:
            out.append(f"{YELLOW}{val}{RESET}")
        else:
            out.append(str(val))
    print(" ".join(out))


# --- INSERTION SORT pre malé runs ---
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:

            highlight(arr, j, j-1)  # zobraz porovnávanie

            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

            highlight(arr, j, j+1)  # po výmene
            print()
        print()


# --- MERGE dvôch runs ---
def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):

        # zvýrazni porovnávanie
        highlight(arr, k, k)
        print()

        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


# --- TIMSORT ---
def timsort(arr):
    n = len(arr)
    RUN = 32  # veľkosť malých blokov

    # 1) najprv zotriedime malé runs insertion sortom
    for start in range(0, n, RUN):
        end = min(start + RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    # 2) potom spájame runs ako pri merge sort
    size = RUN
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + size * 2 - 1)

            if mid < right:
                merge(arr, left, mid, right)
                print()
        size *= 2


# --- TEST ---
numbers = [15, 20, 7, 3, 6, 11, 12]

print("Pôvodné čísla:")
print(*numbers)
print()

timsort(numbers)

print("Výsledok:")
print(*numbers)
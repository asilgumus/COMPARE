# COMPARE

**COMPARE** is a lightweight Python library for basic list comparison and analysis. It provides easy-to-use functions to analyze differences, detect duplicates, and perform simple statistical operations on lists.

## Features

    - Calculate element-wise differences between two lists (`listDiff`)
    - Check if two lists are exactly equal (`isListEqual`, `isListEqualUNO`)
    - Find indices of differing elements (`whichDiff`)
    - Identify missing or extra elements (`missingElements`, `extraElements`)
    - Detect duplicate elements (`duplicates`)
    - Compute statistical measurements:
    - Mean difference (`meanDifference`)
    - Maximum difference (`maxDifference`)
    - Mean percentage deviation (`mean_percentage_deviation`)

## Installation

    Clone the repository and import it into your project:

    git clone https://github.com/asilgumus/COMPARE.git
    pip install -r requirements.txt

# Usage
    from compare import *

    list1 = [1, -2, 3, 4, 5, 6, 6, 2, 3, 4, 7, 7]
    list2 = [1, 2, 3, 4, 5]
    list3 = [1, 2, 3, 5, 4]

    # Max difference
    print(maxDifference(list3, list1))  # 7

    # Element-wise difference
    print(listDiff(list1, list2))

    # Indices of differences
    print(whichDiff(list1, list2))

    # Duplicates in a list
    print(duplicates(list1))

    # Mean percentage deviation
    print(mean_percentage_deviation(list1, list2))
License
    This project is licensed under the MIT License. See the LICENSE file for details.
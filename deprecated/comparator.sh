#!/bin/env bash

# bash comparator.sh <input.cpp> <prog1.cpp> <prog2.cpp> <groupNumber>
INPUT_SOURCE=$1
PROG1_SOURCE=$2
PROG2_SOURCE=$3
GROUP_NUMBER=$4

# Colors
BOLD="\033[1m"
GREY="\033[1;30m"
RED="\033[1;31m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
BLUE="\033[1;34m"
PURPLE="\033[1;35m"
OFF="\033[m"

HEADER_INFO="${BLUE}[INFO]$OFF "
HEADER_WARN="${YELLOW}[WARN]$OFF "
HEADER_ERROR="${RED}[ERROR]$OFF "
HEADER_BUILD="${PURPLE}[BUILD]$OFF "
HEADER_SUCCESS="${GREEN}[SUCCESS]$OFF "

CC="gcc"
CFLAGS="-std=c11 -g"
CXX="g++"
CXXFLAGS="-g -std=c++17"

echo ""

compileSource() {
    echo -e -n "${HEADER_BUILD}Compiling ${BOLD}$1${OFF}..."
    local SOURCE=$1
    ${CXX} ${CXXFLAGS} "$1" -o "${SOURCE//.cpp/}"

    if [[ $? -eq 0 ]]; then
        echo -e "${GREEN} done${OFF}"
    else
        exit 1
    fi
}

deleteEXE() {
    if [[ $(uname) =~ NT ]]; then
        rm -f ${INPUT_SOURCE//.cpp/.exe}
        rm -f ${PROG1_SOURCE//.cpp/.exe}
        rm -f ${PROG2_SOURCE//.cpp/.exe}
    else
        rm -f ${INPUT_SOURCE//.cpp/}
        rm -f ${PROG1_SOURCE//.cpp/}
        rm -f ${PROG2_SOURCE//.cpp/}
    fi
}

compileSource "${INPUT_SOURCE}"
compileSource "${PROG1_SOURCE}"
compileSource "${PROG2_SOURCE}"
echo ""

COUNTER=0

while [[ $# -gt 0 ]]; do
    COUNTER=$((COUNTER + 1))
    echo -e -n "${HEADER_INFO}Round ${BOLD}${COUNTER}${OFF}, comparing..."

    INPUT=$(./${INPUT_SOURCE//.cpp/})
    PROG1=$(echo ${INPUT} | ./${PROG1_SOURCE//.cpp/})
    PROG2=$(echo ${INPUT} | ./${PROG2_SOURCE//.cpp/})

    if [[ "$PROG1" != "$PROG2" ]]; then
        echo -e "${RED} failed${OFF}"
        echo -e "${HEADER_ERROR}${YELLOW}INPUT: ${OFF}\n${INPUT}\n"
        echo -e "${HEADER_ERROR}${BOLD}${PROG1_SOURCE//.cpp/} ${YELLOW}OUTPUT: ${OFF}\n${PROG1}\n"
        echo -e "${HEADER_ERROR}${BOLD}${PROG2_SOURCE//.cpp/} ${YELLOW}OUTPUT: ${OFF}\n${PROG2}\n"
        deleteEXE
        break
    fi

    echo -e "${GREEN} done${OFF}"

    if [[ $GROUP_NUMBER ]]; then
        if [[ COUNTER -eq GROUP_NUMBER ]]; then
            echo -e "\n${HEADER_SUCCESS}Congratulations! There is no difference!"
            deleteEXE
            break
        fi
    fi
done

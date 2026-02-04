#ifndef ENTROPY_CORE_H
#define ENTROPY_CORE_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Struct for analysis result
typedef struct {
    int score;
    char status[20];
    char color_code[10];
    int has_upper;
    int has_lower;
    int has_digit;
    int has_symbol;
    int length;
} AnalysisResult;

// Core Functions
char* generate_complex(int length, int use_symbols);
char* generate_memorable(int word_count, char separator, int add_digit);
AnalysisResult analyze_password(const char* password);
void free_password(char* password);

#endif

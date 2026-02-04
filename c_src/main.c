#include "entropy_core.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Forward decls from utils.c
void my_sleep(int ms);
void clear_screen();
void flush_buffer();
void loading_bar(const char *message, int ms_duration);

#define COLOR_RESET "\033[0m"
#define COLOR_RED "\033[1;31m"
#define COLOR_GREEN "\033[1;32m"
#define COLOR_YELLOW "\033[1;33m"
#define COLOR_CYAN "\033[1;36m"
#define COLOR_MAGENTA "\033[1;35m"
#define COLOR_WHITE "\033[1;37m"

void print_banner() {
  clear_screen();
  printf(COLOR_CYAN "======================================================\n");
  printf("|                                                    |\n");
  printf("|               🛡️  ENTROPY PASS SYSTEM               |\n");
  printf("|      Secure Identity Management Module v3.0        |\n");
  printf("|                                                    |\n");
  printf(
      "======================================================\n" COLOR_RESET);
}

void handle_complex() {
  int len, sym;
  char c;
  printf(COLOR_CYAN "\n[?] Length (Default: 16): " COLOR_RESET);
  char buffer[10];
  fgets(buffer, sizeof(buffer), stdin);
  len = atoi(buffer);
  if (len <= 0)
    len = 16;

  printf(COLOR_CYAN "[?] Include Symbols? (Y/n): " COLOR_RESET);
  c = getchar();
  sym = (c == 'n' || c == 'N') ? 0 : 1;
  flush_buffer();

  loading_bar("Encrypting entropy pool", 800);
  char *pwd = generate_complex(len, sym);
  if (pwd) {
    printf("\n" COLOR_GREEN "+------------------------------------------+\n");
    printf("| %-40s |\n", "GENERATED KEY");
    printf("+------------------------------------------+\n");
    printf("| %-40s |\n", pwd);
    printf("+------------------------------------------+\n" COLOR_RESET);
    free_password(pwd);
  }
}

void handle_memorable() {
  int count;
  char sep;
  printf(COLOR_GREEN "\n[?] Word Count (Default: 4): " COLOR_RESET);
  char buffer[10];
  fgets(buffer, sizeof(buffer), stdin);
  count = atoi(buffer);
  if (count <= 0)
    count = 4;

  printf(COLOR_GREEN "[?] Separator (- . _): " COLOR_RESET);
  scanf("%c", &sep);
  flush_buffer();

  loading_bar("Fetching dictionary", 600);
  char *pass = generate_memorable(count, sep, 1);
  if (pass) {
    printf("\n" COLOR_MAGENTA "+------------------------------------------+\n");
    printf("| %-40s |\n", "MEMORABLE PASSPHRASE");
    printf("+------------------------------------------+\n");
    printf("| %-40s |\n", pass);
    printf("+------------------------------------------+\n" COLOR_RESET);
    free_password(pass);
  }
}

void handle_analysis() {
  char password[256];
  printf(COLOR_MAGENTA "\n[?] Enter Password to Scan: " COLOR_RESET);
  scanf("%255s", password);
  flush_buffer();

  loading_bar("Scanning vulnerability database", 1000);
  AnalysisResult res = analyze_password(password);

  printf("\n%s=== ANALIZ RAPORU ===\n", res.color_code);
  printf("GUVENLIK SEVIYESI: %s\n", res.status);
  printf("SCORE: %d%%\n", res.score);

  printf("\n[+] Strengths:\n");
  if (res.length >= 12)
    printf("  - Good Length\n");
  if (res.has_digit && res.has_symbol)
    printf("  - Complex Character Set\n");

  printf("\n[-] Weaknesses (if any):\n");
  if (res.length < 12)
    printf("  - Short Length\n");
  if (!res.has_symbol)
    printf("  - No Symbols\n");
  printf("=====================\n" COLOR_RESET);
}

int main() {
  srand(time(NULL));

  while (1) {
    print_banner();

    printf("1. Generate Complex Password\n");
    printf("2. Generate Memorable Passphrase\n");
    printf("3. Analyze Password Strength\n");
    printf(COLOR_RED "4. Exit System\n" COLOR_RESET);

    printf(COLOR_CYAN "\nCOMMAND > " COLOR_RESET);

    int choice;
    if (scanf("%d", &choice) != 1) {
      flush_buffer();
      continue;
    }
    flush_buffer();

    switch (choice) {
    case 1:
      handle_complex();
      break;
    case 2:
      handle_memorable();
      break;
    case 3:
      handle_analysis();
      break;
    case 4:
      printf(COLOR_RED "\nShutting down Entropy...\n" COLOR_RESET);
      return 0;
    default:
      printf("Invalid choice!\n");
    }

    printf("\nPress Enter to continue...");
    getchar();
  }
  return 0;
}

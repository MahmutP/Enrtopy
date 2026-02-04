#include "entropy_core.h"
#include <ctype.h>
#include <time.h>

// Note: In a real production environment, replace rand() with a CSPRNG.
// For this port, we are keeping standar library rand() but isolating it.

const char *word_list[] = {
    "sky",     "blue",  "falcon", "eagle",   "mountain", "river",  "silent",
    "storm",   "cyber", "neon",   "solar",   "crypto",   "vault",  "shield",
    "alpha",   "delta", "shadow", "ghost",   "flame",    "iron",   "steel",
    "titan",   "atlas", "hyper",  "kirmizi", "beyaz",    "siyah",  "mavi",
    "dag",     "deniz", "gunes",  "yildiz",  "aslan",    "kaplan", "kartal",
    "demir",   "celik", "altin",  "cesur",   "guclu",    "kale",   "kapi",
    "anahtar", "kilit", "sifre",  "veri",    "istanbul", "ankara", "efsane",
    "destan",  "bilgi", "zeka",   "sanat",   "bilim",    "uzay",   "zaman"};
const int word_list_size = 56;

char *generate_complex(int length, int use_symbols) {
  char pool[100] =
      "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  if (use_symbols) {
    strcat(pool, "!@#$%^&*()_+-=[]{}|;:,.<>?");
  }

  char *password = (char *)malloc((length + 1) * sizeof(char));
  if (!password)
    return NULL;

  int pool_len = strlen(pool);
  for (int i = 0; i < length; i++) {
    password[i] = pool[rand() % pool_len];
  }
  password[length] = '\0';
  return password;
}

char *generate_memorable(int word_count, char separator, int add_digit) {
  // Estimate size: words (avg 7 chars) + separators + digit (~3)
  char *passphrase = (char *)malloc(256 * sizeof(char));
  if (!passphrase)
    return NULL;
  passphrase[0] = '\0';

  for (int i = 0; i < word_count; i++) {
    const char *word = word_list[rand() % word_list_size];
    char temp_word[50];
    strcpy(temp_word, word);
    temp_word[0] = toupper(temp_word[0]);

    strcat(passphrase, temp_word);

    if (i < word_count - 1) {
      strncat(passphrase, &separator, 1);
    }
  }

  if (add_digit) {
    char num_str[10];
    sprintf(num_str, "%c%d", separator, rand() % 100);
    strcat(passphrase, num_str);
  }

  return passphrase;
}

AnalysisResult analyze_password(const char *password) {
  AnalysisResult res;
  memset(&res, 0, sizeof(AnalysisResult));

  res.length = strlen(password);
  int score = 0;

  if (res.length >= 20)
    score += 40;
  else if (res.length >= 16)
    score += 30;
  else if (res.length >= 12)
    score += 20;

  for (int i = 0; i < res.length; i++) {
    if (isupper(password[i]))
      res.has_upper = 1;
    if (islower(password[i]))
      res.has_lower = 1;
    if (isdigit(password[i]))
      res.has_digit = 1;
    if (ispunct(password[i]))
      res.has_symbol = 1;
  }

  if (res.has_upper)
    score += 10;
  if (res.has_lower)
    score += 10;
  if (res.has_digit)
    score += 20;
  if (res.has_symbol)
    score += 20;
  if (strchr(password, '-') || strchr(password, '_'))
    score += 10;

  if (score > 100)
    score = 100;
  res.score = score;

  if (score >= 90) {
    strcpy(res.status, "SECURE");
    strcpy(res.color_code, "\033[1;32m"); // Green
  } else if (score >= 60) {
    strcpy(res.status, "MODERATE");
    strcpy(res.color_code, "\033[1;33m"); // Yellow
  } else {
    strcpy(res.status, "VULNERABLE");
    strcpy(res.color_code, "\033[1;31m"); // Red
  }

  return res;
}

void free_password(char *password) {
  if (password)
    free(password);
}

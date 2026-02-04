#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
#include <windows.h>
void my_sleep(int ms) { Sleep(ms); }
void clear_screen() { system("cls"); }
#else
#include <unistd.h>
void my_sleep(int ms) { usleep(ms * 1000); }
void clear_screen() { system("clear"); }
#endif

void flush_buffer() {
  int c;
  while ((c = getchar()) != '\n' && c != EOF)
    ;
}

void loading_bar(const char *message, int ms_duration) {
  printf("%s [", message);
  for (int i = 0; i < 20; i++) {
    printf("=");
    fflush(stdout);
    my_sleep(ms_duration / 20);
  }
  printf("] Done!\n");
  my_sleep(300);
}

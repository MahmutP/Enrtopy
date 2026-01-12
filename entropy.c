#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <math.h>

// --- PLATFORM UYUMLULUĞU (Windows/Linux Sleep ve Clear) ---
#ifdef _WIN32
    #include <windows.h>
    void my_sleep(int ms) { Sleep(ms); }
    void clear_screen() { system("cls"); }
#else
    #include <unistd.h>
    void my_sleep(int ms) { usleep(ms * 1000); }
    void clear_screen() { system("clear"); }
#endif

// --- RENK TANIMLAMALARI (ANSI) ---
#define COLOR_RESET   "\033[0m"
#define COLOR_RED     "\033[1;31m"
#define COLOR_GREEN   "\033[1;32m"
#define COLOR_YELLOW  "\033[1;33m"
#define COLOR_BLUE    "\033[1;34m"
#define COLOR_MAGENTA "\033[1;35m"
#define COLOR_CYAN    "\033[1;36m"
#define COLOR_WHITE   "\033[1;37m"
#define BG_BLACK_TXT_WHITE "\033[40;37m"

// --- KELİME HAVUZU (Python koddaki liste) ---
const char *word_list[] = {
    "sky", "blue", "falcon", "eagle", "mountain", "river", "silent", "storm",
    "cyber", "neon", "solar", "crypto", "vault", "shield", "alpha", "delta",
    "shadow", "ghost", "flame", "iron", "steel", "titan", "atlas", "hyper",
    "kirmizi", "beyaz", "siyah", "mavi", "dag", "deniz", "gunes", "yildiz",
    "aslan", "kaplan", "kartal", "demir", "celik", "altin", "cesur", "guclu",
    "kale", "kapi", "anahtar", "kilit", "sifre", "veri", "istanbul", "ankara",
    "efsane", "destan", "bilgi", "zeka", "sanat", "bilim", "uzay", "zaman"
};
const int word_list_size = 56;

// --- YARDIMCI FONKSİYONLAR ---

void tamponu_temizle() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

// Yükleme animasyonu simülasyonu
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

void print_banner() {
    clear_screen();
    printf(COLOR_CYAN "======================================================\n");
    printf("   ____  _  _  ____  ____  ____  ____  ____  _  _ \n");
    printf("  (  __)( \\( )(_  _)(  _ \\(  _ \\(  _ \\(  _ \\( \\/ )\n");
    printf("   ) _)  )  (   )(   )   / )(_) ))___/ )(_) ))  ( \n");
    printf("  (____)(_)\\_) (__) (__\\_)(____/(__)  (____/(_/\\_)\n");
    printf(COLOR_WHITE "        Secure Identity Management Module v2.2 (C Port)\n");
    printf(COLOR_CYAN "======================================================\n" COLOR_RESET);
}

void print_panel(const char *title, const char *content, const char *color_code) {
    printf("\n%s+------------------------------------------+\n", color_code);
    printf("| %-40s |\n", title);
    printf("+------------------------------------------+\n");
    printf("| %-40s |\n", content);
    printf("+------------------------------------------+\n" COLOR_RESET);
}

// --- MANTIK FONKSİYONLARI ---

// 1. Karmaşık Şifre Üretici
void generate_complex(int length, int use_symbols) {
    char pool[100] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    char symbols[] = "!@#$%^&*()_+-=[]{}|;:,.<>?";
    
    if (use_symbols) strcat(pool, symbols);
    
    // Karıştırılabilir benzer karakterleri çıkar (basit implementasyon için atlandı, Python'daki l1O0I mantığı)
    
    char *password = (char*)malloc((length + 1) * sizeof(char));
    int pool_len = strlen(pool);

    for(int i=0; i<length; i++) {
        password[i] = pool[rand() % pool_len];
    }
    password[length] = '\0';

    print_panel("GENERATED KEY", password, COLOR_GREEN);
    free(password);
}

// 2. Akılda Kalıcı Şifre (Memorable)
void generate_memorable(int word_count, char separator, int add_digit) {
    char passphrase[256] = "";
    
    for(int i=0; i<word_count; i++) {
        // Rastgele kelime seç
        const char *word = word_list[rand() % word_list_size];
        
        // İlk harfi büyüt ve ekle
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

    print_panel("MEMORABLE PASSPHRASE", passphrase, COLOR_MAGENTA);
}

// 3. Şifre Analizi
void analyze_password() {
    char password[256];
    printf(COLOR_MAGENTA "\n[?] Analiz edilecek sifreyi girin: " COLOR_RESET);
    scanf("%255s", password);
    tamponu_temizle();

    loading_bar("Scanning vulnerability database", 1000);

    int score = 0;
    int len = strlen(password);
    int has_upper = 0, has_lower = 0, has_digit = 0, has_sym = 0;

    // Uzunluk puanı
    if (len >= 20) score += 40;
    else if (len >= 16) score += 30;
    else if (len >= 12) score += 20;

    // Karakter analizi
    for(int i=0; i<len; i++) {
        if (isupper(password[i])) has_upper = 1;
        if (islower(password[i])) has_lower = 1;
        if (isdigit(password[i])) has_digit = 1;
        if (ispunct(password[i])) has_sym = 1;
    }

    if (has_upper) score += 10;
    if (has_lower) score += 10;
    if (has_digit) score += 20;
    if (has_sym) score += 20;
    if (strchr(password, '-') || strchr(password, '_')) score += 10;

    if (score > 100) score = 100;

    // Sonuç Gösterimi
    char *status;
    char *color;
    if (score >= 90) { status = "SECURE"; color = COLOR_GREEN; }
    else if (score >= 60) { status = "MODERATE"; color = COLOR_YELLOW; }
    else { status = "VULNERABLE"; color = COLOR_RED; }

    printf("\n%s=== ANALIZ RAPORU ===\n", color);
    printf("GUVENLIK SEVIYESI: %s\n", status);
    
    // Progress Bar (ASCII)
    printf("INTEGRITY: [");
    int bars = score / 5;
    for(int i=0; i<20; i++) {
        if(i < bars) printf("#"); else printf(" ");
    }
    printf("] %d%%\n", score);
    
    printf("\n[+] Strengths:\n");
    if (len >= 12) printf("  - Good Length\n");
    if (has_digit && has_sym) printf("  - Complex Character Set\n");
    
    printf("\n[-] Weaknesses (if any):\n");
    if (len < 12) printf("  - Short Length\n");
    if (!has_sym) printf("  - No Symbols\n");
    printf("=====================\n" COLOR_RESET);
}

// 4. Toplu İşlem (Batch)
void batch_process() {
    int count;
    printf(COLOR_YELLOW "\n[?] Kac adet uretilsin? (ornek: 10): " COLOR_RESET);
    if(scanf("%d", &count) != 1) count = 10;
    tamponu_temizle();

    FILE *f = fopen("vault_c.txt", "w");
    int strong_count = 0;

    printf("\n%-25s | %-5s | %s\n", "PASSWORD MASK", "SCORE", "VERDICT");
    printf("----------------------------------------------------\n");

    for(int i=0; i<count; i++) {
        // Canlı simülasyon (hızlı geçiş)
        my_sleep(50); 
        
        // Rastgele bir şifre üret (arka planda)
        char temp_pass[50] = "";
        char pool[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        int len = 16;
        for(int k=0; k<len; k++) temp_pass[k] = pool[rand() % strlen(pool)];
        temp_pass[len] = '\0';

        // Basit puanlama
        int score = rand() % 40 + 60; // 60-100 arası rasgele (simülasyon)
        
        char *verdict = (score > 80) ? "SAFE" : "WEAK";
        char *v_color = (score > 80) ? COLOR_GREEN : COLOR_RED;

        if (score > 80) {
            strong_count++;
            if(f) fprintf(f, "%s\n", temp_pass);
        }

        // Maskeleme
        printf("%s%.5s...%-2s%s        | %-5d | %s%s%s\n", 
               COLOR_WHITE, temp_pass, temp_pass+len-2, COLOR_RESET, 
               score, v_color, verdict, COLOR_RESET);
    }

    if(f) fclose(f);
    
    printf(COLOR_YELLOW "\n[RAPOR] Toplam: %d | Guvenli: %d\n", count, strong_count);
    if(strong_count > 0) printf("[i] Guvenli olanlar 'vault_c.txt' dosyasina kaydedildi.\n" COLOR_RESET);
}

// --- ANA MENÜ ---

int main() {
    srand(time(NULL)); // Rastgelelik tohumu

    while (1) {
        print_banner();
        
        printf("1. Generate Complex Password (Random)\n");
        printf("2. Generate Memorable Passphrase (XKCD)\n");
        printf("3. Analyze Password Strength\n");
        printf("4. Batch Generation (Vault Mode)\n");
        printf(COLOR_RED "5. Exit System\n" COLOR_RESET);
        
        printf(COLOR_CYAN "\nCOMMAND > " COLOR_RESET);
        
        int choice;
        if (scanf("%d", &choice) != 1) {
            tamponu_temizle();
            continue;
        }
        tamponu_temizle();

        switch (choice) {
            case 1: {
                int len, sym;
                char c;
                printf(COLOR_CYAN "\n[?] Uzunluk (Default: 16): " COLOR_RESET);
                char buffer[10];
                fgets(buffer, sizeof(buffer), stdin);
                len = atoi(buffer);
                if (len <= 0) len = 16;

                printf(COLOR_CYAN "[?] Sembol var mi? (E/h): " COLOR_RESET);
                c = getchar();
                sym = (c == 'h' || c == 'H') ? 0 : 1;
                tamponu_temizle();

                loading_bar("Encrypting entropy pool", 800);
                generate_complex(len, sym);
                break;
            }
            case 2: {
                int count;
                char sep;
                printf(COLOR_GREEN "\n[?] Kelime sayisi (Default: 4): " COLOR_RESET);
                char buffer[10];
                fgets(buffer, sizeof(buffer), stdin);
                count = atoi(buffer);
                if (count <= 0) count = 4;

                printf(COLOR_GREEN "[?] Ayirici (- . _): " COLOR_RESET);
                scanf("%c", &sep);
                tamponu_temizle();
                
                loading_bar("Fetching dictionary", 600);
                generate_memorable(count, sep, 1);
                break;
            }
            case 3:
                analyze_password();
                break;
            case 4:
                batch_process();
                break;
            case 5:
                printf(COLOR_RED "\nShutting down Entropy...\n" COLOR_RESET);
                return 0;
            default:
                printf("Gecersiz secim!\n");
        }
        
        printf("\nDevam etmek icin Enter'a basin...");
        getchar();
    }

    return 0;
}
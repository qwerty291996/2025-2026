#include <iostream>
#include <vector>
#include <random>
#include <fstream>
#include <chrono> // Vaqt bilan ishlash uchun

using namespace std;

int main() {
    ofstream outFile("input.txt");

    int N;
    cout << "N elementlar sonini kiriting: ";
    if (!(cin >> N)) return 0;

    const int MAX_VAL = 100000;

    // Generatorni joriy vaqt (nanosekundlargacha) bilan sozlaymiz
    // Bu har safar dastur ishga tushganda turlicha natija berishini kafolatlaydi
    unsigned seed = chrono::steady_clock::now().time_since_epoch().count();
    mt19937 gen(seed); 

    uniform_int_distribution<int> dist(1, MAX_VAL);

    outFile << N << endl;

    for (int i = 0; i < N; ++i) {
        outFile << dist(gen) << (i == N - 1 ? "" : " ");
    }

    outFile.close();
    cout << N << " ta tasodifiy test 'input.txt' fayliga yozildi!" << endl;

    return 0;
}

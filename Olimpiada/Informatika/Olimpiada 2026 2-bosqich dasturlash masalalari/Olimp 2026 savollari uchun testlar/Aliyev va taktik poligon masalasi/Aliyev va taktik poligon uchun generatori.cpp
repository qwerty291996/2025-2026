#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
    // Faylga yozish uchun oqim
    ofstream outFile("input.txt");

    // Tasodifiylikni ta'minlash uchun vaqtdan foydalanamiz
    unsigned seed = chrono::steady_clock::now().time_since_epoch().count();
    mt19937 gen(seed);

    // Masala cheklovlari
    int n = 999; // Cho'qqilar soni
    int m = gen() % n + 1; // Maksimal ketma-ket pistirmalar (1 dan n gacha)

    // 1. n va m ni chiqaramiz
    outFile << n << " " << m << endl;

    // 2. Pistirmalar (0 yoki 1)
    uniform_int_distribution<int> catDist(0, 1);
    for (int i = 0; i < n; ++i) {
        outFile << catDist(gen) << (i == n - 1 ? "" : " ");
    }
    outFile << endl;

    // 3. Daraxt qirralari (n-1 ta)
    // Daraxt bog'lamli bo'lishi uchun har bir i-cho'qqini 
    // o'zidan oldingi ixtiyoriy j cho'qqiga bog'laymiz
    vector<pair<int, int>> edges;
    for (int i = 2; i <= n; ++i) {
        uniform_int_distribution<int> parentDist(1, i - 1);
        int parent = parentDist(gen);
        edges.push_back({parent, i});
    }

    // Test yanada qiyinroq bo'lishi uchun qirralar tartibini aralashtiramiz
    shuffle(edges.begin(), edges.end(), gen);

    for (const auto& edge : edges) {
        outFile << edge.first << " " << edge.second << endl;
    }

    outFile.close();
    cout << "Test muvaffaqiyatli 'input.txt' fayliga yozildi!" << endl;
    cout << "n = " << n << ", m = " << m << endl;

    return 0;
}

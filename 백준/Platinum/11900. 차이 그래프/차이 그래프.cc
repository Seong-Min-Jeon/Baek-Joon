#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> a(n-1);
    for (int i = 0; i < n-1; i++) {
        cin >> a[i];
    }

    vector<int> d;
    d.reserve(n-1);
    for (int v = 1; v < n; v++) {
        if (a[n-1-v] > 0) {
            d.push_back(v);
        }
    }

    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<>> pq;
    vector<ll> dist(n, LLONG_MAX);
    dist[0] = 0;
    pq.emplace(0LL, 0);

    while (!pq.empty()) {
        auto [cd, u] = pq.top(); 
        pq.pop();
        if (cd > dist[u]) continue;

        for (int dv : d) {
            int v = u + dv;
            if (v >= n) v -= n;

            int idx;
            if (u > v) {
                idx = u - v - 1;
            } else {
                idx = u - v + (n-1);
            }

            if (a[idx] > 0) {
                ll nd = cd + a[idx];
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.emplace(nd, v);
                }
            }
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int x, y;
        cin >> x >> y;
        int dy = (y - x) % n;
        if (dy < 0) dy += n;

        if (dist[dy] == LLONG_MAX) {
            cout << -1 << '\n';
        } else {
            cout << dist[dy] << '\n';
        }
    }

    return 0;
}

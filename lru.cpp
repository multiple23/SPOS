#include <bits/stdc++.h>

using namespace std;

int lru(int pg[],int pn,int fn){
    unordered_set<int>s;
    unordered_map<int,int>ind;
    list<int>fra;
    int paff=0;

    for(int i=0;i<pn;i++){
        if(s.size()<fn){
            if(s.find(pg[i])==s.end()){
                s.insert(pg[i]);
                fra.push_back(pg[i]);
                paff++;
            }

            ind[pg[i]]=i;
        }
        else{
            if(s.find(pg[i])==s.end()){
                int lru=INT_MAX;
                int val=0;
                for(int it:s){
                    if(ind[it]<lru){
                        lru=ind[it];
                        val=it;
                    }

                }

                s.erase(val);
                fra.pop_front();
                fra.push_back(pg[i]);
                s.insert(pg[i]);
                paff++;
            }
            ind[pg[i]]=i;
        }

        cout << "frsme contents: ";
        for(int it: fra){
            cout << it << " ";
        }
        cout << endl;
    }

    return paff;
}


int main() {
    cout << "Enter the value of n: ";
    int n;
    cin >> n;
    int pages[n];

    cout << "Enter the page numbers:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> pages[i];
    }

    cout << "Enter the number of frames: ";
    int capacity;
    cin >> capacity;

    int pageFaultCount = lru(pages, n, capacity);
    cout << "No. of page faults: " << pageFaultCount << endl;

    return 0;
}



#include <bits/stdc++.h>
using namespace std;


void fifo(int pg[],int pn,int fn){
    vector<int>fr;
    queue<int>fifo;
    int paf=0;
    for(int i=0;i<pn;i++){
        cout << "Contents in frame are: ";
        for(int j=0;j<fr.size();j++){
            cout << fr[j] << " ";
        }
        cout << endl;
        int cp=pg[i];
        if(find(fr.begin(),fr.end(),cp)==fr.end()){
            paf++;

            if(fr.size()<fn){
                fr.push_back(cp);
                fifo.push(cp);
            }

            else {
                int rp=fifo.front();
                fifo.pop();
                fr.erase(remove(fr.begin(),fr.end(),rp),fr.end());
                fr.push_back(cp);
                fifo.push(cp);
            }
        }
    }
    cout << "No of hits: " << paf << endl;
    cout << "No of misses: " << pn-paf << endl;
}

int main(){
    cout << "ENter no of pages: ";
    int n;
    cin >> n;
    cout << "Enter frame size: ";
    int fn;
    cin >> fn;
    cout << "Enter page numbers: ";
    int pg[n];
    for(int i=0;i<n;i++){
        cin >> pg[i];

    }
    fifo(pg,n,fn);

    return 0;
}
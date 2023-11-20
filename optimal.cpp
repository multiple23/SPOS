#include <bits/stdc++.h>
using namespace std;

bool search(int key, vector<int>&fr){
    for(int i=0;i<fr.size();i++){
        if(fr[i]==key){
            return true;
        }
    }
    return false;
}

int predict(int pg[],vector<int>&fr,int pn,int index){
    int res=-1;
    int far=index;
    for(int i=0;i<fr.size();i++){
        int j;
        for(int j=index;j<pn;j++){
            if(fr[i]==pg[j]){
                if(j>far){
                    far=j;
                    res=i;
                }
                break;
            }
        }

        if(j==pn){
            return i;
        }
    }

    return (res==-1) ? 0: res;
}


void optimalPage(int pg[],int pn,int fn){
    vector<int>fr;
    int hit=0;
    for(int i=0;i<pn;i++){
        cout << "Contents in frame are: ";
        for(int j=0;j<fr.size();j++){
            cout << fr[j] << " ";
        }
        cout << endl;
        

        if(search(pg[i], fr)){
            hit++;
            continue;
        }

        if(fr.size()<fn){
            fr.push_back(pg[i]);
        }
        else{
            int j=predict(pg,fr,pn,i+1);
            fr[j]=pg[i];
        }

    }

    cout << "No of hits: " << hit << endl;
    cout << "No of misses: " << pn-hit << endl;
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
    optimalPage(pg,n,fn);

    return 0;
}
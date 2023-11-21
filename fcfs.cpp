#include <bits/stdc++.h>
using namespace std;
#define int long long
signed main(){
    cout << "No of praocess: ";
    int n;
    cin >> n;
    vector<vector<int>>v;
    int mn=INT_MAX;
    int mx=INT_MIN;
    cout << "Enter arrival and burst time: ";
    cout << endl;
    for(int i=0;i<n;i++){
        int a,b;
        vector<int>v1;
        cin >> a >> b;
        v1.push_back(a);
        v1.push_back(b);
        v.push_back(v1);
        mn=min(mn,a);
        mx=max(a,mx);
    }

    vector<vector<int>>v2;
    int r=mn;
    vector<int>red;
    for(int i=0;i<n;i++){
        if(v[i][0]==mn){
            vector<int>m=v[i];
            m.push_back(i);
            v2.push_back(m);
            red.push_back(i);
        }
    }

    vector<int>ct;
    for(int i=0;i<n;i++){
        ct.push_back(0);

    }

    while(true){
        if(v2.size()==0 and r>mx)  break;

        if(v2.size()==0) r++;

        else{
            sort(v2.begin(),v2.end());
            r+=v2[0][1];
            for(int i=0;i<n;i++){
                if(v[i][0]>r-v2[0][1] and v[i][0]<=r){
                    vector<int>m1=v[i];
                    m1.push_back(i);
                    v2.push_back(m1);
                    red.push_back(i);
                }
            }

            ct[v2[0][2]]=r;
            v2.erase(v2.begin());
        }
    }

    cout << endl;
    cout << "Ghatt chart:  ";
    for(int i=0;i<n;i++){
        cout << "p" << red[i] << " ";
    }
    cout << endl;

    for(int i=0;i<n;i++){
        v[i].push_back(ct[i]);
        v[i].push_back(ct[i]-v[i][0]);
        v[i].push_back(ct[i]-v[i][0]-v[i][1]);
    }

    cout << "ID   " << "arrivaltime   " << "brusttime   " << "comletiontime   " << "trt  " << "waititme   " << endl;
    for(int i=0;i<n;i++) {
        cout << i+1 << "   "  << v[i][0] << "   " << v[i][1] << "   " << v[i][2] << "   " << v[i][3] << v[i][4] << endl; 
    }
    cout << endl;

    return 0;
}
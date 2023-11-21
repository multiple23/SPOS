#include <bits/stdc++.h>
using namespace std;

#define int long long

signed main(){
    cout << "Enter the number of process; ";
    int n;
    cin >> n;
    cout << "quantum is: ";
    int q;
    cin >> q;
    vector<vector<int>>v;
    int mn=INT_MAX;
    int mx=INT_MIN;
    vector<int>dm;
    cout << "Enter araival and burst time: ";
    for(int i=0;i<n;i++){
        vector<int>v1;
        int a,b;
        cin >> a >> b;
        v1.push_back(a);
        v1.push_back(b);
        v.push_back(v1);
        dm.push_back(b);
        mn=min(mn,a);
        mx=max(a,mx);
        
    }

    int r=mn;
    vector<int>red;
    for(int i=0;i<n;i++){
        if(v[i][0]==mn){
            red.push_back(i);
        }
    }

    vector<int>ct;
    for(int i=0;i<n;i++){
        ct.push_back(0);
    }

    vector<int>g;
    while(true){
        if(red.size()==0 and r>mx) break;
        if(red.size()==0){
            r+=q;
            for(int i=0;i<n;i++){
                if(v[i][0]>r-q and v[i][0]<=r){
                    red.push_back(i);
                }
            }

        }
        else{
            int p=red[0];
            if(v[p][1]-q>0){
                v[p][1]-=q;
                r+=q;
                for(int i=0;i<n;i++){
                    if(v[i][0]>r-q and v[i][0]<=r){
                        red.push_back(i);
                    }
                }

                red.push_back(p);
                g.push_back(p);
                red.erase(red.begin());
            }
            else{
                r+=v[p][1];
                v[p][1]=0;

                for(int i=0;i<n;i++){
                    if(v[i][0]>r-v[p][1] and v[i][0]<=r){
                        red.push_back(i);
                    }
                }

                ct[p]=r;
                g.push_back(p);
                red.erase(red.begin());
            }
        }
    }

    cout<<endl;
    cout<<"gaint chart is : ";
     for(auto x :g) cout<<"p"<<x+1<<" ";
        cout<<endl;
        cout<<endl;
    vector<int>tat;
    for(int i=0;i<n;i++){
        tat.push_back(ct[i]-v[i][0]);
    }
    vector<int>wt;
    for(int i=0;i<n;i++){
        wt.push_back(tat[i]-dm[i]);
    }
    for(int i=0;i<n;i++){
        v[i][1]=dm[i];
        v[i].push_back(ct[i]);
        v[i].push_back(tat[i]);
        v[i].push_back(wt[i]);
    }
    cout<<"id       "<<"at       "<<"bt       "<<"ct       "<<"tat      "<<"wt    "<<endl;
    for(int i=0;i<n;i++){
        cout<<i+1<<"         ";
        for(int j=0;j<v[i].size();j++){
            cout<<v[i][j]<<"        ";
        }
        cout<<endl;
    }

    return 0;

}
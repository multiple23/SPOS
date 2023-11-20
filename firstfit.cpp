#include <bits/stdc++.h>
using namespace std;

void print(int p[],int n,int a[]){
    cout << "\nProcess no \tProcessSize \t Blockallacted\n";
    for(int i=0;i<n;i++){
        cout << " " << i+1 << "\t\t" << p[i] << "\t\t";
        if(a[i]!=-1){
            cout << a[i]+1;
        }   
        else{
            cout << "Not allocated" ;
        }

        cout << endl;
    }
}

void firstfit(int b[],int m,int p[],int n){
    int a[n];
    for(int i=0;i<n;i++){
        a[i]=-1;
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(b[j]>=p[i]){
                a[i]=j;
                b[j]-=p[i];
                break;
            }
        }
    }print(p,n,a);
}


void bestfit(int b[],int m,int p[],int n){
    int a[n];
    for(int i=0;i<n;i++){
        a[i]=-1;
    }

    for(int i=0;i<n;i++){
        int bestInd=-1;
        for(int j=0;j<m;j++){
            if(b[j]>=p[i]){
                if(bestInd==-1){
                    bestInd=j;
                }
                else if(b[bestInd]>b[j]){
                    bestInd=j;
                }
            }
        }
        if(bestInd!=-1){
            a[i]=bestInd;
            b[bestInd]-=p[i];
        }
    }
    print(p,n,a);
}

void worstfit(int b[],int m,int p[],int n){
    int a[n];
    for(int i=0;i<n;i++){
        a[i]=-1;
    }
    
    for(int i=0;i<n;i++){
        int worstind=-1;
        for(int j=0;j<m;j++){
            if(b[j]>=p[i]){
                if(worstind==-1){
                    worstind=j;
                }
                else if(b[worstind]<=b[j]){
                    worstind=j;
                }
            }
        }

        if(worstind!=-1){
            a[i]=worstind;
            b[worstind]-=p[i];
        }
        
    }
    print(p,n,a);



}



void nextfit(int b[],int m,int p[],int n){
    int a[n];
    for(int i=0;i<n;i++){
        a[i]=-1;
    }

    int j=0;
    int t=m-1;
    for(int i=0;i<n;i++){
        while(j<m){
            if(b[j]>=p[i]){
                a[i]=j;
                b[j]-=p[i];
                t=(j-1)%m;
                break;
            }
            if(t==j){
                t=(j-1)%m;
                break;
            }

            j=(j+1)%m;
        }
    }
    print(p,n,a);
}




int main(){
    cout << "Enter no of block size: ";
    int n,m;
    cin >> m;
    cout << "Enter no of process size: ";
    cin >> n;
    int p[n];
    int b[m];
    cout << "Enter the block for process: ";
    for(int i=0;i<m;i++){
        cin >> b[i];
    }
    cout << "Enter the process: ";
    for(int i=0;i<n;i++){
        cin >> p[i];
    }

    cout << "\tMENU\t" << endl;
    cout << "1.firstfit" << endl;
    cout << "2bestfit" << endl;
    cout <<"3.worstfir" << endl;
    cout << "4.nextfit" << endl;
    cout << "Enter choice: " ;
    int ch;
    cin >> ch;
    switch(ch){
        case 1:
        firstfit(b,m,p,n);
        break;
        case 2:
        bestfit(b,m,p,n);
        break;
        case 3:
        worstfit(b,m,p,n);
        break;
        case 4:
        nextfit(b,m,p,n);
        break;
        case 5:
        exit(0);
    }
}
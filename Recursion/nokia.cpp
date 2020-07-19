#include <iostream>
using namespace std;

int findleft(int n , int d[], int pos){
   if(pos==1){
       return 1;
   }
   
   int k=0;
   for(int i = pos-1; i>=0;i--){
       
       k = k+1;
       if(d[i]==1){
           return k;
       }
   }
    
    
}


int findright(int n, int d[], int pos){
    
    if(pos==n){
        return 1;
    } 
    
    int k=0;
    for(int i=pos+1;i<=n+1;i++){
        k=k+1;
        if(d[i]==1){
            return k;
        }
    }
    
}


int findmin(int n,int m,int d[],int pos,int sum=0,int index= 0){
    if(index==n){
        sum += 2;
        return m-sum>=0?m-sum:-1;
    }
    
    if(pos>0){
       d[pos]=1;
       int left = findleft(n,d,pos);
       int right = findright(n,d,pos);
       sum += left+right;
    }
    
    int min = 9999;
    int cost =0;
    for(int i=1;i<=n;i++){
        if(d[i]==0){
         cost = findmin(n,m,d,i,sum,index+1);
         if(cost >=0 && cost<min){
            min = cost;
         }
        }
        
    }
    d[pos]=0;
    return min!=9999?min :-1;
      
    }

int main() {
	// your code goes here
	int t;
	int n,m;
	int pos=0;
	cin>>t;
	while(t>0){
	    
	    cin>> n >> m;
	    int d[n+2]={0};
	    int cost = findmin(n,m,d,pos,0,0);
	    cout<<cost<<endl;
	    --t;
	}
	return 0;
}

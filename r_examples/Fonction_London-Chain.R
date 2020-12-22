


LC=function(triangle)
  {
  n=dim(triangle)[1]
  lambda=0
  beta=0
  for(j in 0:(n-2)){
    Cj_bar0=mean(triangle[1:(n-j-1),j+1])
    Cj_bar1=mean(triangle[1:(n-j-1),j+2])
    num=mean(triangle[1:(n-j-1),j+1]*triangle[1:(n-j-1),j+2])-Cj_bar0*Cj_bar1
    denom=mean(triangle[1:(n-j-1),j+1]^2)-Cj_bar0^2
    lambda[j+1]=num/denom
    beta[j+1]=Cj_bar1-lambda[j+1]*Cj_bar0
  }
  lambda[n-1]=Cj_bar1/Cj_bar0
  beta[n-1]=0
  M_cumule=triangle
  for(j in 1:(n-1)){
    for(i in (n+1-j):n){
      M_cumule[i,j+1]=M_cumule[i,j]*lambda[j]+beta[j]
    }
  }
  prov_LC=0
  for(i in 2:n){
    prov_LC[i]=M_cumule[i,n]-M_cumule[i,(n+1-i)]
  }
  return(list(lambda_LC=lambda,beta_LC=beta,M_cumule=M_cumule,prov_LC_an=prov_LC,prov_LC=sum(prov_LC)))
 }

import json,os,urllib.request as u;E=os.environ.get('MAKEFUN_ENV_URL');D=[(),(),(31,33,14,18,-31,-33,-14,-18),(15,17,-15,-17),(1,-1,16,-16)];D+=[D[3]+D[4]]*2;X=D[2]+D[6];KG=[20,25,10,0,0,10,25,20];F=[0,1,2,3,3,2,1,0];R={0:13,7:14,112:7,119:11};B=[0]*128;N=0;L=0;A=0;J=100000;M=-10**5;U=[];TT={};S=1;C=15;P=-1;K2=[116,4]
for i,v in enumerate((4,2,3,5,6,3,2,4)):B[i]=v;B[112+i]=-v;B[16+i]=1;B[96+i]=-1
Q=[i for i in range(128)if B[i]];K=lambda:(tuple(B),S,C,P);O=lambda t:not t&136;kv=lambda x:KG[x]if x<8 else-12*(x>>3)
def at(q,y):
 for o in(15,17):
  t=q-o*y
  if O(t)and B[t]==y:return 1
 for o in X:
  t=q+o
  if O(t)and B[t]==y*(2 if o in D[2]else 6):return 1
 for o in D[5]:
  t=q+o
  while O(t):
   p=B[t]
   if p:
    if p==5*y or p==y*(3+(o in D[4])):return 1
    break
   t+=o
 return 0
def gen(c):
 ms=[]
 def A(t,q=0):ms.append(s|(t<<7)|(q<<14))
 for s in Q:
  p=B[s]
  if p*S<=0:continue
  a=abs(p);r=s>>4
  if a==1:
   d=16*S
   for o in(0,-1,1):
    t=s+d+o
    if O(t)and(B[t]==0 if o==0 else B[t]*S<0 or t==P)and(o or not c):
     z=r==1+5*(S>0)
     for q in((5,4,3,2)if z else(0,)):A(t,q)
     if not o and r==1+5*(S<0)and B[s+2*d]==0:A(s+2*d)
  else:
   for o in D[a]:
    t=s+o
    if a in(2,6):
     if O(t)and B[t]*S<=0 and(not c or B[t]*S<0):A(t)
    else:
     while O(t)and B[t]==0:
      if not c:A(t)
      t+=o
     if O(t)and B[t]*S<0:A(t)
  if a==6 and s in(4,116)and not c:
   for z,aa,bb,cc in((1,5,6,7),(2,3,2,0),(4,117,118,119),(8,115,114,112)):
    if C&z and not(B[aa]|B[bb])and(z&5 or not B[bb-1])and B[cc]==4*S and not(at(s,-S)|at(aa,-S)|at(bb,-S)):A(bb)
 return ms
def make(m,u=0):
 global S,C,P
 if u:z=U.pop();B[:]=z[0];S,C,P=z[1:4];K2[:]=z[4];Q[:]=z[5];return
 f=m&127;t=(m>>7)&127;r=m>>14;p=B[f];a=abs(p);U.append((B[:],S,C,P,K2[:],Q[:]));e=t-16*S if a==1 and t==P and B[t]==0 else t
 if B[e]:B[e]=0;Q.remove(e)
 Q[Q.index(f)]=t;B[t]=r*S if r else p;B[f]=0
 if a==6:
  K2[S>0]=t
  if abs(t-f)==2:rf=(f&120)+7*(t>f);rt=(f+t)//2;B[rt]=B[rf];B[rf]=0;Q[Q.index(rf)]=rt
 if a==6:C&=3+9*(S>0)
 C&=R.get(f,15)&R.get(t,15);P=f+16*S if a==1 and abs(t-f)==32 else-1;S=-S
 if at(K2[S<0],S):make(0,1);return 0
 return 1
def ev():
 s=0;k=[0,0]
 for q in Q:
  p=B[q];a=abs(p);r=q>>4;f=q&7;w=r if p>0 else 7-r;g=F[f]+F[w]
  if a==6:k[p<0]=w*8+f;continue
  v=(100+w*w,302+6*g,322+4*g,500,894+2*g)[a-1];s+=v*p//a
 s+=kv(k[0])-kv(k[1]);return s*S
def order(ms,t):ms.sort(key=lambda m:M if m==t else(0 if not(x:=B[(m>>7)&127])else-(6*abs(x)-abs(B[m&127]))))
def negamax(d,a,b,pl):
 global N,A,S,P;N+=1
 if L and N>L:A=1;return 0
 if d<=0:
  ck=at(K2[S>0],-S);be=M if ck else ev()
  if be>=b:return be
  if be>a:a=be
  ms=gen(1-ck);order(ms,0);lg=0
  for m in ms:
   if not make(m):continue
   lg+=1;sc=-negamax(0,-b,-a,pl+1);make(0,1)
   if A:return 0
   if sc>be:be=sc
   if sc>=b:return sc
   if sc>a:a=sc
  if ck and lg==0:return M+pl
  return be
 k=K();e=TT.get(k);tt=0
 if e:
  tt=e[3]
  if e[1]>=d:
   s=e[0]
   if e[2]==1 or e[2]==2 and s>=b or e[2]==3 and s<=a:return s
 ck=at(K2[S>0],-S);a0=a;d+=ck;ms=gen(0);order(ms,tt);lg=0;be=M;bm=0
 for m in ms:
  if not make(m):continue
  lg+=1;sc=-negamax(d-1,-b,-a,pl+1);make(0,1)
  if A:return 0
  if sc>be:be=sc;bm=m
  if sc>a:a=sc
  if a>=b:break
 if lg==0:return M+pl if ck else 0
 TT[k]=(be,d,1+(be>=b)+2*(be<=a0),bm);return be
def root():
 global N,L,A;ms=[m for m in gen(0)if make(m)and not make(0,1)];be=ms[0];N=0;sc={m:0 for m in ms}
 for d in range(1,13):
  L=J*(d>1);A=0;a=M
  for m in ms:
   make(m);s2=-negamax(d-1,M,-a,1);make(0,1)
   if A:break
   sc[m]=s2
   if s2>a:a=s2
  if A:break
  ms.sort(key=lambda m:-sc[m]);be=ms[0]
 return be
post=lambda p,b:json.load(u.urlopen(E+p,json.dumps(b).encode()));sq=lambda c:ord(c[0])-97+(int(c[1])-1)*16
while 1:
 g=post('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  while U:make(0,1)
  for v in g['moves']:make(sq(v)|sq(v[2:])<<7|(len(v)>4 and('nbrq'.index(v[4])+2)<<14))
  m=root();f=m&127;t=(m>>7)&127;r=m>>14;u2='%c%d%c%d%s'%(97+(f&7),(f>>4)+1,97+(t&7),(t>>4)+1,'nbrq'[r-2]if r else'');g=post('/move',{'game':g['game'],'move':u2})

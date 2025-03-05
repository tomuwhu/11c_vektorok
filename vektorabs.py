from browser import document as D, html as H
from random import randrange as R
psz = 0
tsz = 0
def kk():
  D <= H.A("Jutalom: kiskrokodil", href="https://cukisag.blog.hu/media/image/Erika/20110526/kis%20nilusi%20krokodil02%20foto%20Bagosi%20Zoltan.JPG")
def f(e):
  global psz, F, HSZ, _er, tsz
  psz += 1
  if psz > 15:
    F.clear()
    F2.clear()
    F2 <= H.SPAN("Túl sok próbálkozás!", Class="psz")
  HSZ.clear()
  HSZ <= 15 - psz
  af = e.target.id
  if e.target.value == '': return
  v = int(e.target.value)
  if af == 'pp1':
    if v == _er:
      e.target.disabled = True
      tsz += 1
      if tsz == 2:
        kk()
  if af == 'pq1':
    if v == _erq:
      e.target.disabled = True
      tsz += 1
      if tsz == 2:
        kk()
phlist=[
  [3,4,5],
  [3,-4,5],
  [-4,3,5],
  [-4,-3,5],  
  [5,12,13],
  [12,5,13],
  [-5,12,13],
  [12,-5,13],
  [-12,-5,13],
  [20,21,29],
  [21,28,35],
  [-21,28,35],
  [12,35,37],
  [-12,35,37],
  [24,45,51],
  [39,52,65],
  [21,20,29],
  [28,21,35],
  [35,12,37],
  [45,24,51],
  [52,39,65],
]
szhi=R(0,20)
szhv=phlist[szhi]
a1=R(-20,20)
a2=R(-30,20)
sz=R(1,4)
_p11 = str(a1)
_p12 = str(a2)
_p21 = str(szhv[0]*sz+a1)
_p22 = str(szhv[1]*sz+a2)
_er = szhv[2] * sz

szhi=R(0,20)
szhv=phlist[szhi]
a1=R(-210,220)
a2=R(-310,230)
sz=R(4,9)
_q11 = str(a1)
_q12 = str(a2)
_q21 = str(szhv[0]*sz+a1)
_q22 = str(szhv[1]*sz+a2)
_erq = szhv[2] * sz


D <= H.H1("Vektorok - 11c") 

HSZ = H.SPAN(15, Class="psz") 
C = H.DIV(Class="f f1")
C <= H.DIV(f"Koordinátáival adott két pont a síkon:") 
C <= H.DIV([H.SPAN("$$P_1("+_p11+","+_p12+")$$"), " és ", H.SPAN("$$P_2("+_p21+","+_p22+").$$")], Class="p1p2")
F = H.DIV(["Határozza meg a két pont távolságát! ($$|\\vec{P_1P_2}|$$)! "], Class="fel")
F <= H.DIV(H.SPAN("$$|\\vec{P_1P_2}|=$$") <= 
      H.INPUT(id='pp1', type='number').bind("input", f))# <= _er
C <= F <= H.HR()

C <= H.DIV(f"Koordinátáival adott két pont a síkon:") 
C <= H.DIV([H.SPAN("$$Q_1("+_q11+","+_q12+")$$"), " és ", H.SPAN("$$Q_2("+_q21+","+_q22+").$$")], Class="p1p2")
F2 = H.DIV(["Határozza meg a két pont távolságát! ($$|\\vec{Q_1Q_2}|$$)! ", HSZ], Class="fel")
F2 <= H.DIV(H.SPAN("$$|\\vec{Q_1Q_2}|=$$") <= 
      H.INPUT(id='pq1', type='number').bind("input", f))# <= _erq
C <= F2
D <= C


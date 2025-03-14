from browser import document as D, html as H
from random import randrange as R
psz = 0
vsz = 0
mpsz = 45
def f(e):
  global psz, F, HSZ, vsz, mpsz
  psz += 1
  if psz > mpsz:
    F.clear()
    F <= H.SPAN("Túl sok próbálkozás!", Class="psz")
  HSZ.clear()
  HSZ <= mpsz - psz
  af = e.target.id
  if e.target.value == '': return
  v = int(e.target.value)
  if af == 'pp1':
    if v == a1+b1:
      e.target.disabled = True
      vsz += 1
  if af == 'pp2':
    if v == a2+b2:
      e.target.disabled = True
      vsz += 1
  if af == 'pm1':
    if v == a1-b1:
      e.target.disabled = True
      vsz += 1
  if af == 'pm2':
    if v == a2-b2:
      e.target.disabled = True
      vsz += 1
  if af == 'p11':
    if v == c*(a1+b1):
      e.target.disabled = True
      vsz += 1
  if af == 'p12':
    if v == c*(a2+b2):
      e.target.disabled = True
      vsz += 1
  if af == 'p21':
    if v == c*a1-d*b1:
      e.target.disabled = True
      vsz += 1
  if af == 'p22':
    if v == c*a2-d*b2:
      e.target.disabled = True
      vsz += 1
  if af == 'p31':
    if v == d*a1-c*d*b1:
      e.target.disabled = True
      vsz += 1
  if af == 'p32':
    if v == d*a2-c*d*b2:
      e.target.disabled = True
      vsz += 1
  if af == 'p41':
    if v == c*(a1+d*b1):
      e.target.disabled = True
      vsz += 1
  if af == 'p42':
    if v == c*(a2+d*b2):
      e.target.disabled = True
      vsz += 1
  if af == 'p51':
    if v == c*(a1-d*b1):
      e.target.disabled = True
      vsz += 1
  if af == 'p52':
    if v == c*(a2-d*b2):
      e.target.disabled = True
      vsz += 1
  if vsz == 14:
    D <= H.A("Következő feladat", href="https://tomuwhu.github.io/11c_vektorok/vektorabs.html")
a1=R(5,9)
a2=R(1,5)
b1=R(1,4)
b2=R(5,9)
c=R(2,6)
d=R(1,5)
_a1 = str(a1)
_a2 = str(a2)
_b1 = str(b1)
_b2 = str(b2)
_cd = str(c*d)
if d == 1:
  _d = ''
else: _d = str(d)
_c = str(c)
HSZ = H.SPAN(mpsz, Class="psz")
D <= H.H1("Vektorok - 11c") 
C = H.DIV(Class="f f1")
C <= H.DIV(f"Koordinátáikkal adottak ") <= [H.SPAN("$$\\vec{a}("+_a1+","+_a2+")$$"), " és ", H.SPAN("$$\\vec{b}("+_b1+","+_b2+")$$"), " helyvektorok."]
F = H.DIV([f"Határozza meg az alábbi helyvektorok koordinátáit! ", HSZ, H.HR()], Class="fel")
F <= H.DIV(H.SPAN("$$\\vec{a}+\\vec{b}=\\vec{e_1}($$") <= 
      [H.INPUT(id='pp1', type='number').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='pp2', type='number').bind("input", f)]) <= "$$)$$"
F <= H.DIV(H.SPAN("$$\\vec{a}-\\vec{b}=\\vec{e_2}($$") <= 
      [H.INPUT(id='pm1', type='number').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='pm2', type='number').bind("input", f)]) <= "$$)$$"
F <= H.DIV(H.SPAN("$$"+_c+"\\vec{a}+"+_c+"\\vec{b}=\\vec{e_3}($$") <= 
      [H.INPUT(id='p11', type='number').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='p12', type='number').bind("input", f)]) <= "$$)$$"
F <= H.DIV(H.SPAN("$$"+_c+"\\vec{a}-"+_d+"\\vec{b}=\\vec{e_4}($$")  <= 
      [H.INPUT(id='p21', type='number').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='p22', type='number').bind("input", f)]) <= "$$)$$"
F <= H.DIV(H.SPAN("$$"+_d+"\\vec{a}-"+_cd+"\\vec{b}=\\vec{e_5}($$")  <= 
      [H.INPUT(id='p31', type='number').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='p32', type='number').bind("input", f)]) <= "$$)$$"
F <= H.DIV(H.SPAN("$$"+_c+"(\\vec{a}+"+_d+"\\vec{b})=\\vec{e_6}($$")  <= 
      [H.INPUT(id='p41', type='number').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='p42', type='number').bind("input", f)]) <= "$$)$$"
F <= H.DIV(H.SPAN("$$"+_c+"(\\vec{a}-"+_d+"\\vec{b})=\\vec{e_7}($$") <= 
      [H.INPUT(id='p51', type='number').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='p52', type='number').bind("input", f)]) <= "$$)$$"
C <= F
D <= C
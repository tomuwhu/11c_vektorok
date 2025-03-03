from browser import document as D, html as H
from random import randrange as R

def f(e):
  af = e.target.id
  v = int(e.target.value)
  if af == 'p11':
    if v == c*(a1+b1):
      e.target.disabled = True
  if af == 'p12':
    if v == c*(a2+b2):
      e.target.disabled = True
  if af == 'p21':
    if v == c*a1-d*b1:
      e.target.disabled = True
  if af == 'p22':
    if v == c*a2-d*b2:
      e.target.disabled = True
  if af == 'p31':
    if v == d*a1-c*d*b1:
      e.target.disabled = True
  if af == 'p32':
    if v == d*a2-c*d*b2:
      e.target.disabled = True
  if af == 'p41':
    if v == c*(a1+d*b1):
      e.target.disabled = True
  if af == 'p42':
    if v == c*(a2+d*b2):
      e.target.disabled = True
  if af == 'p51':
    if v == c*(a1-d*b1):
      e.target.disabled = True
  if af == 'p52':
    if v == c*(a2-d*b2):
      e.target.disabled = True
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
D <= H.H1("Vektorok - 11c")
C = H.DIV(Class="f f1")
C <= H.DIV(f"Legyen ") <= [H.SPAN("$$\\vec{a}=("+_a1+","+_a2+")$$"), " és ", H.SPAN("$$\\vec{b}=("+_b1+","+_b2+")$$")]
F = H.DIV(f"Határozza meg az alábbi helyvektorok koordinátáit:")
F <= H.DIV(H.SPAN("$$"+_c+"\\vec{a}+"+_c+"\\vec{b}=($$") <= [H.INPUT(id='p11').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='p12').bind("input", f)]) <= "$$)$$"
F <= H.DIV(H.SPAN("$$"+_c+"\\vec{a}-"+_d+"\\vec{b}=($$")  <= [H.INPUT(id='p21').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='p22').bind("input", f)]) <= "$$)$$"
F <= H.DIV(H.SPAN("$$"+_d+"\\vec{a}-"+_cd+"\\vec{b}=($$")  <= [H.INPUT(id='p31').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='p32').bind("input", f)]) <= "$$)$$"
F <= H.DIV(H.SPAN("$$"+_c+"(\\vec{a}+"+_d+"\\vec{b})=($$")  <= [H.INPUT(id='p41').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='p42').bind("input", f)]) <= "$$)$$"
F <= H.DIV(H.SPAN("$$"+_c+"(\\vec{a}-"+_d+"\\vec{b})=($$") <= [H.INPUT(id='p51').bind("input", f), H.SPAN(";", Class="pv"), H.INPUT(id='p52').bind("input", f)]) <= "$$)$$"
C <= F
D <= C
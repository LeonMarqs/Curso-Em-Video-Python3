import math
ang = float(input('Digite o ângulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos (math.radians(ang))
tan = math.tan(math.radians(ang) )
print('sen de {}° = {:.2f}\ncos de {}° = {:.2f}\ntang de {}° = {:.2f}'.format(ang,sin,ang,cos,ang,tan))
import matplotlib.pyplot as plt, numpy as np, math as m

class Soils:
  def __init__(self, data, wm):
    self.wr, self.mesh = list(), list()
    self.wm = wm
    for x, y in data.items():
      self.wr.append(y); self.mesh.append(x)
      
    self.wr = np.array(self.wr)
    self.ret = list( self.wr * 100 / self.wm )
      
    self.passing = list()
    for i, h in enumerate(self.ret):
      if i == 0: 
        valor = 100 - h
        self.passing.append(valor)
      else:
        valor = self.passing[i-1] - h
        self.passing.append(valor)
    
  def d136(self):
    breaker = 0
    self.d10 = '--'
    for k, j in enumerate(self.passing):
      if j < 60 and breaker == 0:
        y1, y2 = j, self.passing[k-1]
        x1, x2 = self.mesh[k], self.mesh[k-1]
        eq = np.polyfit(np.log10([x1, x2]), [y1, y2], 1)
        self.d60 = 10 ** ((60 - eq[1])/ eq[0])
        self.d10 = '--'
        breaker += 1
      elif j < 30 and breaker == 1:
        y1, y2 = j, self.passing[k-1]
        x1, x2 = self.mesh[k], self.mesh[k-1]
        eq = np.polyfit(np.log10([x1, x2]), [y1, y2], 1)
        self.d30 = 10 ** ((30 - eq[1])/ eq[0])
        self.d10 = '--'
        breaker += 1
      elif j < 10 and breaker == 2:
        y1, y2 = j, self.passing[k-1]
        x1, x2 = self.mesh[k], self.mesh[k-1]
        eq = np.polyfit(np.log10([x2, x1]), [y2, y1], 1)
        self.d10 = 10 ** ((10 - eq[1])/ eq[0])
        breaker += 1
      else:
        continue
    
    if self.d10 != '--':
      self.cu = self.d60 / self.d10
      self.cc = ( self.d30 ** 2 ) / ( self.d10 * self.d60)
    else:
      self.d60 = '--'
      self.d30 = '--'
      self.cu, self.cc = '--', '--'
    return {'d60':self.d60, 'd30':self.d30, 'd10':self.d10, 'cu':self.cu, 'cc':self.cc}
  
  def sucs_pre(self):
    self.gravel, self.sand, self.fines, self.sucs = 0, 0, 0, str()
    for y, x in enumerate(self.mesh):
      if x >= 4.76 and y != 0:
        self.gravel = 100 - self.passing[y]
      elif 4.76 > x >= 0.074: 
        self.sand = 100 - self.gravel - self.passing[y]
      else:
        continue
    self.fines = 100 - self.gravel - self.sand

    if type(self.cc) == type("asd") or type(self.cu) == type("asd"):
      self.sucs = '--'
      return {'sand':self.sand, 'gravel':self.gravel, 'fines':self.fines, 'sucs': self.sucs}

    if self.gravel >= 50 and self.fines < 5 and type(self.cc) != type("asd") :
      if self.cu >= 4 and (1 <= self.cc <= 3):
        self.sucs = 'GW'
      else:
        self.sucs = 'GP'
    elif self.sand >= 50 and self.fines < 5 and type(self.cc) != type("asd"):
      if self.cu >= 6 and (1 <= self.cc <= 3):
        self.sucs = 'SW'
      else:
        self.sucs = 'SP'
    else:
      self.sucs = '--'
    
    return {'sand':self.sand, 'gravel':self.gravel, 'fines':self.fines, 'sucs': self.sucs}

  def plasticity(self, lld, pld):
    self.lld, self.pld = lld, pld
    self.x, self.y = list(), list()

    for i in self.lld:
      i.append(i[3] - i[4])
      i.append(i[4] - i[2])
      i.append(i[5] * 100 / i[6])
      self.x.append(i[0]); self.y.append(i[7])

    x_arr, y_arr, w = np.array(self.x), np.array(self.y), 0

    for i in self.pld:
      i.append(i[2] - i[3])
      i.append(i[3] - i[1])
      i.append(i[4] * 100 / i[5])

    for j, i in enumerate(self.pld):
      w += i[6]

    self.pl = w / (j + 1)

    self.eq = np.polyfit(np.log10(x_arr), y_arr, 1)
    self.ll = self.eq[0] * np.log10(25) + self.eq[1]
    self.Ip = self.ll - self.pl
    self.IpA = (11 / 15) * (self.ll - 20)

    cycle = list(np.linspace(10,100,10))
    cycle1 = list(np.linspace(1,10,10))
    self.hit_axis = cycle + cycle1
    self.hit_axis.sort()

    linear_eq = lambda x: self.eq[0] * np.log10(x) + self.eq[1]
    self.wprcnt_ax = list(map(linear_eq, self.hit_axis))

    if self.Ip < self.IpA: self.type = 'M'
    else: self.type = 'C'

    if self.ll < 50: self.comp = 'L'
    else: self.comp = 'H'

    self.classf = self.type + self.comp

    if hasattr(self, 'sucs'):
      if self.gravel >= 50 and self.fines < 5 and type(self.cc) != type("asd") :
        if self.cu >= 4 and (1 <= self.cc <= 3):
          self.sucs = 'GW'
        else:
          self.sucs = 'GP'
      elif self.sand >= 50 and self.fines < 5 and type(self.cc) != type("asd"):
        if self.cu >= 6 and (1 <= self.cc <= 3):
          self.sucs = 'SW'
        else:
          self.sucs = 'SP'
      elif self.fines >= 50 and type(self.cc) != type("asd"):
        self.sucs = self.classf
      elif self.sand >= 50 and 5 <= self.fines <= 12 and type(self.cc) != type("asd"):
        if self.cu >= 4 and (1 <= self.cc <= 3):
          self.sucs = 'SW-S' + self.type
        else:
          self.sucs = 'SP-S' + self.type
      elif self.gravel >= 50 and 5 <= self.fines <= 12 and type(self.cc) != type("asd"):
        if self.cu >= 4 and (1 <= self.cc <= 3):
          self.sucs = 'GW-G' + self.type
        else:
          self.sucs = 'GP-G' + self.type
      elif self.gravel >= 50 and self.fines >= 12 and type(self.cc) != type("asd"):
        self.sucs = 'G' + self.type
      elif self.sand >= 50 and self.fines >= 12 and type(self.cc) != type("asd"):
        self.sucs = 'S' + self.type
    else:
      self.sucs = self.classf

    return {'ll':self.ll, 'pl':self.pl, 'fw':self.eq[0], 'cte':self.eq[1], 'sucs':self.sucs, 'Ip':self.Ip, 'IpA':self.IpA, 'hits': self.hit_axis, 'wc': self.wprcnt_ax, 'x':self.x, 'y':self.y, 'lld':self.lld, 'pld':self.pld}
    